"""
Chatlog Capture Service

Captura conversaciones en tiempo real y las organiza según:
- Rostro ejecutado (MELQUISEDEC, HYPATIA, SALOMON, MORPHEUS, ALMA)
- Fase de la investigación
- Checkpoint results
- Potential lessons identificadas

Escribe en estructura _daath/chatlog/ de cada output:
    metadata.yaml
    full-transcript.md
    by-rostro/01-melquisedec.md
    by-rostro/02-hypatia.md
    ...

Uso:
    capture = ChatlogCapture(output_path="5-outputs/DD-001-semantic-search")

    capture.start_instance(
        instance_id="DD-001-I001",
        domain_id="DD-001",
        prompts_used={"HYPATIA": "v1.0.0", "SALOMON": "v1.0.0"}
    )

    capture.record_message(
        rostro="HYPATIA",
        phase="investigation",
        speaker="user",
        message="Search for papers on semantic search"
    )

    capture.record_checkpoint(
        rostro="HYPATIA",
        checkpoint_name="citations-filtered",
        passed=True
    )

    capture.finalize_instance(status="success")
"""

import os
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Literal


class ChatlogCapture:
    """
    Captura conversaciones estructuradas en _daath/chatlog/.

    Responsabilidades:
    1. Inicializar metadata.yaml con info de instance
    2. Registrar mensajes en full-transcript.md cronológicamente
    3. Separar conversaciones por rostro en by-rostro/
    4. Registrar checkpoints y potential lessons
    5. Finalizar metadata con duración y resultados
    """

    # Mapping rostro → archivo
    ROSTRO_FILES = {
        "MELQUISEDEC": "01-melquisedec.md",
        "HYPATIA": "02-hypatia.md",
        "SALOMON": "03-salomon.md",
        "MORPHEUS": "04-morpheus.md",
        "ALMA": "05-alma.md"
    }

    def __init__(self, output_path: str):
        """
        Args:
            output_path: Path al output (ej: 5-outputs/DD-001-semantic-search)
        """
        self.output_path = Path(output_path)
        self.daath_path = self.output_path / "_daath"
        self.chatlog_path = self.daath_path / "chatlog"
        self.metadata_path = self.chatlog_path / "metadata.yaml"
        self.transcript_path = self.chatlog_path / "full-transcript.md"
        self.by_rostro_path = self.chatlog_path / "by-rostro"

        # Estado interno
        self.metadata: Dict = {}
        self.started_at: Optional[datetime] = None
        self.current_rostro: Optional[str] = None

    # =========================================================================
    # INICIALIZACIÓN
    # =========================================================================

    def start_instance(
        self,
        instance_id: str,
        domain_id: str,
        prompts_used: Dict[str, str],  # {rostro: version}
        git_branch: Optional[str] = None,
        git_commit: Optional[str] = None
    ):
        """
        Inicializa nueva instance de investigación.

        Crea:
        - _daath/chatlog/ directory structure
        - metadata.yaml con info inicial
        - full-transcript.md con header
        - by-rostro/*.md con headers
        """
        # Crear estructura de directorios
        self.chatlog_path.mkdir(parents=True, exist_ok=True)
        self.by_rostro_path.mkdir(exist_ok=True)

        # Timestamp de inicio
        self.started_at = datetime.now(timezone.utc)

        # Inicializar metadata
        self.metadata = {
            "instance_id": instance_id,
            "domain_id": domain_id,
            "created_at": self.started_at.isoformat(),
            "updated_at": self.started_at.isoformat(),
            "status": "in-progress",
            "rostros_executed": {
                rostro: {
                    "prompt_version": version,
                    "started_at": None,
                    "finished_at": None,
                    "checkpoints": [],
                    "potential_lessons": []
                }
                for rostro, version in prompts_used.items()
            },
            "outputs_produced": [],
            "lessons_extracted": 0,
            "rollback_info": None,
            "git_tracking": {
                "branch": git_branch,
                "commit_at_start": git_commit,
                "commit_at_end": None
            }
        }

        # Escribir metadata inicial
        self._write_metadata()

        # Crear full-transcript.md
        self._init_full_transcript()

        # Crear archivos by-rostro
        self._init_by_rostro_files(list(prompts_used.keys()))

    def _write_metadata(self):
        """Escribe metadata.yaml con formato correcto."""
        with open(self.metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.metadata, f, allow_unicode=True, sort_keys=False)

    def _init_full_transcript(self):
        """Inicializa full-transcript.md con header."""
        header = f"""# Chatlog Completo: {self.metadata['instance_id']}

**Domain**: {self.metadata['domain_id']}
**Created**: {self.metadata['created_at']}
**Status**: {self.metadata['status']}

Este archivo contiene la conversación completa en orden cronológico.
Para ver conversaciones por rostro, consulta `by-rostro/`.

---

## Inicio de Instance

**Timestamp**: {self.started_at.isoformat()}

"""

        with open(self.transcript_path, 'w', encoding='utf-8') as f:
            f.write(header)

    def _init_by_rostro_files(self, rostros: List[str]):
        """Crea archivos separados por rostro."""

        for rostro in rostros:
            if rostro not in self.ROSTRO_FILES:
                continue

            filename = self.ROSTRO_FILES[rostro]
            filepath = self.by_rostro_path / filename

            header = f"""# {rostro} - Conversaciones

**Instance**: {self.metadata['instance_id']}
**Prompt Version**: {self.metadata['rostros_executed'][rostro]['prompt_version']}

Este archivo contiene todas las conversaciones del rostro {rostro}.

---

"""

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header)

    # =========================================================================
    # REGISTRO DE MENSAJES
    # =========================================================================

    def record_message(
        self,
        rostro: str,
        phase: str,
        speaker: Literal["user", "assistant", "system"],
        message: str,
        timestamp: Optional[datetime] = None
    ):
        """
        Registra mensaje en full-transcript.md y by-rostro/{rostro}.md.

        Args:
            rostro: Rostro actual (MELQUISEDEC, HYPATIA, etc.)
            phase: Fase de la investigación (classification, investigation, etc.)
            speaker: Quién habla (user, assistant, system)
            message: Contenido del mensaje
            timestamp: Timestamp opcional (default: now)
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        # Actualizar rostro actual
        if self.current_rostro != rostro:
            self.current_rostro = rostro

            # Actualizar started_at del rostro si es primera vez
            if self.metadata['rostros_executed'][rostro]['started_at'] is None:
                self.metadata['rostros_executed'][rostro]['started_at'] = timestamp.isoformat()
                self._write_metadata()

        # Formatear mensaje
        formatted = self._format_message(timestamp, rostro, phase, speaker, message)

        # Escribir en full-transcript
        with open(self.transcript_path, 'a', encoding='utf-8') as f:
            f.write(formatted + "\n\n")

        # Escribir en by-rostro
        if rostro in self.ROSTRO_FILES:
            rostro_file = self.by_rostro_path / self.ROSTRO_FILES[rostro]
            with open(rostro_file, 'a', encoding='utf-8') as f:
                f.write(formatted + "\n\n")

    def _format_message(
        self,
        timestamp: datetime,
        rostro: str,
        phase: str,
        speaker: str,
        message: str
    ) -> str:
        """Formatea mensaje con metadata."""

        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S UTC")

        # Emoji según speaker
        emoji = {
            "user": "👤",
            "assistant": "🤖",
            "system": "⚙️"
        }.get(speaker, "💬")

        return f"""### {emoji} {speaker.upper()} | {rostro} | {phase}

**Timestamp**: {time_str}

{message}"""

    # =========================================================================
    # CHECKPOINTS
    # =========================================================================

    def record_checkpoint(
        self,
        rostro: str,
        checkpoint_name: str,
        passed: bool,
        errors: Optional[List[str]] = None,
        timestamp: Optional[datetime] = None
    ):
        """
        Registra resultado de checkpoint.

        Args:
            rostro: Rostro que ejecutó checkpoint
            checkpoint_name: Nombre del checkpoint
            passed: Si pasó o no
            errors: Lista de errores si falló
            timestamp: Timestamp opcional
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        checkpoint_data = {
            "name": checkpoint_name,
            "passed": passed,
            "timestamp": timestamp.isoformat(),
            "errors": errors or []
        }

        # Agregar a metadata
        self.metadata['rostros_executed'][rostro]['checkpoints'].append(checkpoint_data)
        self._write_metadata()

        # Registrar en transcript
        status_emoji = "✅" if passed else "❌"
        status_text = "PASSED" if passed else "FAILED"

        message = f"""## {status_emoji} Checkpoint: {checkpoint_name}

**Status**: {status_text}
**Timestamp**: {timestamp.isoformat()}
"""

        if not passed and errors:
            message += "\n**Errors**:\n"
            for error in errors:
                message += f"- {error}\n"

        with open(self.transcript_path, 'a', encoding='utf-8') as f:
            f.write(message + "\n")

        # También en by-rostro
        if rostro in self.ROSTRO_FILES:
            rostro_file = self.by_rostro_path / self.ROSTRO_FILES[rostro]
            with open(rostro_file, 'a', encoding='utf-8') as f:
                f.write(message + "\n")

    # =========================================================================
    # POTENTIAL LESSONS
    # =========================================================================

    def record_potential_lesson(
        self,
        rostro: str,
        lesson_text: str,
        confidence: float,
        applies_to_prompt: str,
        timestamp: Optional[datetime] = None
    ):
        """
        Registra potential lesson identificada durante ejecución.

        ALMA las revisará después para extracción formal.
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        lesson_data = {
            "text": lesson_text,
            "confidence": confidence,
            "applies_to_prompt": applies_to_prompt,
            "timestamp": timestamp.isoformat()
        }

        # Agregar a metadata
        self.metadata['rostros_executed'][rostro]['potential_lessons'].append(lesson_data)
        self._write_metadata()

        # Registrar en transcript
        message = f"""## 💡 Potential Lesson Detected

**Rostro**: {rostro}
**Confidence**: {confidence:.2f}
**Applies To**: {applies_to_prompt}
**Timestamp**: {timestamp.isoformat()}

### Lesson Text

{lesson_text}
"""

        with open(self.transcript_path, 'a', encoding='utf-8') as f:
            f.write(message + "\n")

        # También en by-rostro
        if rostro in self.ROSTRO_FILES:
            rostro_file = self.by_rostro_path / self.ROSTRO_FILES[rostro]
            with open(rostro_file, 'a', encoding='utf-8') as f:
                f.write(message + "\n")

    # =========================================================================
    # OUTPUT TRACKING
    # =========================================================================

    def record_output(
        self,
        output_name: str,
        output_path: str,
        version: str,
        rostro: str,
        timestamp: Optional[datetime] = None
    ):
        """Registra output producido durante instance."""

        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        output_data = {
            "name": output_name,
            "path": output_path,
            "version": version,
            "produced_by": rostro,
            "timestamp": timestamp.isoformat()
        }

        self.metadata['outputs_produced'].append(output_data)
        self._write_metadata()

    # =========================================================================
    # FINALIZACIÓN
    # =========================================================================

    def finalize_rostro(self, rostro: str, timestamp: Optional[datetime] = None):
        """Marca rostro como finalizado."""

        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        self.metadata['rostros_executed'][rostro]['finished_at'] = timestamp.isoformat()
        self._write_metadata()

        # Agregar nota en transcript
        message = f"""---

## 🏁 {rostro} Finalizado

**Timestamp**: {timestamp.isoformat()}
**Checkpoints**: {len(self.metadata['rostros_executed'][rostro]['checkpoints'])} ejecutados
**Potential Lessons**: {len(self.metadata['rostros_executed'][rostro]['potential_lessons'])} identificadas

---
"""

        with open(self.transcript_path, 'a', encoding='utf-8') as f:
            f.write(message + "\n")

    def finalize_instance(
        self,
        status: Literal["success", "failed", "partial"],
        git_commit_end: Optional[str] = None,
        rollback_reason: Optional[str] = None,
        timestamp: Optional[datetime] = None
    ):
        """
        Finaliza instance completa.

        Args:
            status: Estado final (success, failed, partial)
            git_commit_end: Commit hash al finalizar
            rollback_reason: Razón si se hizo rollback
            timestamp: Timestamp opcional
        """
        if timestamp is None:
            timestamp = datetime.now(timezone.utc)

        # Calcular duración
        if self.started_at:
            duration = (timestamp - self.started_at).total_seconds()
            duration_formatted = f"{duration / 60:.1f} minutes"
        else:
            duration_formatted = "unknown"

        # Actualizar metadata
        self.metadata['status'] = status
        self.metadata['updated_at'] = timestamp.isoformat()
        self.metadata['finished_at'] = timestamp.isoformat()
        self.metadata['duration'] = duration_formatted

        if git_commit_end:
            self.metadata['git_tracking']['commit_at_end'] = git_commit_end

        if rollback_reason:
            self.metadata['rollback_info'] = {
                "reason": rollback_reason,
                "timestamp": timestamp.isoformat()
            }

        self._write_metadata()

        # Agregar footer en transcript
        status_emoji = {
            "success": "✅",
            "failed": "❌",
            "partial": "⚠️"
        }.get(status, "🏁")

        footer = f"""
---

## {status_emoji} Instance Finalizada

**Status**: {status.upper()}
**Timestamp**: {timestamp.isoformat()}
**Duration**: {duration_formatted}

### Summary

- **Rostros Ejecutados**: {len(self.metadata['rostros_executed'])}
- **Outputs Producidos**: {len(self.metadata['outputs_produced'])}
- **Lessons Extracted**: {self.metadata['lessons_extracted']}

"""

        if rollback_reason:
            footer += f"**⚠️ Rollback**: {rollback_reason}\n"

        with open(self.transcript_path, 'a', encoding='utf-8') as f:
            f.write(footer)


# =============================================================================
# EJEMPLO DE USO
# =============================================================================

if __name__ == "__main__":
    # Crear capture service
    capture = ChatlogCapture(output_path="5-outputs/DD-001-semantic-search")

    # Inicializar instance
    capture.start_instance(
        instance_id="DD-001-I001",
        domain_id="DD-001",
        prompts_used={
            "HYPATIA": "v1.0.0",
            "SALOMON": "v1.0.0",
            "ALMA": "v1.0.0"
        },
        git_branch="main",
        git_commit="abc123def456"
    )
    print("✅ Instance iniciada")

    # Registrar mensajes de HYPATIA
    capture.record_message(
        rostro="HYPATIA",
        phase="investigation",
        speaker="user",
        message="Search for papers on semantic search published after 2020 with >100 citations"
    )

    capture.record_message(
        rostro="HYPATIA",
        phase="investigation",
        speaker="assistant",
        message="I will search arXiv for papers on semantic search. Filtering by date and citations..."
    )

    # Checkpoint
    capture.record_checkpoint(
        rostro="HYPATIA",
        checkpoint_name="citations-filtered",
        passed=True
    )

    # Potential lesson
    capture.record_potential_lesson(
        rostro="HYPATIA",
        lesson_text="Filter papers by citation count (>100 for mature topics) to ensure quality and relevance.",
        confidence=0.95,
        applies_to_prompt="HYPATIA-research-prompt"
    )

    # Output producido
    capture.record_output(
        output_name="research-summary.md",
        output_path="5-outputs/DD-001-semantic-search/research-summary.md",
        version="1.0.0",
        rostro="HYPATIA"
    )

    # Finalizar rostro
    capture.finalize_rostro("HYPATIA")

    # Finalizar instance
    capture.finalize_instance(
        status="success",
        git_commit_end="def456abc789"
    )

    print("✅ Instance finalizada")
    print(f"📁 Chatlog guardado en: {capture.chatlog_path}")

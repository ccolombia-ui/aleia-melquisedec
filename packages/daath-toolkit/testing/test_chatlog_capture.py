"""
Tests for capture.chatlog_capture module

Tests:
- Instance initialization
- Message recording (full transcript + by rostro)
- Checkpoint recording
- Potential lesson capture
- Metadata finalization
- File structure creation
"""

import pytest
from pathlib import Path
from datetime import datetime, timezone
import yaml
import sys
from pathlib import Path as PathLib

# Add parent directory to path for imports
sys.path.insert(0, str(PathLib(__file__).parent.parent))

from capture.chatlog_capture import ChatlogCapture


class TestChatlogCapture:
    """Test suite for ChatlogCapture"""

    def test_initialization_creates_directories(self, temp_output_dir):
        """Initializing capture should create necessary directories"""
        capture = ChatlogCapture(str(temp_output_dir))

        assert capture.chatlog_path == temp_output_dir / "_daath" / "chatlog"
        assert capture.by_rostro_path == temp_output_dir / "_daath" / "chatlog" / "by-rostro"

    def test_start_instance_creates_metadata(self, temp_output_dir):
        """Starting instance should create metadata.yaml"""
        capture = ChatlogCapture(str(temp_output_dir))

        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        assert capture.metadata_path.exists()

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        assert metadata['instance_id'] == "DD-001-I001"
        assert metadata['domain_id'] == "DD-001"
        assert "HYPATIA" in metadata['rostros_executed']

    def test_record_message_writes_to_transcript(self, temp_output_dir):
        """Recording message should write to full-transcript.md"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        capture.record_message(
            rostro="HYPATIA",
            phase="investigation",
            speaker="user",
            message="Search for papers on semantic search"
        )

        assert capture.transcript_path.exists()
        content = capture.transcript_path.read_text(encoding='utf-8')
        assert "HYPATIA" in content
        assert "investigation" in content
        assert "Search for papers on semantic search" in content

    def test_record_message_separates_by_rostro(self, temp_output_dir):
        """Recording messages should separate by rostro file"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0", "SALOMON": "v1.0.0"}
        )

        capture.record_message(
            rostro="HYPATIA",
            phase="investigation",
            speaker="user",
            message="HYPATIA message"
        )

        capture.record_message(
            rostro="SALOMON",
            phase="design",
            speaker="assistant",
            message="SALOMON message"
        )

        # Check HYPATIA file
        hypatia_file = capture.by_rostro_path / "02-hypatia.md"
        assert hypatia_file.exists()
        hypatia_content = hypatia_file.read_text(encoding='utf-8')
        assert "HYPATIA message" in hypatia_content

        # Check SALOMON file
        salomon_file = capture.by_rostro_path / "03-salomon.md"
        assert salomon_file.exists()
        salomon_content = salomon_file.read_text(encoding='utf-8')
        assert "SALOMON message" in salomon_content

    def test_record_checkpoint_adds_to_metadata(self, temp_output_dir):
        """Recording checkpoint should add entry to metadata"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        capture.record_checkpoint(
            rostro="HYPATIA",
            checkpoint_name="citations-filtered",
            passed=True
        )

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        checkpoints = metadata['rostros_executed']['HYPATIA']['checkpoints']
        assert len(checkpoints) == 1
        assert checkpoints[0]['name'] == "citations-filtered"
        assert checkpoints[0]['passed'] is True

    def test_record_potential_lesson_adds_to_metadata(self, temp_output_dir):
        """Recording potential lesson should add entry to metadata"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        capture.record_potential_lesson(
            rostro="HYPATIA",
            lesson_text="Always filter citations by year",
            confidence=0.85,
            applies_to_prompt="HYPATIA-v1.0.0"
        )

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        lessons = metadata['rostros_executed']['HYPATIA']['potential_lessons']
        assert len(lessons) == 1
        assert "Always filter citations" in lessons[0]['text']
        assert lessons[0]['confidence'] == 0.85

    def test_finalize_instance_updates_metadata(self, temp_output_dir):
        """Finalizing instance should update metadata with duration and status"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        capture.finalize_instance(status="success")

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        assert metadata['status'] == "success"
        assert 'finished_at' in metadata
        assert 'duration' in metadata

    def test_multiple_messages_maintain_order(self, temp_output_dir):
        """Multiple messages should maintain chronological order"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        messages = [
            "First message",
            "Second message",
            "Third message"
        ]

        for msg in messages:
            capture.record_message(
                rostro="HYPATIA",
                phase="investigation",
                speaker="user",
                message=msg
            )

        content = capture.transcript_path.read_text(encoding='utf-8')
        # Check order
        first_pos = content.find("First message")
        second_pos = content.find("Second message")
        third_pos = content.find("Third message")

        assert first_pos < second_pos < third_pos

    def test_empty_prompts_dict_handled(self, temp_output_dir):
        """Empty prompts_used dict should be handled gracefully"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={}
        )

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        assert 'rostros_executed' in metadata
        assert metadata['rostros_executed'] == {}

    def test_git_metadata_stored_when_provided(self, temp_output_dir):
        """Git branch and commit should be stored when provided"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"},
            git_branch="feature/semantic-search",
            git_commit="abc123"
        )

        metadata = yaml.safe_load(capture.metadata_path.read_text(encoding='utf-8'))
        assert metadata['git_tracking']['branch'] == "feature/semantic-search"
        assert metadata['git_tracking']['commit_at_start'] == "abc123"

    def test_invalid_rostro_handled_gracefully(self, temp_output_dir):
        """Known rostro in prompts_used should work properly"""
        capture = ChatlogCapture(str(temp_output_dir))
        capture.start_instance(
            instance_id="DD-001-I001",
            domain_id="DD-001",
            prompts_used={"HYPATIA": "v1.0.0"}
        )

        # Should work with known rostro
        capture.record_message(
            rostro="HYPATIA",
            phase="investigation",
            speaker="user",
            message="Test message"
        )

        # Should still write to transcript
        assert capture.transcript_path.exists()

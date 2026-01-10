# Smart-Thinking MCP Server - Docker Container
# Base: Node.js 20 LTS Alpine (ligero)
FROM node:20-alpine

# Metadata
LABEL maintainer="DAATH-ZEN MELQUISEDEC"
LABEL description="Smart-Thinking MCP Server (100% local reasoning)"
LABEL version="11.0.6"

# Variables de entorno
ENV NODE_ENV=production \
    DISABLE_TELEMETRY=true \
    TELEMETRY_DISABLED=1 \
    DO_NOT_TRACK=1 \
    SMART_THINKING_DATA_DIR=/data/sessions

# Crear directorios
WORKDIR /app
RUN mkdir -p /data/sessions && \
    chmod 777 /data/sessions

# Instalar smart-thinking-mcp globalmente
RUN npm install -g smart-thinking-mcp@latest

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD node -e "console.log('OK')" || exit 1

# Exponer puerto (si usa HTTP/SSE)
EXPOSE 8000

# Usuario no-root
USER node

# Comando por defecto (stdio mode para MCP)
CMD ["smart-thinking-mcp"]

#!/usr/bin/env bash
# One-command deployment to Google Cloud Run (Singapore: asia-southeast1)
# Usage:
#   export KB_API_KEY="replace-with-your-strong-secret-token"
#   bash deploy/deploy_cloud_run.sh [SERVICE_NAME] [REGION]

set -euo pipefail

SERVICE_NAME="${1:-robotic-assembly-kb}"
REGION="${2:-asia-southeast1}"

if [ -z "${KB_API_KEY:-}" ]; then
  echo "[ERROR] Please set KB_API_KEY first, e.g.:"
  echo "        export KB_API_KEY=\"$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')\""
  exit 1
fi

echo "Deploying ${SERVICE_NAME} to Google Cloud Run (${REGION})..."
gcloud run deploy "${SERVICE_NAME}" \
  --source . \
  --region "${REGION}" \
  --platform managed \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --min-instances 0 \
  --max-instances 3 \
  --set-env-vars "KB_API_KEY=${KB_API_KEY}"

echo ""
echo "[DONE] Verify your deployment:"
echo "  1) Health:   curl https://<YOUR-RUN-URL>/health"
echo "  2) OpenAPI:  https://<YOUR-RUN-URL>/openapi.json"
echo "  3) Remote MCP endpoint: https://<YOUR-RUN-URL>/mcp (Header: Authorization: Bearer <KB_API_KEY>)"

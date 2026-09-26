#!/usr/bin/env bash
# ==============================================================================
# Google Cloud Shell Automated Setup Script
# Zero Hardcoded Credentials: Sets up ADK environment with Application Default Credentials
# ==============================================================================
set -euo pipefail

echo "============================================================"
echo " Setting up Autonomous Content Auditor & Fact-Checking Engine"
echo "============================================================"

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-$(gcloud config get-value project 2>/dev/null)}"
REGION="${GOOGLE_CLOUD_REGION:-us-central1}"

if [ -z "${PROJECT_ID}" ]; then
    echo "ERROR: GOOGLE_CLOUD_PROJECT is not set."
    echo "Please set your project: gcloud config set project <PROJECT_ID>"
    exit 1
fi

echo "[1/4] Enabling required Google Cloud APIs..."
gcloud services enable \
    aiplatform.googleapis.com \
    --project="${PROJECT_ID}"

echo "[2/4] Initializing Python 3.11 virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "[3/4] Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[4/4] Configuring .env file..."
cat <<EOF > .env
GOOGLE_GENAI_USE_VERTEXAI=True
GOOGLE_CLOUD_PROJECT=${PROJECT_ID}
GOOGLE_CLOUD_LOCATION=${REGION}
MODEL_NAME=gemini-3.5-flash
LOG_LEVEL=INFO
EOF

echo "============================================================"
echo " Setup complete!"
echo " To launch the ADK Web Playground, run:"
echo "   source .venv/bin/activate"
echo "   adk web"
echo "============================================================"

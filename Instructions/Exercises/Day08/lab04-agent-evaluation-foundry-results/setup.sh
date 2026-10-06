#!/usr/bin/env bash
set -e
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "Setup completed. Copy .env.example to .env and fill in values."

#!/bin/bash

# This script is intended to automate the running of the Streamlit application.

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Activate the virtual environment if needed
# source venv/bin/activate

# Run the Streamlit application
streamlit run app.py
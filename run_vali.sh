# #!/bin/bash

# # Check if a key argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 Validator key is required"
  sleep 2
  exit 1
fi

# Assign the first argument to the 'key' variable
KEY=$1

# Install dependencies using Poetry
poetry install

# Activate Poetry shell and run the Python script with the provided key
poetry run python -m src.betterTherapy.cli "$KEY"

#!/bin/bash

mkdir -p /logs/verifier

# pytest is baked into the environment image (environment/Dockerfile).
pytest /tests/test_outputs.py -rA --json-ctrf /logs/verifier/ctrf.json
rc=$?

if [ $rc -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

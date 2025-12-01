#!/bin/bash
# cli command to run the agent
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -m vllm_code.cli


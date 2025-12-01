#!/bin/bash
set -e

# Create and activate a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
echo "Activating virtual environment..."
source venv/bin/activate

# Clone vLLM if it doesn't exist
if [ ! -d "vllm" ]; then
    echo "Cloning vLLM repository..."
    git clone https://github.com/vllm-project/vllm.git
fi

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Install PyTorch (MPS support)
echo "Installing PyTorch..."
pip install torch torchvision

# Install vLLM from source (This is needed for MacOS)
echo "Installing vLLM from source..."
cd vllm
export VLLM_TARGET_DEVICE=cpu
export VLLM_BUILD_WITH_CUDA=0
pip install -e .
cd .. # Go back to the original directory

echo "vLLM installation complete."
echo "To use vLLM, activate the virtual environment: source venv/bin/activate"

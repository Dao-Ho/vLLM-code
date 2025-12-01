from typing import List, Optional
from pydantic import BaseModel
from .config import settings
from .schemas.message import Message

class Agent:
    def __init__(self, model_name: str = settings.model_name):
        self.model_name = model_name
        self.history: List[Message] = []
        
        # macOS workaround for vLLM (since it's a CUDA-based library)
        import sys
        import os
        from pathlib import Path
        
        project_root = Path(__file__).parent.parent.parent
        vllm_path = project_root / "vllm"
        
        if vllm_path.exists():
            print(f"Adding local vLLM path: {vllm_path}")
            sys.path.append(str(vllm_path))
            
        print(f"Initializing Agent with model: {self.model_name}")

    def chat(self, user_input: str) -> str:
        self.history.append(Message(role="user", content=user_input))
        
        # TODO: Placeholder for actual inference/ generation

        response_content = f"Echo: {user_input}"
        
        self.history.append(Message(role="assistant", content=response_content))
        return response_content

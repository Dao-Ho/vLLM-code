from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = Field(default="facebook/opt-125m", description="Name or path of the vLLM model to use")
    max_tokens: int = Field(default=1024, description="Maximum number of tokens to generate")
    temperature: float = Field(default=0.7, description="Sampling temperature")

    class Config:
        env_prefix = "VLLM_CODE_"

settings = Settings()

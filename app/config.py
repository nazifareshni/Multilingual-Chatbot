# app/config.py
from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # App Configuration
    app_name: str = "Multilingual RAG System"
    app_version: str = "1.0.0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database Configuration
    mongodb_url: str = "mongodb://localhost:27017/"
    database_name: str = "multilingual_rag"
    
    # OpenAI Configuration
    openai_api_key: str
    
    # Embedding Configuration
    embedding_model: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    chunk_size: int = 500
    chunk_overlap: int = 100
    
    # Vector Search Configuration
    top_k_results: int = 5
    similarity_threshold: float = 0.7
    
    # LLM Configuration
    llm_model: str = "gpt-3.5-turbo"
    llm_temperature: float = 0.3
    llm_max_tokens: int = 300
    
    # Logging Configuration
    log_level: str = "INFO"
    log_file: str = "logs/app.log"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()
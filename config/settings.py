from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    TAVILY_API_KEY: str
    RESEND_API_KEY: str = ""
    DATABASE_URL: str = "postgresql+psycopg2://postgres:password@localhost:5432/lead_agent_db"
    REDIS_URL: str = "redis://localhost:6379/0"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

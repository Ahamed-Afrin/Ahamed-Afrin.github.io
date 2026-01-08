from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pathlib import Path

# Get the backend directory path (parent of app directory)
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    """Application configuration settings"""
    
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='ignore'
    )
    
    # Database Configuration
    DATABASE_URL: str = Field(
        default="mysql+pymysql://root:root@localhost:3306/taskapp_db",
        description="Database connection URL"
    )
    
    # JWT Configuration
    SECRET_KEY: str = Field(
        default="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
        description="Secret key for JWT token generation"
    )
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=1440, description="Token expiry time in minutes")
    
    # API Configuration
    API_PREFIX: str = Field(default="/api/v1", description="API route prefix")
    DEBUG: bool = Field(default=True, description="Debug mode")
    
    # CORS Configuration
    ALLOWED_ORIGINS: str = Field(
        default="http://localhost:3000,http://localhost:5173",
        description="Comma-separated list of allowed origins"
    )
    
    @property
    def cors_origins(self) -> List[str]:
        """Parse CORS origins from comma-separated string"""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]

# Initialize settings
try:
    settings = Settings()
    env_file_path = BASE_DIR / '.env'
    
    if env_file_path.exists():
        print(f"✅ Configuration loaded from: {env_file_path}")
    else:
        print(f"⚠️  Warning: .env file not found at: {env_file_path}")
        print(f"⚠️  Using default configuration values")
    
    # Display current configuration (without sensitive data)
    print(f"\n📋 Current Configuration:")
    print(f"   Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'Not configured'}")
    print(f"   API Prefix: {settings.API_PREFIX}")
    print(f"   Debug Mode: {settings.DEBUG}")
    print(f"   Token Expiry: {settings.ACCESS_TOKEN_EXPIRE_MINUTES} minutes")
    print(f"   CORS Origins: {', '.join(settings.cors_origins)}")
    print()
    
except Exception as e:
    print(f"\n{'='*60}")
    print(f"❌ ERROR: Failed to load configuration!")
    print(f"{'='*60}")
    print(f"Expected .env location: {BASE_DIR / '.env'}")
    print(f"\nError details: {e}")
    print(f"{'='*60}\n")
    raise
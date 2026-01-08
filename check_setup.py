"""
Diagnostic script to check backend setup
Run: python check_setup.py
"""
import os
import sys
from pathlib import Path

print("="*60)
print("Backend Setup Diagnostic")
print("="*60)

# Check current directory
current_dir = Path.cwd()
print(f"\n1. Current Directory: {current_dir}")

# Check for app directory
app_dir = current_dir / "app"
print(f"\n2. App Directory Exists: {app_dir.exists()}")
if app_dir.exists():
    print(f"   Files in app/:")
    for file in app_dir.iterdir():
        print(f"   - {file.name}")

# Check for .env file
env_file = current_dir / ".env"
print(f"\n3. .env File Exists: {env_file.exists()}")
print(f"   Expected location: {env_file}")

if env_file.exists():
    print(f"\n4. .env File Contents:")
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                # Hide password in DATABASE_URL
                if 'DATABASE_URL' in line and '@' in line:
                    parts = line.split('@')
                    user_part = parts[0].split(':')
                    if len(user_part) > 2:
                        user_part[2] = '****'
                    print(f"   {':'.join(user_part)}@{parts[1]}")
                # Hide SECRET_KEY value
                elif 'SECRET_KEY' in line:
                    print(f"   SECRET_KEY=****")
                else:
                    print(f"   {line}")
else:
    print(f"\n4. Creating .env file...")
    env_content = """DATABASE_URL=mysql+pymysql://root:root@localhost:3306/taskapp_db
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
API_PREFIX=/api/v1
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
"""
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    print(f"   ✅ Created .env file at: {env_file}")
    print(f"   ⚠️  Remember to update MySQL password in .env!")

# Check Python version
print(f"\n5. Python Version: {sys.version}")

# Try to import required packages
print(f"\n6. Checking Required Packages:")
required_packages = [
    'fastapi',
    'uvicorn',
    'sqlalchemy',
    'pymysql',
    'pydantic',
    'pydantic_settings',
    'python_jose',
    'passlib',
    'python_dotenv'
]

for package in required_packages:
    try:
        __import__(package)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - NOT INSTALLED")

# Try to load settings
print(f"\n7. Testing Configuration Load:")
try:
    sys.path.insert(0, str(current_dir))
    from app.config import settings
    print(f"   ✅ Configuration loaded successfully")
    print(f"   Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else settings.DATABASE_URL}")
    print(f"   Debug: {settings.DEBUG}")
except Exception as e:
    print(f"   ❌ Failed to load configuration")
    print(f"   Error: {e}")

print("\n" + "="*60)
print("Diagnostic Complete!")
print("="*60)
print("\nNext Steps:")
print("1. Update MySQL password in .env file")
print("2. Create database: CREATE DATABASE taskapp_db;")
print("3. Run server: uvicorn app.main:app --reload")
print("="*60 + "\n")
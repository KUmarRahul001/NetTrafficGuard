@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Define the project directory
SET "PROJECT_DIR=Email_Monitoring_System"

REM Create the main project directory
mkdir "%PROJECT_DIR%"

REM Create subdirectories
mkdir "%PROJECT_DIR%\Flask_app\app.py"
mkdir "%PROJECT_DIR%\Flask_app\models"
mkdir "%PROJECT_DIR%\Flask_app\routers"
mkdir "%PROJECT_DIR%\Flask_app\static"
mkdir "%PROJECT_DIR%\Flask_app\templates"
mkdir "%PROJECT_DIR%\Flask_app\config"

mkdir "%PROJECT_DIR%\MongoDB\setup"
mkdir "%PROJECT_DIR%\MongoDB\migrations"

mkdir "%PROJECT_DIR%\datasets\raw"
mkdir "%PROJECT_DIR%\datasets\processed"

mkdir "%PROJECT_DIR%\notebooks"
mkdir "%PROJECT_DIR%\scripts"

mkdir "%PROJECT_DIR%\Docker"
mkdir "%PROJECT_DIR%\docs"

REM Create placeholder files
echo # Email Monitoring System > "%PROJECT_DIR%\README.md"
echo # Technical Documentation > "%PROJECT_DIR%\docs\technical_documentation.md"
echo # Project Report > "%PROJECT_DIR%\docs\project_report.md"
echo # User Guide > "%PROJECT_DIR%\docs\user_guide.md"

echo # Flask Application Entry Point > "%PROJECT_DIR%\Flask_app\app.py"
echo # Email Model > "%PROJECT_DIR%\Flask_app\models\email_model.py"
echo # NLP Model > "%PROJECT_DIR%\Flask_app\models\nlp_model.py"
echo # Utilities > "%PROJECT_DIR%\Flask_app\models\utils.py"
echo # Email Routes > "%PROJECT_DIR%\Flask_app\routers\email_routes.py"
echo # Configuration > "%PROJECT_DIR%\Flask_app\config\config.py"

echo # Dockerfile > "%PROJECT_DIR%\Docker\Dockerfile"
echo # Docker Compose Configuration > "%PROJECT_DIR%\Docker\docker-compose.yml"

echo # Data Preprocessing Script > "%PROJECT_DIR%\scripts\data_preprocessing.py"
echo # Feature Engineering Script > "%PROJECT_DIR%\scripts\feature_engineering.py"
echo # Model Training Script > "%PROJECT_DIR%\scripts\model_training.py"

echo # EDA Notebook > "%PROJECT_DIR%\notebooks\EDA.ipynb"
echo # Model Development Notebook > "%PROJECT_DIR%\notebooks\Model_Development.ipynb"

echo Project structure created successfully.
pause

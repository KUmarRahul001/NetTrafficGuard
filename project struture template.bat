@echo off
REM Create project directory
mkdir Email_Monitoring_System

REM Create backend directory and its subdirectories
mkdir Email_Monitoring_System\backend
mkdir Email_Monitoring_System\backend\routes
mkdir Email_Monitoring_System\backend\models
mkdir Email_Monitoring_System\backend\static
mkdir Email_Monitoring_System\backend\static\css
mkdir Email_Monitoring_System\backend\static\js
mkdir Email_Monitoring_System\backend\static\images
mkdir Email_Monitoring_System\backend\templates
mkdir Email_Monitoring_System\backend\monitoring

REM Create database directory
mkdir Email_Monitoring_System\database

REM Create frontend directory and its subdirectories
mkdir Email_Monitoring_System\frontend
mkdir Email_Monitoring_System\frontend\static
mkdir Email_Monitoring_System\frontend\static\css
mkdir Email_Monitoring_System\frontend\static\js
mkdir Email_Monitoring_System\frontend\static\images

REM Create notebooks directory
mkdir Email_Monitoring_System\notebooks

REM Create datasets directory
mkdir Email_Monitoring_System\datasets
mkdir Email_Monitoring_System\datasets\raw
mkdir Email_Monitoring_System\datasets\processed

REM Create design directory and its subdirectories
mkdir Email_Monitoring_System\design
mkdir Email_Monitoring_System\design\wireframes

REM Create scripts directory
mkdir Email_Monitoring_System\scripts

REM Create placeholder files
echo # Main Flask application > Email_Monitoring_System\backend\app.py
echo # Configuration settings >> Email_Monitoring_System\backend\config.py
echo # Initializes routes module >> Email_Monitoring_System\backend\routes\__init__.py
echo # Routes for handling email submissions and analysis >> Email_Monitoring_System\backend\routes\email_routes.py
echo # Routes for user authentication >> Email_Monitoring_System\backend\routes\auth_routes.py
echo # Initializes models module >> Email_Monitoring_System\backend\models\__init__.py
echo # Machine learning model for email analysis >> Email_Monitoring_System\backend\models\email_model.py
echo # NLP model for text analysis >> Email_Monitoring_System\backend\models\nlp_model.py
echo # Utility functions >> Email_Monitoring_System\backend\models\utils.py
echo # Script for real-time email monitoring >> Email_Monitoring_System\backend\monitoring\real_time_monitor.py
echo # Dockerfile for containerizing the Flask application >> Email_Monitoring_System\backend\Dockerfile
echo # Python dependencies for the backend >> Email_Monitoring_System\backend\requirements.txt
echo # SQL script for setting up the database schema >> Email_Monitoring_System\database\schema.sql
echo # Python classes for database models >> Email_Monitoring_System\database\models.py
echo # Configuration for MongoDB >> Email_Monitoring_System\database\mongo_config.py
echo # Jupyter notebook for data preprocessing >> Email_Monitoring_System\notebooks\data_preprocessing.ipynb
echo # Jupyter notebook for feature extraction >> Email_Monitoring_System\notebooks\feature_extraction.ipynb
echo # Jupyter notebook for model training and evaluation >> Email_Monitoring_System\notebooks\model_training.ipynb
echo # Jupyter notebook for hyperparameter tuning >> Email_Monitoring_System\notebooks\tuning.ipynb
echo # Jupyter notebook for exploratory data analysis >> Email_Monitoring_System\notebooks\exploratory_analysis.ipynb
echo # Raw dataset files >> Email_Monitoring_System\datasets\raw\README.md
echo # Processed dataset files for model training >> Email_Monitoring_System\datasets\processed\README.md
echo # Data Flow Diagram (DFD) Level 3 >> Email_Monitoring_System\design\dfd_level_3.pdf
echo # Entity-Relationship (ER) Diagram >> Email_Monitoring_System\design\er_diagram.pdf
echo # UI/UX Design documentation >> Email_Monitoring_System\design\ui_ux_design.pdf
echo # Wireframes and mockups >> Email_Monitoring_System\design\wireframes\README.md
echo # Data cleaning and preprocessing >> Email_Monitoring_System\scripts\data_preprocessing.py
echo # Feature extraction >> Email_Monitoring_System\scripts\feature_extraction.py
echo # Model training and evaluation >> Email_Monitoring_System\scripts\model_training.py
echo # Auxiliary scripts for monitoring tasks >> Email_Monitoring_System\scripts\monitoring_script.py
echo # Environment variables for configuration >> Email_Monitoring_System\.env
echo # Git ignore file >> Email_Monitoring_System\.gitignore
echo # Docker Compose file for multi-container setup >> Email_Monitoring_System\docker-compose.yml
echo # Project overview and instructions >> Email_Monitoring_System\README.md

echo Project structure created successfully!
pause

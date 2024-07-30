# **Email Monitoring System**

## **Project Overview**

The Email Monitoring System is a cybersecurity solution designed to detect and prevent phishing attacks using advanced Machine Learning (ML) and Natural Language Processing (NLP) techniques. This end-to-end system includes a web application built with Flask, a MongoDB database for data storage, and sophisticated models for analyzing email content.

## **Project Structure**

Here’s an overview of the project structure:

```
Email_Monitoring_System/
│
├── Flask_app/
│   ├── app.py
│   ├── models/
│   │   ├── email_model.py
│   │   ├── nlp_model.py
│   │   └── utils.py
│   ├── routers/
│   │   └── email_routes.py
│   ├── static/
│   ├── templates/
│   └── config.py
│
├── MongoDB/
│   ├── setup/
│   │   └── initialize_db.py
│   └── migrations/
│
├── datasets/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA.ipynb
│   └── Model_Development.ipynb
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── model_training.py
│
├── Docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── docs/
│   ├── technical_documentation.md
│   ├── project_report.md
│   └── user_guide.md
│
└── .gitignore
```

## **Features**

- **Email Analysis**: Detect phishing attempts by analyzing email content using ML and NLP models.
- **Web Application**: Submit and analyze emails through a user-friendly Flask web app.
- **Real-Time Monitoring**: Monitor incoming emails for phishing threats.
- **Database Storage**: Store email data and analysis results in MongoDB.

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/Email_Monitoring_System.git
cd Email_Monitoring_System
```

### **2. Set Up Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Set Up MongoDB**

- Ensure MongoDB is installed and running.
- Initialize the database:

```bash
python MongoDB/setup/initialize_db.py
```

### **5. Run the Application**

```bash
python Flask_app/app.py
```

- Access the web application at `http://127.0.0.1:5000`.

## **Usage**

- **Submit Emails**: Navigate to the email submission page on the web app to submit emails for analysis.
- **View Results**: Check the results page to view the analysis and potential phishing alerts.

## **Model Training and Development**

For details on model training and development, refer to the Jupyter notebooks located in the `notebooks/` directory. The notebooks provide in-depth analysis, model selection, and evaluation processes.

## **Testing**

- **Unit Tests**: Ensure that all components are tested. Run unit tests using:

```bash
pytest
```

- **Integration Tests**: Test interactions between the Flask app, MongoDB, and models.

## **Deployment**

Deployment scripts and Docker configurations are located in the `Docker/` directory. Build and run the Docker containers using:

```bash
docker-compose up --build
```

## **Documentation**

- **Technical Documentation**: Detailed documentation on code, architecture, and design is available in the `docs/technical_documentation.md`.
- **Project Report**: Comprehensive project report in the `docs/project_report.md`.
- **User Guide**: Instructions for end-users are available in the `docs/user_guide.md`.

## **Contributing**

Contributions are welcome! Please follow the standard pull request process and ensure all code adheres to the project's style guidelines.

## **License**

This project is licensed under the [MIT License](LICENSE).

## **Contact**

For any questions or issues, please contact [Your Name](mailto:your.kumarrahulraj468@gmail.com).

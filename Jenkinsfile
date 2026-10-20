pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/unnatichavan/student-management-devops.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m unittest test_app.py'
            }
        }
        stage('Docker Build') {
            steps {
                bat 'docker build -t student-app .'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker compose up -d'
            }
        }
    }
}
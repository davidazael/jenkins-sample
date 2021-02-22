pipeline {
    agent {
        docker {
            image 'python:3.7-slim-stretch'
        }
    }
    stages {
        
        stage ('SetUp Env') {
            echo 'Setting up Python VENV...'
            sh 'python3 -m venv env'
            sh '. env/bin/activate'
            sh 'pip install -r requirements.txt'
        }
        
        stage ('build') {
            steps {
                echo 'building the app...'
                sh 'python3 main.py'
            }
        }
        stage ('test') {
            steps {
                echo 'testing the app...'
                sh 'pytest -v'
            }
        }
    }
}
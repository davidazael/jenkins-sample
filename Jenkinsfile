pipeline {
    agent any

    stages {
        stage ('build') {
            agent {
                docker {
                    image 'python:3.7-slim-stretch'
                }
            }
            steps {
                echo 'building the app...'
                sh 'python3 -m py_compile main.py'
            }
            
        }
    }
}

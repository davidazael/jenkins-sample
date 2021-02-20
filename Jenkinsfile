pipeline {

  agent any 

  stages {
    stage('build') {
      steps { 
        echo 'building the application...'
        }
      }
   stage('test') {
      steps { 
        echo 'testing application...'

        withPythonEnv('python') {
            sh 'pip -U install pytest'
            sh 'pytest -v'
          }
        }
      }
  stage('deploy') {
        steps { 
        echo 'deploying the application'
          }
      }
    }
  }

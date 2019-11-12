pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'echo \'Aqui se ejecutara el build\''
          }
        }
        stage('Prueba-build') {
          steps {
            sh 'source /home/ubuntu/environments/prueva_env/bin/activate'
            sh 'pip3 freeze'
            sh 'deactivate'
          }
        }
      }
    }
    stage('Pruebas Unitarias') {
      steps {
        sh '''echo \'Aqui se ejecutaran las pruebas unitarias\'
'''
        sh '''echo $JAVA_HOME
'''
        sh 'which java'
      }
    }
    stage('Pruebas estaticas SonarQube') {
      environment {
        scannerHome = 'SonarQubeScanner'
      }
      steps {
        sh 'echo \'Aqui las pruebas estaticas\''
        withSonarQubeEnv('sonarqube') {
          sh 'echo $scannerHome'
          sh 'echo $JAVA_HOME'
        }

      }
    }
    stage('Pruebas de Integracion') {
      steps {
        sh 'echo \'Aqui se ejecutan las pruebas de integracion\''
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo \'Aqui se hace el deploy\''
      }
    }
    stage('Fin') {
      steps {
        echo 'Se ha terminado el proceso'
      }
    }
  }
}
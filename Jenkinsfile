pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'echo \'Aqui se ejecutara el build\''
      }
    }
    stage('Pruebas Unitarias') {
      steps {
        sh 'echo \'Aqui se ejecutaran las pruebas unitarias\''
      }
    }
    stage('Pruebas estaticas SonarQube') {
      environment {
        scannerHome = 'SonarQubeScanner'
      }
      steps {
        sh 'echo \'Aqui las pruebas estaticas\''
        withSonarQubeEnv(installationName: 'sonarqube', credentialsId: 'token de sonarqube')
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
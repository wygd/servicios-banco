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
          sh '''${scannerHome}/bin/sonar-scanner \\
  -Dsonar.projectKey=backend-banco \\
  -Dsonar.sources=. \\
  -Dsonar.host.url=http://ec2-34-238-247-40.compute-1.amazonaws.com:9000 \\
  -Dsonar.login=ac5d9adacd41a23b7a3f45ae4ceed6fbfbb5f43c'''
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
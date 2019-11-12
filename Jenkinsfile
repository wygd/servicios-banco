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
echo $JAVA_HOME
echo which java'''
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
  -Dsonar.login=74e4835b2a5ce4de6e425d0b9226b5055f1ac1d0'''
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
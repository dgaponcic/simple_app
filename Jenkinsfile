pipeline {
    agent any 

    stages {
        stage('Build Assets') {
            agent any 
            steps {
                sh 'docker ps'
            }
        }
        stage('Test') {
            agent any
            steps {
                echo 'Testing stuff...'
            }
        }
    }
}
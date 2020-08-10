pipeline {
    agent any 

    stages {
        stage('Build Assets') {
            agent any 
            steps {
                sh 'docker build . -t my_app'
            }
        }
        stage('Test') {
            agent any
            steps {
                sh 'docker images'
                echo 'Testing stuff...'
            }
        }
    }
}
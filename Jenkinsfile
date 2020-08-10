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
                sh 'docker run -d --name app -p 5000:5000 my_app '
                sh 'pytest test_flask.py'
            }
        }
    }

    post {
        always {
            sh 'docker stop app'
        }
    }
}
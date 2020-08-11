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
                sh 'docker run -d --name app my_app'
                sh 'docker exec app pytest test_flask.py'
            }
        }
    }

    post {
        always {
            sh 'docker stop app'
            sh 'docker rm app'
        }

        success {
            sh 'echo Yeah!'
            sh 'docker tag my_app registry.heroku.com/shielded-atoll-44823/web'
            sh 'docker push registry.heroku.com/shielded-atoll-44823/web'
            sh 'heroku container:release web --app=shielded-atoll-44823'
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'sudo docker build -t weather-app .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to docker hub....'
                sh 'sudo docker push 285484/weather-app'
            }
        }
        stage('Running') {
            steps {
                echo 'Starting service....'
                sh 'sudo docker run --rm --name weather-app -p 8080:8080 --env API_KEY_WEATHER=<your_key> -d weather-app'
            }
        }
    }
}
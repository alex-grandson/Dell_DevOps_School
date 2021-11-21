pipeline {
    agent any
    triggers { pollSCM('H */4 * * 1-3') }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'export GIT_COMMIT=$(git log -1 --format=%h)'
                sh 'docker build -t 285484/weather-app:dev-$GIT_COMMIT .'
            }
        }
        stage('Docker Login') {
            steps {
                echo 'Login..'
                withCredentials([usernamePassword(credentialsId: 'dockerhub_285484', usernameVariable: 'USERNAME_DOCKER', passwordVariable: 'PASSWORD_DOCKER')]) {

                    sh """
                    docker login -u $USERNAME_DOCKER -p $PASSWORD_DOCKER
                    """
                }
            }
        }
        stage('Publish') {
            steps {
                echo 'Deploying to docker hub....'
                sh 'docker push 285484/weather-app:$GIT_COMMIT'

            }
        }
    }
}
pipeline {
    agent any
    triggers { pollSCM('H */4 * * 1-3') }
    stages {
        stage('Build') {
            steps {
                sh 'export GIT_COMMIT=$(git log -1 --format=%h)'
                sh 'docker build -t 285484/weather-app:dev-$GIT_COMMIT .'
            }
        }
        stage('Publish') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME_DOCKER', passwordVariable: 'PASSWORD_DOCKER')]) {
                    sh """
                    docker login -u $USERNAME_DOCKER -p $PASSWORD_DOCKER
                    """
                    sh 'docker push 285484/weather-app:dev-$GIT_COMMIT'
                }
            }
        }

    }
}
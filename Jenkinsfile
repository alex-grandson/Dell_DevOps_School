pipeline {
    agent any
    triggers { pollSCM('H */4 * * 1-3') }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'export GIT_COMMIT=$(git log -1 --format=%h)'
                sh 'docker build -t 285484/weather-app:master-$GIT_COMMIT .'
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
        stage('Deploy') {
            steps {
                echo 'Deploying to docker hub....'
                sh 'docker push 285484/weather-app'

            }
        }
        stage('Apply Kubernetes files') {
            withKubeConfig([credentialsId: 'root', serverUrl: 'http://94.26.239.74']) {
              sh 'kubectl apply -f manifests'
            }
        }
//         stage('Running') {
//             steps {
//                 echo 'Starting service....'
//                 sh 'docker run --rm --name weather-app -p 8080:8080 --env API_KEY_WEATHER=<your_key> -d weather-app'
//             }
//         }
    }
}
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yashdalal45/ml'
        DOCKER_TAG = 'latest' // Change this as needed
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        // stage('Push to Docker Hub') {
        //     steps {
        //         echo 'Pushing Docker image to Docker Hub...'
        //         script {
        //             withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
        //                 sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
        //             }
        //         }
        //     }
        // }
    }

    post {
        success {
            echo 'Build successful!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}

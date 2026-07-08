pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'localhost:5000'
        IMAGE_NAME = 'python-demo'
        IMAGE_TAG = 'v1'
        DOCKER_IMAGE = "${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
        GIT_REPO = 'https://github.com/agawand007/arg.git'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Clone') {
            steps {
                script {
                    echo '========== Stage: Clone =========='
                    echo "Cloning repository from ${GIT_REPO}"
                }
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: "${GIT_REPO}"]]
                ])
                script {
                    echo '✓ Repository cloned successfully'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo '========== Stage: Build =========='
                    echo "Building Docker image: ${DOCKER_IMAGE}"
                    sh '''
                        docker build -t ${DOCKER_IMAGE} .
                        echo "✓ Docker image built successfully"
                        docker images | grep ${IMAGE_NAME}
                    '''
                }
            }
        }

        stage('Push') {
            steps {
                script {
                    echo '========== Stage: Push =========='
                    echo "Pushing Docker image to registry: ${DOCKER_REGISTRY}"
                    sh '''
                        docker push ${DOCKER_IMAGE}
                        echo "✓ Docker image pushed successfully to ${DOCKER_REGISTRY}"
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✓ Pipeline completed successfully!'
            echo "Image ${DOCKER_IMAGE} is ready in the Docker registry"
        }
        failure {
            echo '✗ Pipeline failed!'
            echo 'Check the logs above for details'
        }
        always {
            echo 'Pipeline execution finished'
        }
    }
}

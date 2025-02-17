// Jenkinsfile
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/feature/cicd']],
                        userRemoteConfigs: [[
                            url: 'https://github.com/olaoluthomas/jenkins-test',
                            credentialsId: 'github-pat-for-jenkins'
                        ]]
                    ])
                }
            }
        }
        
        stage('Setup Python') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest --cov=app tests/test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-jenkins-demo .'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
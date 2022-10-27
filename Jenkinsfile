pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building....'
            }
        }
        stage('Tests') {
            steps {
                sh 'py.test main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
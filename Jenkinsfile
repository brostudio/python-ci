pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python main.py'
            }
        }
        stage('Tests') {
            steps {
                bat 'py.test main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
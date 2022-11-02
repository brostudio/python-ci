pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build stage...'
            }
        }
        stage('Tests') {
            steps {
                bat 'py.test main.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
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
                sh 'py.test main.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -v'
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
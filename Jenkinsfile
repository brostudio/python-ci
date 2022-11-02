pipeline {
    agent any

    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32"
    }
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
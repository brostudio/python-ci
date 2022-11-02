pipeline {
    agent any

    environment {
        PATH = "C:\\WINDOWS\\SYSTEM32"
    }
    stages {
        stage('Build') {
            steps {
                powershell 'python -v'
            }
        }
        stage('Tests') {
            steps {
                powershell 'py.test main.py'
            }
        }
        stage('Deploy') {
            steps {
                powershell 'python main.py'
            }
        }
    }
}
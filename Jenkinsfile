pipeline {
    agent any

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
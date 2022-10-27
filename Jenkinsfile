pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python main.py'
            }
        }
        stage('Tests') {
            steps {
                sh 'py.test main.py'
            }
        }
    }
}
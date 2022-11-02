pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat "C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -v"
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
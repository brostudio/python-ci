pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building..."
                bat "C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -v"
            }
        }
        stage('Tests') {
            steps {
                bat 'C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\py.test.exe main.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'C:\\Users\\Student\\AppData\\Local\\Programs\\Python\\Python310\\python.exe main.py'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '49b7fc15-6f88-43b2-99df-3a8826c42b0b', url: 'https://github.com/Jibin173/demo_datascience1.git']]])
            }

        }
        stage('Test'){
            steps {
               git credentialsId: '49b7fc15-6f88-43b2-99df-3a8826c42b0b', url: 'https://github.com/Jibin173/demo_datascience1.git'
               sh 'pytest -s -v -m "regression" --html=./Reports/report.html testcases/ --browser chrome'
            }
        }
    }
}

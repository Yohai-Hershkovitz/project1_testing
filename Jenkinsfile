pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                echo 'running test_myFirstTest.py'
                bat 'pytest test_myFirstTest.py'  //pytest engaged
            }
        }
    }
}

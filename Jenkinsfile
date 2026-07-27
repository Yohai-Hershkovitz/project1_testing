pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                echo 'running test_myFirstTest.py'
                bat 'pytest project1_testing/test_myFirstTest.py'  //pytest engaged
            }
        }
    }
}

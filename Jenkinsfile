pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm //Jenkins job chooses repo
            }
        }

        stage('Testing') {//assume pytest installed in env
            steps {
                echo 'running test_myFirstTest.py'
                bat '''
                    python -m pytest project1_testing/test_myFirstTest.py
                '''  //pytest engaged
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        failure {
            echo 'A pipeline stage failed'
        }
    }
}

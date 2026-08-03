pipeline {
    agent any

    parameters{
        choice(
            name: 'modelChoice',
            choices: ['all', 'model1', 'model2'],
            description: 'Select which model to test'
        )
    }

    environment {
        modelChoice = "${params.modelChoice}"
    }

    stages { //checkout is automatic
        stage('Testing') {//assume pytest installed in env
            steps {
                echo 'running test_myFirstTest.py'
                bat '''
                    python -m pytest project1_testing/test_myFirstTest.py --modelChoice %modelChoice%
                '''  //pytest engaged
            }
        }
    }

    post {
        failure {
            echo 'A pipeline stage failed'
        }
    }
}

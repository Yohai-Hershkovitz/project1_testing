pipeline {
    agent any

    parameters{
        choice(
            name: 'modelChoice',
            choices: ['all', 'model1', 'model2'],
            description: 'Select which model to test'
        )
        booleanParam(
            name: 'REFRESH_PARAMETERS',
            defaultValue: false,
            description: 'Check this to reload the Jenkinsfile without running the build.'
        )
    }

    environment {
        modelChoice = "${params.modelChoice}"
    }

    stages {
        stage('Only Refresh Jenkinsfile') {
            when {
                expression { params.REFRESH_PARAMETERS }
            }
            steps {
                script {
                    currentBuild.description = 'Configuration Refreshed'
                }
            }
        }

        // --- PARENT STAGE ---
        stage('Deployment Pipeline') {
            // This condition applies to ALL stages nested inside this block
            when {
                expression { !params.REFRESH_PARAMETERS }
            }
            
            // Note the nested 'stages' block here
            stages {
                //checkout stage is integrated automatically
                stage('Testing') {//assumes pytest installed in env
                    steps {
                        echo 'running test_myFirstTest.py'
                        bat '''
                            python -m pytest project1_testing/test_myFirstTest.py --modelChoice %modelChoice%
                        '''  //pytest engaged
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'A pipeline stage failed'
        }
    }
}

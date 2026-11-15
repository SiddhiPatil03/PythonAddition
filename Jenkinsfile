
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting Python Addition UAT Project'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v --junitxml=reports/pytest-results.xml'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                bat 'python -m monitoring.evidently_report'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'reports/pytest-results.xml'

            archiveArtifacts artifacts: 'reports/*',
                             allowEmptyArchive: true
        }

        success {
            echo 'UAT Pipeline Completed Successfully!'
        }

        failure {
            echo 'UAT Pipeline Failed!'
        }
    }
}

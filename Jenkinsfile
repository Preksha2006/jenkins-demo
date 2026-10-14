pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                bat 'echo Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the project...'
                bat 'echo All tests passed'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
                bat 'echo Deployment completed successfully'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }
    }
}

pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ishaanghosh2002/MLC-Mid-Term.git'
            }
        }
        
        stage('Run Existing Docker Image') {
            steps {
                // Run the existing Docker image 'speech_recognition_app'
                script {
                    docker.image('speech_recognition_app').inside {
                        // Execute the Jupyter notebook and convert it to a desired format
                        sh 'jupyter nbconvert --execute --to notebook --inplace speech_processing_app.ipynb'
                    }
                }
            }
        }
    }
}

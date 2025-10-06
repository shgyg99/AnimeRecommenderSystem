pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage("Cloning from Github..."){
            steps{
                script{
                    echo 'Cloning from Github...'
                    sh '''
                    git lfs install
                    '''
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shgyg99/AnimeRecommenderSystem.git']])
                    sh '''
                    git lfs pull
                    '''
                }
            }
        }
    }
    stages{
        stage("Making a virtual environment..."){
            steps{
                script{
                    echo 'Making a virtual environment...'
                    sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
    
}
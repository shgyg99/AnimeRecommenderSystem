pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage("Cloning from Github") {
            steps {
                script {
                    echo 'Cloning from Github...'
                    checkout([$class: 'GitSCM',
                        branches: [[name: '*/main']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shgyg99/AnimeRecommenderSystem.git']]
                    ])

                    echo 'Pulling LFS files...'
                    sh 'git lfs pull'
                }
            }
        }

        stage("Making a virtual environment") {
            steps {
                script {
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

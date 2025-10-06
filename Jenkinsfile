pipeline {
    agent any

    stages {
        stage("Cloning from Github...") {
            steps {
                script {
                    echo 'Cloning from Github...'

                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'GitLFSPull']  // ← این خط مهمه
                        ],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/shgyg99/AnimeRecommenderSystem.git'
                        ]]
                    ])
                }
            }
        }
    }
}

pipeline{
    agent any
    environment {
        KUBECONFIG = 'C:\\ProgramData\\Jenkins\\.kube\\config'
        CHCP = '65001'
    }
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Checkout'){
            steps {
                git branch:'main', url:'https://github.com/Aliminium-11929/CRUD'
            }
        }
        stage('Build in Minikube Docker') {
            steps {
                bat """
                REM === Switch Docker to Minikube Docker ===
                call minikube -p minikube docker-env --shell=cmd > docker_env.bat
                call docker_env.bat

                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                """
            }
        }
        stage('Deploy to Minikube'){
            steps{
                bat """
                echo === Applying Kubernetes Deployment ===
                kubectl apply -f deployment.yaml --validate=false

                echo === Applying Service ===
                kubectl apply -f service.yaml --validate=false

                echo === Waiting for Rollout Completion ===
                kubectl rollout status deployment/django-deployment --timeout=90s
                """
            }
        }
    }
    post {
        success {
            echo "✅ Deployment successful!"
        }
        failure {
            echo "❌ Deployment failed — check Minikube or kubeconfig path."
        }
    }
}
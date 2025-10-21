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
                @FOR /F "tokens=*" %%i IN ('minikube -p minikube docker-env --shell=cmd') DO %%i

                REM === Build Django image inside Minikube Docker ===
                docker build -t mydjangoapp:latest .
                """
            }
        }
        stage('Deploy to Minikube'){
            steps{
                bat """
                kubectl apply -f deployment.yaml --validate=false
                kubectl apply -f service.yaml --validate=false
                kubectl rollout restart deployment/django-deployment
                kubectl rollout status deployment/django-deployment --timeout=180s
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
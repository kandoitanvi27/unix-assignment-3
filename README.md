# Todo App - Flask + PostgreSQL

A simple two-tier web application built with Flask (web frontend/API) and PostgreSQL (database).

## Features
- Create, read, update, and delete todo items
- Mark todos as complete/incomplete
- Clean and responsive UI

## Tech Stack
- **Frontend/API**: Flask (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Kubernetes (Minikube)

## Project Structure
```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
├── static/                # CSS styles
├── Dockerfile             # Multi-stage Docker build
├── docker-compose.yml     # Docker Compose config
└── k8s/                   # Kubernetes manifests
    ├── app-deployment.yaml
    ├── app-service.yaml
    ├── db-deployment.yaml
    └── db-service.yaml
```

## Running with Docker Compose

```bash
docker-compose up --build
```

Open http://localhost:5000 in your browser.

## Running with Kubernetes (Minikube)

```bash
# Start Minikube
minikube start

# Build the Docker image inside Minikube
eval $(minikube docker-env)
docker build -t todo-app:latest .

# Apply Kubernetes manifests
kubectl apply -f k8s/

# Wait for pods to be ready
kubectl get pods

# Access the app
minikube service todo-app
```

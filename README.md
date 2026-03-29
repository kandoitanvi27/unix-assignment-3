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

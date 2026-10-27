# 🚀 DeployX — Automated Deployment Platform

**A FastAPI application with Docker containerization and GitHub Actions CI/CD automation.**

DeployX is a Python-based project that demonstrates API health monitoring, automated testing, Docker image building, and publishing container images to Docker Hub through GitHub Actions.

## ✨ Features

- FastAPI REST API
- Root endpoint and health-check endpoint
- UTC timestamp in health responses
- Interactive Swagger API documentation
- Automated API testing with Pytest
- Docker containerization
- GitHub Actions CI pipeline
- Automated Docker image build and publishing on pushes to `main`

## 🛠️ Tech Stack

- **Language:** Python 3.14
- **API Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Testing:** Pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Container Registry:** Docker Hub

## 📂 Project Structure

```text
deployx/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .venv/                 # Local virtual environment
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

> `.venv/` is a local development environment and should not be committed to Git.

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message and useful endpoint paths |
| GET | `/health` | Returns the service status and current UTC timestamp |
| GET | `/docs` | Interactive Swagger API documentation |

### Example health response

```json
{
  "status": "ok",
  "service": "deployx",
  "timestamp": "2026-10-27T07:00:00+00:00"
}
```

The timestamp is an example; the API generates the current UTC timestamp for each request.

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rukeshkumar914/deployx.git
cd deployx
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Start the API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open these URLs in your browser:

- API: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Swagger documentation: http://127.0.0.1:8000/docs

Stop the server with `Ctrl + C`.

## 🧪 Run Tests

Activate `.venv` first, then execute:

```bash
python -m pytest -v
```

The tests verify the root endpoint and health-check endpoint, including expected responses and HTTP status codes.

## 🐳 Docker

### Build the Docker image

```bash
docker build -t deployx:1.0 .
```

### Run the container

```bash
docker run --rm -p 8000:8000 deployx:1.0
```

Verify the application at http://127.0.0.1:8000/health.

## 🔄 CI/CD Pipeline

DeployX uses GitHub Actions to automate testing and Docker image publishing.

### Workflow

1. A push or pull request targeting `main` triggers the test job.
2. GitHub Actions sets up Python 3.14 and installs project dependencies.
3. Pytest runs the automated test suite.
4. On a push to `main`, the Docker job runs after the test job succeeds.
5. The workflow builds the Docker image and pushes it to Docker Hub.

### Required GitHub Secrets

Configure these repository secrets for Docker Hub publishing:

- `DOCKERHUB_USERNAME` — Docker Hub username.
- `DOCKERHUB_TOKEN` — Docker Hub access token.

Never commit passwords, tokens, or other credentials to the repository.

## 📦 Docker Hub Image

The workflow is configured to publish:

```text
rukesh91/deployx:1.0
```

After the image has been successfully published, run:

```bash
docker pull rukesh91/deployx:1.0
docker run --rm -p 8000:8000 rukesh91/deployx:1.0
```

## 🎯 Learning Outcomes

- Building REST APIs using FastAPI
- Creating and managing Python virtual environments
- Writing automated tests with Pytest
- Packaging applications with Docker
- Automating testing through GitHub Actions
- Building and publishing Docker images
- Understanding a basic CI/CD pipeline

## 👨‍💻 Author

**Rukesh Yadav**

GitHub: [Rukeshkumar914](https://github.com/Rukeshkumar914)

**Project:** DeployX — Automated Deployment Platform

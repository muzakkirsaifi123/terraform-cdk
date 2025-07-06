# 🐳 Terraform CDK (Python): Flask + Nginx + Redis (Local Docker Deployment)

This project demonstrates how to deploy a simple containerized application stack using **Terraform CDK (CDKTF)** with **Python** and **Docker**.

### 💡 Stack Includes:
- ⚙️ **Terraform CDK (Python)** – Infrastructure as code
- 🐍 **Flask** – Python web application
- 🌐 **Nginx** – Reverse proxy for the Flask app
- 🧠 **Redis** – In-memory data store
- 🐳 **Docker** – Local container orchestration via Terraform

---

## 🚀 Quick Start

### 🔧 Prerequisites

Make sure you have the following installed:

- [Python 3.8+](https://www.python.org/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Node.js](https://nodejs.org/)
- [Terraform](https://developer.hashicorp.com/terraform)
- [Docker](https://www.docker.com/)
- CDKTF CLI:

```bash
npm install -g cdktf-cli


# 📁 Create and enter a new project folder
mkdir cdktf-docker-compose && cd cdktf-docker-compose

# 🏗️ Initialize a new CDKTF Python project with local backend
cdktf init --template=python --local

# 🐍 Start pipenv shell (Python virtual environment)
pipenv shell

# 📦 Install CDKTF Docker provider bindings
pipenv install cdktf-cdktf-provider-docker

# 🔌 Add the Docker Terraform provider (version 2.24.0)
cdktf provider add "kreuzwerker/docker@~>2.24.0"

# 🔄 OR manually update cdktf.json:
# {
#   "language": "python",
#   "app": "pipenv run python main.py",
#   "terraformProviders": [
#     "kreuzwerker/docker@~>2.24.0"
#   ],
#   "terraformModules": [],
#   "codeMakerOutput": "imports",
#   "context": {},
#   "projectId": "your-project-id"
# }

# 🔁 Generate provider bindings
cdktf get

# 🛠️ Synthesize Terraform JSON
cdktf synth

# 🚀 Deploy infrastructure (runs `terraform apply`)
cdktf deploy


.
├── cdktf.json                # CDKTF project config
├── main.py                   # CDKTF infrastructure definition in Python
├── requirements.txt          # Python dependencies
├── Pipfile / Pipfile.lock    # Pipenv environment config
├── imports/                  # Auto-generated provider bindings
├── .venv/                    # Python virtual environment (Git-ignored)
├── docker/
│   ├── flask-app/            # Flask application source
│   ├── nginx/                # Nginx configuration
│   └── Dockerfiles, assets   # Docker-related files
└── README.md
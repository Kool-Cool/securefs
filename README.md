# SecureFS - Secure File Sharing System

A secure file sharing system built with Next.js, Flask, and Kubernetes.

## Project Structure

```
securefs/
│── backend/                 # Flask API
│   ├── app.py              # Flask application
│   ├── requirements.txt     # Dependencies
│   └── Dockerfile          # Backend Docker config
│── frontend/               # Next.js UI
│   ├── pages/             # Next.js pages
│   ├── components/        # React components
│   └── Dockerfile        # Frontend Docker config
│── k8s/                   # Kubernetes manifests
└── README.md              # Documentation
```

## Development Setup

1. Backend Setup:

```bash
cd backend
pip install -r requirements.txt
python app.py
```

2. Frontend Setup:

```bash
cd frontend
npm install
npm run dev
```

## Docker Build

```bash
# Build backend
docker build -t securefs-backend ./backend

# Build frontend
docker build -t securefs-frontend ./frontend
```

## Features

- File upload/download
- Secure file storage
- Web-based interface

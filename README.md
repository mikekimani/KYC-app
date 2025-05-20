# 🔐 KYC Web Application – Full Stack (FastAPI + Next.js)

This is a secure Know Your Customer (KYC) web application that uses OCR, face recognition, and selfie verification to validate user identity. Designed for universal use, compliant with GDPR and AML/KYC regulations, and supports real-time document scanning and liveness detection.

## 🌍 Tech Stack
| Layer     | Technology                             |
|-----------|-----------------------------------------|
| Frontend  | **Next.js**, **Tailwind CSS**, **React** |
| Backend   | **FastAPI**, **Uvicorn**, **Pydantic**   |
| OCR       | **PaddleOCR** / **EasyOCR**              |
| Face Match| **DeepFace** / **face_recognition**      |
| Hosting   | **AWS** (EC2, S3, etc.)                  |
| Auth      | **JWT Authentication**                  |
| Mobile    | Camera support via HTML5 (mobile-friendly) |


## 📁 Monorepo Structure
kyc-app/
├── backend/ # FastAPI server (Python)
│ ├── app/ # App logic
│ │ ├── auth/ # JWT login/register
│ │ ├── kyc/ # OCR + face match
│ │ ├── core/ # Configs & schemas
│ │ └── utils/ # Helper functions
│ ├── main.py # FastAPI entry point
│ └── requirements.txt
│
├── frontend/ # Next.js + Tailwind (React)
│ ├── pages/ # index.tsx, dashboard.tsx
│ ├── components/ # UI components
│ └── utils/ # Axios config
│
├── shared/ # (Optional) Shared types/configs
│ └── init.py
│
├── docker-compose.yml # Local dev (full stack)
├── .gitignore
└── README.md

## 🚀 Getting Started (Local Dev)

### 1. Prerequisites
- Docker + Docker Compose
- Git

### 2. Clone the Repo
git clone https://github.com/your-username/kyc-app.git
cd kyc-app


### 3. Run Locally with Docker
docker-compose up --build
Backend runs on: http://localhost:8000
FastAPI docs: http://localhost:8000/docs
Frontend runs on: http://localhost:3000


## ✅ KYC Flow
User registers/logs in
Uploads government-issued ID (passport, driver’s license, etc.)
Uploads selfie or uses live camera

## Backend:
Extracts text using OCR
Performs face match + liveness detection
Backend returns validation result
All PII data is securely discarded after processing

## 🛡️ Compliance & Security
GDPR / AML / KYC regulation aware
Temporary PII handling (no permanent storage)
Secure user authentication (JWT)
HTTPS recommended for production

## 🧪 Testing (Manually)
Try uploading:
A passport image (JPG or PNG)
A selfie image (live capture supported on mobile)

## Check:
OCR results
Face match confidence
Liveness verification result

## 📦 Deployment
Backend (AWS EC2 or ECS):
FastAPI served via Uvicorn or Gunicorn
Store temporary uploads in /tmp or S3
Add Nginx reverse proxy (optional)

## Frontend:
Host on Vercel, AWS Amplify, or same EC2 instance
Configure NEXT_PUBLIC_API_BASE to your backend URL

## ✅ Roadmap
 Full KYC process with ID + selfie
 Dark/Light mode toggle
 Mobile camera support
 JWT secure login/register
 Email verification / OTP
 Admin dashboard (optional)
 Upload audit logs (optional)

## 🤝 Contributing
Pull requests welcome. For major changes, please open an issue first.

## 📝 License
MIT © [Mike Kimani]

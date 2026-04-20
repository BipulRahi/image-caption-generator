# 🖼️ Image Caption Generator using BLIP

A multimodal **Image Captioning project** built using **BLIP (Bootstrapping Language-Image Pretraining)** from Hugging Face.

This project supports **two modes**:

- 🖥️ **CLI Mode** → local terminal-based caption generation
- 🌐 **Web App Mode** → React frontend + FastAPI backend

The model automatically generates meaningful natural language captions from uploaded images.

---

# 🎥 Demo Video

Watch the complete project demo here:

[▶️ Click to Watch Demo Video](https://github.com/BipulRahi/image-caption-generator/blob/main/w.mp4)

### Demo Includes
- CLI image caption generation
- Frontend image upload
- Backend health check loading
- Caption generation flow
- Full deployment demo

---

# ✨ Features

- 🧠 BLIP-based image captioning
- 🖥️ Command Line Interface (CLI)
- 🌐 Full-stack web application
- ⚡ FastAPI backend API
- 🎨 React frontend UI
- 🔄 Backend health polling + loading states
- ☁️ Deployment ready (Render + Vercel)

---

# 🧠 Model Used

This project uses:

**BLIP – `Salesforce/blip-image-captioning-base`**

Hugging Face model:  
https://huggingface.co/Salesforce/blip-image-captioning-base

---

# 🔥 What is BLIP?

BLIP stands for:

**Bootstrapping Language-Image Pretraining**

It is a powerful **vision-language model** for tasks like:

- image captioning
- visual question answering
- image-text retrieval
- multimodal understanding

BLIP combines:

- image understanding using Vision Transformer
- text generation using language decoder

This allows it to produce more natural and context-aware captions.

---

# ⚙️ How It Works

```text
Input Image
   ↓
Image Preprocessing
   ↓
Vision Transformer Encoder
   ↓
Visual Embeddings
   ↓
Text Decoder
   ↓
Generated Caption
```

---

# 📁 Project Structure

```text
image-caption-generator/
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── app.py                # CLI application
├── asserts/              # sample images for CLI
├── .gitignore
└── README.md
```

---

# 🖥️ CLI Application (`app.py`)

The project also includes a **Command Line Interface (CLI)** version that allows image caption generation directly from the terminal without running the frontend or backend.

This file is present in the **root directory** of the project.

---

## 🚀 How to Run `app.py` Locally

Make sure you are in the **root directory** of the project:

```bash
cd image-caption-generator
```

---

### 1️⃣ Create Virtual Environment (Recommended)

#### Windows
```bash
python -m venv cleanenv
cleanenv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv cleanenv
source cleanenv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r backend/requirements.txt
```

> If your `requirements.txt` is in the root folder, use:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the CLI Application

```bash
python app.py
```

---

## 🖼 Example Run

```text
Enter image path: ./asserts/dog.jpg

🧠 Generating caption...
--------------------------------------------------
a dog running in a grassy field
--------------------------------------------------
```

---

## 📂 Supported Image Formats

- `.jpg`
- `.jpeg`
- `.png`

---

## 📌 Sample Input Path

Use images from the `asserts` folder:

```text
./asserts/sample.jpg
```

---

## 🔁 Exit CLI

To stop the CLI application, type:

```text
exit
```

# 🌐 Web Application

The web app consists of:

- **Frontend:** React + Vite
- **Backend:** FastAPI + BLIP

---

# ⚙️ Backend Setup

Move inside backend folder:

```bash
cd backend
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv cleanenv
cleanenv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv cleanenv
source cleanenv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

---

# 🎨 Frontend Setup

Move inside frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# 🔄 Web App Flow

```text
Frontend starts
   ↓
Health polling starts
   ↓
Backend model loading
   ↓
Ready state detected
   ↓
Image upload
   ↓
Caption generation
```

---

# ☁️ Deployment

---

## Backend → Render

Deploy `backend/` folder as **Web Service**

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Frontend → Vercel

Deploy `frontend/` folder

### Build Command

```bash
npm run build
```

### Output Directory

```text
dist
```

---

# 🛠 Tech Stack

- Python
- FastAPI
- React
- Vite
- PyTorch
- Transformers
- PIL
- BLIP
- Vision Transformer

---

# 📚 References

BLIP model:  
https://huggingface.co/Salesforce/blip-image-captioning-base

BLIP paper:  
https://arxiv.org/abs/2201.12086

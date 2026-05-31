# DriveLegal

AI-powered legal assistant for Indian traffic laws.

## Features

* Challan Fine Calculator
* Traffic Law Chatbot
* RAG over Motor Vehicles Act, 1988
* OCR-based Challan Analysis
* Automatic Location Detection

---

## Backend Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the backend directory:

```env
DATABASE_URL=YOUR_DATABASE_URL_HERE
REDIS_URL=YOUR_REDIS_URL_HERE
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

### 5. Build RAG Index

```bash
python -m app.rag.build_index
```

### 6. Run Backend

```bash
uvicorn app.main:app --reload
```

**Backend URL:**

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

**Frontend URL:**

```text
http://localhost:3000
```

---

## Environment Variables

Copy `.env.example` to `.env` and update the values:

```env
DATABASE_URL=YOUR_DATABASE_URL_HERE
REDIS_URL=YOUR_REDIS_URL_HERE
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```


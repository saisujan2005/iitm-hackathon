# DriveLegal

AI-powered legal assistant for Indian traffic laws.

## Features

* Challan Fine Calculator
* Traffic Law Chatbot
* RAG over Motor Vehicles Act, 1988
* OCR-based Challan Analysis
* Automatic Location Detection
* Offline Support with Cached Data
* Challan Fine Calculator Works Offline

---

## Offline Support

DriveLegal is designed to provide a seamless experience even when internet connectivity is unavailable.

### Offline Capabilities

* Challan Fine Calculator works completely offline using locally cached fine and violation data.
* Previously accessed legal information and frequently used resources can be stored in cache for faster access.
* Users can continue checking challan penalties and common traffic law information without an active internet connection.
* Cached data is automatically synchronized and updated when the device reconnects to the internet.

### Online-Only Features

The following features require an internet connection:

* AI-powered Traffic Law Chatbot
* OCR-based Challan Analysis (if cloud processing is enabled)
* Real-time legal updates and database synchronization
* Automatic location-based services (depending on device permissions and connectivity)

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



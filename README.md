# VroomEasy

VroomEasy is a full-stack web application using:
- **Frontend:** React + TypeScript (Vite)
- **Backend:** Python (FastAPI)
- **Database/Auth:** Supabase

---

## Project Structure

```
VroomEasy/
│
├── backend/         # Python FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend/        # React + TypeScript frontend (Vite)
│   ├── src/
│   ├── public/
│   ├── .env
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

---

## Getting Started

### 1. **Clone the repository**
```bash
git clone https://github.com/sujanedwinp/VroomEasy
cd VroomEasy
```

---

### 2. **Backend Setup (Python + FastAPI)**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
```
- Create a `.env` file in `backend/` with:
  ```
  SUPABASE_URL=your-supabase-url
  SUPABASE_ANON_KEY=your-supabase-anon-key
  ```
- Start the backend server:
  ```bash
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
  ```

---

### 3. **Frontend Setup (React + Vite)**
```bash
cd frontend
npm install
```
- Create a `.env` file in `frontend/` with:
  ```
  VITE_SUPABASE_URL=your-supabase-url
  VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
  ```
- Start the frontend dev server:
  ```bash
  npm run dev
  ```
- Visit [http://localhost:5173/](http://localhost:5173/) in your browser.

---

## .gitignore Highlights

- Ignores IDE files (`.idea/`), Python cache (`__pycache__/`), environment files (`.env`), and all frontend build, dependency, and coverage files (`node_modules/`, `build/`, `coverage/`).
- Keeps your secrets and local configs out of version control.

---

## API Endpoints

- `GET /users` — Returns all users from Supabase.
- `GET /insurers` — Returns all insurer info from Supabase.
- *(Add more as needed in `backend/main.py`)*

---

## Notes

- **Do not commit your `.env` files** — they contain sensitive keys.
- For production, configure environment variables securely on your server.



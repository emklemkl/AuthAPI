# AuthAPI

A lightweight authentication API built with Flask using JWT.

---

## 🚀 Getting Started

### 📦 Prerequisites

Make sure you have the following installed:

- Python 3.13+
- pip
- Virtualenv

---

### 🛠️ Installation

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/AuthAPI.git
   ```
   
3. **Create virtual env**
   ```
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # macOS/Linux
   ```
   
4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
## ⚙️ Configuration
1. **Set env vars in .env**
  ```
  JWT_SECRET_KEY=<your-secret>
  DATABASE_URI=sqlite+pysqlite:///auth.db
  ```

## ▶️ Running the Ap
  ```
  python -m auth_api
  ```

## Notes
  * This project uses JWT for stateless authentication
  * Future plans include refresh tokens and multi-device session tracking

## Project Structure 
```
AuthAPI/
│
├── app/
│   ├── controllers/
│   ├── custom_exceptions/
│   ├── handlers/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── __init__.py
│
├── instance/auth.db
├── requirements.txt
├── .env
├── app.py
└── README.md
```

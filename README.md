# Taller API

A REST API built with FastAPI and PostgreSQL for managing projects and tasks.

## Tasks

- [x] 1. Project structure
- [x] 2. FastAPI setup
- [ ] 3. Database setup
- [ ] 4. Models & relationships (Project, Task)
- [ ] 5. POST /projects
- [ ] 6. Finish /projects CRUD
- [ ] 7. /tasks endpoint
- [ ] 8. Add pagination, sort, and validate creation of projects
- [ ] 9. Use asynchronous
- [ ] 10. Implement simple authentication

---

## 1. Project Structure

```
main.py
requirements.txt
backend/
    __init__.py
    api.py
    db.py
    model.py
```

---

## 2. FastAPI Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## 3. Database Setup

Create the database:

```sql
CREATE DATABASE tallerapi;
```

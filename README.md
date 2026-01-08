# 🚀 Task Management Application

A full-stack web application built with **FastAPI** (Python) and **React** featuring user authentication, task management, and a modern responsive UI.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=flat&logo=react)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

##  Features

###  Authentication & Security
- User registration and login with JWT tokens
- Secure password hashing using bcrypt
- Protected API routes with middleware
- Token-based session management
- Automatic token expiry handling

###  Task Management
- Create, read, update, and delete tasks (CRUD operations)
- Task status management (Pending, In Progress, Completed)
- Search tasks by title and description
- Filter tasks by status
- User-specific task isolation

###  User Profile
- View and update profile information
- Email validation
- Account creation date tracking

###  Modern UI
- Responsive design with Tailwind CSS
- Clean and intuitive interface
- Real-time form validation
- Loading states and error handling
- Modal dialogs for task operations

##  Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **MySQL** - Relational database
- **Pydantic** - Data validation
- **python-jose** - JWT token implementation
- **passlib** - Password hashing library

### Frontend
- **React 18** - UI library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Build tool and dev server

##  Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9 or higher
- Node.js 16 or higher
- MySQL 8.0 or higher
- npm or yarn package manager

##  Quick Start

###  Clone the Repository

```bash
git clone https://github.com/yourusername/task-management-app.git
cd task-management-app
```

### 2️⃣ Backend Setup

#### Install Dependencies

```bash
cd Backend
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

#### Configure Environment Variables

Create a `.env` file in the `Backend` directory:

```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/taskapp_db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440
API_PREFIX=/api/v1
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

**🔒 Security Note:** Generate a secure secret key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

#### Create MySQL Database

```sql
CREATE DATABASE taskapp_db;
```

#### Run Backend Server

```bash
# From Backend directory
uvicorn app.main:app --reload
```

Backend will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/api/v1/docs`

### 3️⃣ Frontend Setup

#### Install Dependencies

```bash
cd Frontend
npm install
```

#### Configure Environment Variables

Create a `.env` file in the `Frontend` directory:

```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

#### Run Frontend Development Server

```bash
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## 📁 Project Structure

```
task-management-app/
├── Backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── config.py            # Configuration settings
│   │   ├── database.py          # Database connection
│   │   ├── models/              # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   ├── schemas/             # Pydantic schemas
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   ├── routes/              # API endpoints
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   └── tasks.py
│   │   ├── services/            # Business logic
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   └── task_service.py
│   │   └── middleware/          # Authentication middleware
│   │       └── auth_middleware.py
│   ├── requirements.txt
│   ├── run.py
│   └── .env
├── Frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth/            # Login & Register
│   │   │   ├── Dashboard/       # Dashboard & Profile
│   │   │   ├── Layout/          # Navbar & Protected Routes
│   │   │   └── Common/          # Reusable components
│   │   ├── services/            # API services
│   │   ├── context/             # React context (Auth)
│   │   ├── utils/               # Utility functions
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── package.json
│   └── .env
└── README.md
```

## 🔌 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user

### Users
- `GET /api/v1/users/me` - Get current user profile
- `PUT /api/v1/users/me` - Update user profile

### Tasks
- `POST /api/v1/tasks` - Create new task
- `GET /api/v1/tasks` - Get all tasks (with filters)
- `GET /api/v1/tasks/{id}` - Get specific task
- `PUT /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

### Query Parameters
- `status` - Filter by task status (pending, in_progress, completed)
- `search` - Search in title and description

## 📖 API Documentation

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api/v1/docs`
- **ReDoc**: `http://localhost:8000/api/v1/redoc`

## 🧪 Testing the Application

### Using cURL

**Register:**
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","email":"john@example.com","password":"password123"}'
```

**Login:**
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"john@example.com","password":"password123"}'
```

**Create Task:**
```bash
curl -X POST "http://localhost:8000/api/v1/tasks" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title":"Complete project","description":"Finish the task app","status":"pending"}'
```

### Using Postman

1. Import the API collection
2. Set environment variable `base_url` = `http://localhost:8000/api/v1`
3. Register/Login to get token
4. Add token to Authorization header: `Bearer YOUR_TOKEN`

## 🔒 Security Features

- **Password Security**: Bcrypt hashing with salt
- **JWT Authentication**: Stateless token-based auth
- **CORS Protection**: Configurable allowed origins
- **Input Validation**: Pydantic models for request validation
- **SQL Injection Prevention**: SQLAlchemy ORM
- **XSS Protection**: React automatic escaping

## 🐛 Troubleshooting

### Backend Issues

**Database Connection Error:**
```bash
# Check MySQL is running
mysql -u root -p

# Verify database exists
SHOW DATABASES;
```

**Module Import Errors:**
```bash
# Ensure you're in the Backend directory
cd Backend

# Run as module, not direct script
uvicorn app.main:app --reload
# NOT: python app/main.py
```

**Port Already in Use:**
```bash
# Change port in run.py or use:
uvicorn app.main:app --reload --port 8001
```

### Frontend Issues

**Dependencies Not Installing:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

**API Connection Failed:**
- Check backend is running on `http://localhost:8000`
- Verify `VITE_API_BASE_URL` in `.env` file
- Check browser console for CORS errors

## 📈 Future Enhancements

- [ ] Task categories and tags
- [ ] Task due dates and reminders
- [ ] Task sharing and collaboration
- [ ] File attachments for tasks
- [ ] Email notifications
- [ ] Dark mode support
- [ ] Mobile responsive improvements
- [ ] Task analytics and statistics
- [ ] Export tasks to CSV/PDF
- [ ] Two-factor authentication (2FA)

##  Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Afrin Mufeena
- GitHub: (https://github.com/Ahamed-Afrin)
- LinkedIn: (https://www.linkedin.com/in/afrin-mufeena-s-a99545278/)
- Email: afrinmufn@gmail.com

 ## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)


---

⭐ If you find this project helpful, please give it a star!

**Made with ❤️ using FastAPI and React**

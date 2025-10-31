# Django Movies & TV Shows API 🎬📺

REST API built with Django REST Framework for managing movies and TV shows with comprehensive authentication, search, and multiple view patterns (FBV, CBV, Mixins, Generics, ViewSets).

## ✨ Features

- 🔐 **Token Authentication** - Secure API access with token-based authentication
- 🔍 **Advanced Search** - Search across movies and TV shows with multiple filters
- 📚 **Multiple View Patterns** - Implemented using Function-Based Views, Class-Based Views, Mixins, Generics, and ViewSets
- 🎬 **Movies Management** - Full CRUD operations for movies
- 📺 **TV Shows Management** - Full CRUD operations for TV shows
- 🔒 **Protected Endpoints** - All data endpoints require authentication
- 📝 **Well Documented** - Complete API documentation included

## 🛠️ Tech Stack

- **Django** 5.2.7
- **Django REST Framework** 3.16.1
- **SQLite** (default database)
- **Token Authentication**

## 📦 Installation

1. **Clone the repository:**
```bash
git clone git@github.com:K7alid/django-movies-tvshows-api.git
cd django-movies-tvshows-api
```

2. **Create virtual environment:**
```bash
python -m venv .env
source .env/bin/activate  # On Windows: .env\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run migrations:**
```bash
cd movies_tvshows_api
python manage.py makemigrations
python manage.py migrate
```

5. **Run the server:**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 🚀 Quick Start

### 1. Register a new user:
```bash
POST /api/auth/register/
{
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
}
```

### 2. Login to get your token:
```bash
POST /api/auth/login/
{
    "username": "your_username",
    "password": "your_password"
}
```

### 3. Use the token in your requests:
```bash
Authorization: Token YOUR_TOKEN_HERE
```

### 4. Access protected endpoints:
```bash
GET /api/movies/
GET /cbv/movies/
GET /fbv/movies/
# ... and many more!
```

## 📚 API Endpoints

See [API_ENDPOINTS.md](API_ENDPOINTS.md) for complete API documentation.

### Authentication (Public)
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login and get token

### Movies (Protected - Require Token)
- **ViewSet:** `/api/movies/` - Full CRUD with router
- **FBV:** `/fbv/movies/` - Function-Based Views
- **CBV:** `/cbv/movies/` - Class-Based Views (APIView)
- **Mixins:** `/mixins/movies/` - Mixins pattern
- **Generics:** `/generics/movies/` - Generic views

### TV Shows (Protected - Require Token)
- Same patterns as Movies: `/api/tvshows/`, `/fbv/tvshows/`, `/cbv/tvshows/`, etc.

### Search Parameters
- `?search=keyword` - Search in title, director, genre, etc.
- `?year=2020` - Filter by year
- `?q=keyword` - Alternative search parameter

## 🔐 Authentication

All endpoints (except login/register) require token authentication:

```http
Authorization: Token YOUR_TOKEN_HERE
```

## 📁 Project Structure

```
django-movies-tvshows-api/
├── movies_tvshows_api/
│   ├── config/           # Main settings & URLs
│   ├── movies/          # Movies app
│   ├── tvshows/         # TV Shows app
│   └── manage.py
├── requirements.txt
├── API_ENDPOINTS.md    # Complete API documentation
└── README.md
```

## 🎯 View Patterns Implemented

This project demonstrates **5 different Django REST Framework patterns**:

1. **Function-Based Views (FBV)** - Traditional Django function views
2. **Class-Based Views (CBV)** - Using APIView
3. **Mixins** - Combining mixins with GenericAPIView
4. **Generics** - Generic class-based views (ListCreateAPIView, etc.)
5. **ViewSets** - Using ModelViewSet with routers

## 📝 Example Usage

### Search Movies
```bash
GET /api/movies/?search=nolan&year=2010
Authorization: Token YOUR_TOKEN
```

### Create Movie
```bash
POST /api/movies/
Authorization: Token YOUR_TOKEN
Content-Type: application/json

{
    "title": "",
    "year": ,
    "genre": "",
    "director": "",
    ...
}
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**K7alid**

---

⭐ If you find this project helpful, please give it a star!


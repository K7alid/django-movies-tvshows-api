# جميع API Endpoints المتاحة

**ملاحظة:** كل الـ endpoints تتطلب Token Authentication في Header:
```
Authorization: Token YOUR_TOKEN_HERE
```

---

## 🔐 Authentication APIs (غير محمية)

### Register
- **POST** `/api/auth/register/`
- **Body:** `{"username": "test", "password": "test123", "email": "test@example.com"}`
- **Response:** `{"token": "...", "username": "test"}`

### Login
- **POST** `/api/auth/login/`
- **Body:** `{"username": "test", "password": "test123"}`
- **Response:** `{"token": "...", "username": "test"}`

---

## 🎬 Movies APIs (كلها محمية - تتطلب Token)

### ViewSet (Router)
- **GET** `/api/movies/` - قائمة الأفلام (مع بحث: `?search=keyword`)
- **POST** `/api/movies/` - إضافة فيلم جديد
- **GET** `/api/movies/{id}/` - تفاصيل فيلم
- **PUT** `/api/movies/{id}/` - تعديل فيلم كامل
- **PATCH** `/api/movies/{id}/` - تعديل فيلم جزئي
- **DELETE** `/api/movies/{id}/` - حذف فيلم

**Search Parameters:**
- `?search=keyword` - يبحث في: title, director, genre, year
- `?year=2020` - فلترة بالسنة

---

### Function-Based Views (FBV)
- **GET** `/fbv/movies/` - قائمة (مع بحث: `?search=keyword&year=2020`)
- **POST** `/fbv/movies/` - إضافة جديد
- **GET** `/fbv/movies/{id}/` - تفاصيل
- **PUT** `/fbv/movies/{id}/` - تعديل
- **DELETE** `/fbv/movies/{id}/` - حذف

---

### Class-Based Views (CBV / APIView)
- **GET** `/cbv/movies/` - قائمة (مع بحث)
- **POST** `/cbv/movies/` - إضافة جديد
- **GET** `/cbv/movies/{id}/` - تفاصيل
- **PUT** `/cbv/movies/{id}/` - تعديل
- **DELETE** `/cbv/movies/{id}/` - حذف

---

### Mixins
- **GET** `/mixins/movies/` - قائمة (مع بحث)
- **POST** `/mixins/movies/` - إضافة جديد
- **GET** `/mixins/movies/{id}/` - تفاصيل
- **PUT** `/mixins/movies/{id}/` - تعديل
- **DELETE** `/mixins/movies/{id}/` - حذف

---

### Generics
- **GET** `/generics/movies/` - قائمة (مع بحث)
- **POST** `/generics/movies/` - إضافة جديد
- **GET** `/generics/movies/{id}/` - تفاصيل
- **PUT** `/generics/movies/{id}/` - تعديل
- **DELETE** `/generics/movies/{id}/` - حذف

---

## 📺 TV Shows APIs (كلها محمية - تتطلب Token)

### ViewSet (Router)
- **GET** `/api/tvshows/` - قائمة المسلسلات (مع بحث: `?search=keyword`)
- **POST** `/api/tvshows/` - إضافة مسلسل جديد
- **GET** `/api/tvshows/{id}/` - تفاصيل مسلسل
- **PUT** `/api/tvshows/{id}/` - تعديل مسلسل كامل
- **PATCH** `/api/tvshows/{id}/` - تعديل مسلسل جزئي
- **DELETE** `/api/tvshows/{id}/` - حذف مسلسل

**Search Parameters:**
- `?search=keyword` - يبحث في: title, genre, stars, year
- `?year=2020` - فلترة بالسنة

---

### Function-Based Views (FBV)
- **GET** `/fbv/tvshows/` - قائمة (مع بحث)
- **POST** `/fbv/tvshows/` - إضافة جديد
- **GET** `/fbv/tvshows/{id}/` - تفاصيل
- **PUT** `/fbv/tvshows/{id}/` - تعديل
- **DELETE** `/fbv/tvshows/{id}/` - حذف

---

### Class-Based Views (CBV / APIView)
- **GET** `/cbv/tvshows/` - قائمة (مع بحث)
- **POST** `/cbv/tvshows/` - إضافة جديد
- **GET** `/cbv/tvshows/{id}/` - تفاصيل
- **PUT** `/cbv/tvshows/{id}/` - تعديل
- **DELETE** `/cbv/tvshows/{id}/` - حذف

---

### Mixins
- **GET** `/mixins/tvshows/` - قائمة (مع بحث)
- **POST** `/mixins/tvshows/` - إضافة جديد
- **GET** `/mixins/tvshows/{id}/` - تفاصيل
- **PUT** `/mixins/tvshows/{id}/` - تعديل
- **DELETE** `/mixins/tvshows/{id}/` - حذف

---

### Generics
- **GET** `/generics/tvshows/` - قائمة (مع بحث)
- **POST** `/generics/tvshows/` - إضافة جديد
- **GET** `/generics/tvshows/{id}/` - تفاصيل
- **PUT** `/generics/tvshows/{id}/` - تعديل
- **DELETE** `/generics/tvshows/{id}/` - حذف

---

## 📝 ملاحظات

1. **Search Parameters:** 
   - استخدم `?search=keyword` أو `?q=keyword` للبحث
   - استخدم `?year=2020` للفلترة بالسنة

2. **DateTime Format:**
   - `created_at` و `updated_at` تظهر كـ: `2025-10-30 13:03:55`

3. **Error Responses:**
   - بدون token: `{"detail": "Authentication credentials were not provided."}`
   - Invalid token: `{"detail": "Invalid token."}`

---

## 📊 إجمالي الـ Endpoints

- **Authentication:** 2 endpoints
- **Movies:** 30 endpoints (6 patterns × 5 methods)
- **TV Shows:** 30 endpoints (6 patterns × 5 methods)
- **Total:** 62 endpoints


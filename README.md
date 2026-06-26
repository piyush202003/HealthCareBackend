super user:
    username = admin
    email = admin@gmai.com
    password = admin123


database:
user = id, username, email, password, created_at
patient = id, name, age, gender, phone, created_by(FK user), created_at
doctor = id, name, specialization, phone, created_by(fk user), created_at

part 1:
POST /api/auth/register/
{
    "username": "ram",
    "email" : "ram@gmail.com",
    "password": "ram@1234",
}

POST /api/auth/login/
{
    "username": "ram",
    "password": "ram@1234",
}
{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4MjUzOTA3MCwiaWF0IjoxNzgyNDUyNjcwLCJqdGkiOiIzYWM3ZjZiOWFmYTA0ZTE3YTBmNzFkZjMyOGMyYjc0NyIsInVzZXJfaWQiOiIyIn0.taarEdS92GgRJPQiieekf1kHMeDubWrz5CrFy8nkuQI",
"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgyNDUyOTcwLCJpYXQiOjE3ODI0NTI2NzAsImp0aSI6ImYxOGRmYmYzM2FkNDQwZWNiMDYzMDc2Yzk1MjhkMzBmIiwidXNlcl9pZCI6IjIifQ.Fn_UkZpbiXKKvj96n8OBNPKxjA4e3KcauCocRbhPvVk"}

part 2: 
POST /api/patients/
Authorization: Bearer <access_token>
{
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "gender": "Male",
    "phone": "9876543210",
    "address": "Mumbai"
}

GET /api/patients/
Authorization: Bearer <access_token>

GET /api/patients/1/
Authorization: Bearer <access_token>

PUT /api/patients/1/
Authorization: Bearer <access_token>
{
    "first_name": "John",
    "last_name": "Smith",
    "age": 31,
    "gender": "Male",
    "phone": "9999999999",
    "address": "Pune"
}

DELETE /api/patients/1/
Authorization: Bearer <access_token>

part 3 :
POST /api/doctors/
Authorization: Bearer <access_token>
{
    "first_name": "Rahul",
    "last_name": "Sharma",
    "specialization": "Cardiologist",
    "experience": 10,
    "phone": "9876543210",
    "email": "rahul.sharma@example.com"
}

GET /api/doctors/
Authorization: Bearer <access_token>

GET /api/doctors/1/
Authorization: Bearer <access_token>

PUT /api/doctors/1/
Authorization: Bearer <access_token>
{
    "first_name": "Rahul",
    "last_name": "Sharma",
    "specialization": "Neurologist",
    "experience": 12,
    "phone": "9876543210",
    "email": "rahul.sharma@example.com"
}

DELETE /api/doctors/1/
Authorization: Bearer <access_token>

part 4:
POST /api/mappings/
{
    "patient": 1,
    "doctor": 2
}

GET /api/mappings/

GET /api/mappings/1/

DELETE /api/mappings/1/

To allow anyone:
from rest_framework.permissions import AllowAny, IsAuthenticated

class DoctorListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class DoctorDetailAPIView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

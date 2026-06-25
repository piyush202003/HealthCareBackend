super user:
    username = admin
    email = admin@gmai.com
    password = admin123


database:
user = id, username, email, password, created_at
patient = id, name, age, gender, phone, created_by(FK user), created_at
doctor = id, name, specialization, phone, created_by(fk user), created_at
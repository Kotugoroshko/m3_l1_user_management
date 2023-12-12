from fastapi import FastAPI

app = FastAPI()

# Студенти можуть одразу використовувати схеми замість використання простого класу
class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.id = user_id
        self.username = username
        self.email = email


users = [
    User(user_id=1, username="john_doe", email="john@example.com"),
    User(user_id=2, username="jane_doe", email="jane@example.com"),
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}


@app.get("/users")
def get_all_users():
    return users


@app.post("/create_user")
def create_user(username: str, email: str):
    user_id = len(users) + 1
    new_user = User(user_id=user_id, username=username, email=email)
    users.append(new_user)
    return new_user

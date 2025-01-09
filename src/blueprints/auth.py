from flask import Blueprint
from flask_login import UserMixin

auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder="templates"
)

class User(UserMixin):

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
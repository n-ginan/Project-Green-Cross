from flask import Blueprint, render_template
from flask_login import UserMixin, login_required

auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder="templates"
)

class User(UserMixin):

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

@auth_bp.route("/admin-dashboard", methods=["GET"])
@login_required
def admin_dashboard():
    # Should return staff and doctor data to show on the front-end side
    return render_template("admin-dashboard.html")
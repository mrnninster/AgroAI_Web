from flask import Blueprint

agroai_bp = Blueprint('agroai_bp',__name__,template_folder="templates", static_folder="static", static_url_path="static")
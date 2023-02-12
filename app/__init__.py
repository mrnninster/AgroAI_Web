import secrets
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)
    app.config.from_object('app.config.BaseConfig')
    
    # Pushing Application Context
    with app.app_context():
        from app import routes
        from app.agroai import agroai_bp

        app.register_blueprint(agroai_bp, url_prefix='/agroai')
    return app

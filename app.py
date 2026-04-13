from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager
from models import db, User
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey_dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Ensure upload folder exists
    upload_folder = os.path.join(app.root_path, 'static', 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Import blueprints
    from routes.auth_routes import auth_bp
    from routes.user_routes import user_bp
    from routes.admin_routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @app.route('/')
    def index():
        return render_template('index.html')

    with app.app_context():
        db.create_all()
        # Seed admin user
        from werkzeug.security import generate_password_hash
        admin = User.query.filter_by(email='admin@system.com').first()
        if not admin:
            hashed_pw = generate_password_hash('admin123', method='pbkdf2:sha256')
            new_admin = User(name='System Admin', email='admin@system.com', password_hash=hashed_pw, role='admin')
            db.session.add(new_admin)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

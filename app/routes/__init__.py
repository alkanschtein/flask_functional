from .Home import home_bp
from .User import user_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(stock_bp)
    app.register_blueprint(user_bp)


from flask import Flask

from .extensions import db, migrate


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object("config.Config")

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from .routes import main
    app.register_blueprint(main)

    # admin blueprint (optional)
    try:
        from .admin.routes import admin_bp
        app.register_blueprint(admin_bp)
    except Exception:
        # if admin package missing or broken, proceed without it
        pass

    return app

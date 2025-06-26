from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
import os



env_file = os.getenv("ENV_FILE", "development.env")
load_dotenv(env_file)
db = SQLAlchemy()
cache =Cache()
migrate = Migrate()
redisHost = os.getenv("REDIS_HOST")
redisPort = os.getenv("REDIS_PORT")
redisPassword = os.getenv("REDIS_PASSWORD")
redisUri = f"redis://:{redisPassword}@{redisHost}:{redisPort}"
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri=redisUri
)

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CACHE_TYPE"] = "RedisCache"
    app.config["CACHE_REDIS_URL"] = redisUri

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    migrate.init_app(app, db)
    # Register blueprints or routes here
    from app.models import Manager, Employee

    @app.route('/', methods=['GET'])
    def index():
        return "Welcome to the Employee Management System"

    from app.routes import employee_routes, manager_routes

    app.register_blueprint(employee_routes.employee_bp)
    app.register_blueprint(manager_routes.manager_bp)

    return app


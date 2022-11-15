from flask import Flask
from views import main_bp


def create_app():
    app_1 = Flask(__name__)
    app_1.register_blueprint(main_bp)
    return app_1


if __name__ == '__main__':
    app = create_app()
    app.run(port=25000, debug=True)

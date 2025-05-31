from flask import Flask


def crear_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "¡Hola, Flask sin entorno virtual!"

    return app

if __name__ == '__main__':
    app = crear_app()
    app.run(debug=True)
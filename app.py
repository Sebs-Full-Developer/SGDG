# app.py
from flask import Flask
from apps.controllers.auth_controller import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
    #print(app.url_map)
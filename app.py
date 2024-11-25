# app.py
from flask import Flask
from apps.controllers.auth_controller import auth_bp
from apps.controllers.home import home_bp
from apps.controllers.usuario import usuario_bp

#app = Flask(__name__)
app = Flask(__name__, template_folder='apps/templates')
app.secret_key = "1JhfYJeuBT5R9l14HwwubQKcpsjAxjbLdr820yIYUXcFIxfQl47qv1P7Rwlsp4Rc"  # Establecer una clave secreta para sesiones y cookies

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True)
    #print(app.url_map)
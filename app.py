# app.py
from flask import Flask
from apps.controllers.auth_controller import auth_bp
from apps.controllers.home import home_bp

from apps.controllers.genero import genero_bp
from apps.controllers.usuario import usuario_bp
from apps.controllers.clave import clave_bp
from apps.controllers.pais import pais_bp
from apps.controllers.estado import estado_bp
from apps.controllers.ciudad import ciudad_bp
from apps.controllers.persona import persona_bp
from apps.controllers.telefono import telefono_bp
from apps.controllers.cargo import cargo_bp
from apps.controllers.entidad import entidad_bp
from apps.controllers.asignacion_cargo import asignacion_cargo_bp

#app = Flask(__name__)
app = Flask(__name__, template_folder='apps/templates', static_folder='apps/static')
app.secret_key = "1JhfYJeuBT5R9l14HwwubQKcpsjAxjbLdr820yIYUXcFIxfQl47qv1P7Rwlsp4Rc"  # Establecer una clave secreta para sesiones y cookies

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(genero_bp)
app.register_blueprint(usuario_bp)
app.register_blueprint(clave_bp)
app.register_blueprint(pais_bp)
app.register_blueprint(estado_bp)
app.register_blueprint(ciudad_bp)
app.register_blueprint(persona_bp)
app.register_blueprint(telefono_bp)
app.register_blueprint(cargo_bp)
app.register_blueprint(entidad_bp)
app.register_blueprint(asignacion_cargo_bp)

if __name__ == '__main__':
    app.run(debug=True)
    #print(app.url_map)
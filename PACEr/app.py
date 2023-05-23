from flask import Flask
import secrets
from routes import home, calculator

pacer = Flask(__name__ , template_folder='templates', static_folder='static')
pacer.secret_key = secrets.token_hex(16)


pacer.register_blueprint(home.bp_home)
pacer.register_blueprint(calculator.bp_calculator)


if __name__ == '__main__':
    pacer.run(debug=True, host="0.0.0.0", port=5000)



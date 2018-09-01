from flask import render_template
from flask_api import FlaskAPI
import settings
from helpers import authenticated, auth_required, get_buzzer, set_buzzer, finish

app = FlaskAPI(__name__)

@app.route('/', methods=["GET"])
def api_root():
    return render_template('index.html')


@app.route('/buzzer', methods=["GET"])
def get_buzzer_state():
    return get_buzzer()

@app.route('/buzzer', methods=["POST"])
def enable_buzzer():
    if authenticated():
        return set_buzzer(enable=True)

    return auth_required()


@app.route('/buzzer', methods=["DELETE"])
def disable_buzzer():
    if authenticated():
        return set_buzzer(enable=False)

    return auth_required()


if __name__ == "__main__":
    try:
        app.debug = True
        app.run(host=settings.rest['listen'], port=settings.rest['port'])
    finally:
        finish()

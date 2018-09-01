import syslog
import settings
from flask import request, make_response, jsonify
from RPi import GPIO

syslog.openlog(settings.logging_ident)
BUZZER_GPIO = settings.gpio['buzzer']
GPIO.setmode(GPIO.BCM)

def auth_required():

    resp = make_response("Not authenticated")
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Relays Access"'

    return resp

def authenticated():

    auth = request.authorization

    if not auth:
        return False

    if settings.auth['uid'] == auth.username and settings.auth['password'] == auth.password:
        return True

    return False

def log_gpio_action(action, gpio, state):
    if settings.logging_enable:
        syslog.syslog(syslog.LOG_INFO, ("%s GPIO %s: %s" % (action, gpio, state)))

def get_buzzer():
    state = GPIO.input(BUZZER_GPIO)
    log_gpio_action('Get', BUZZER_GPIO, state)
    return jsonify(buzzer=state)

def set_buzzer(enable=False):
    if enable:
        log_gpio_action('Set', BUZZER_GPIO, GPIO.LOW)
        GPIO.output(BUZZER_GPIO, GPIO.LOW)
    else:
        log_gpio_action('Set', BUZZER_GPIO, GPIO.HIGH)
        GPIO.output(BUZZER_GPIO, GPIO.HIGH)

    return jsonify(buzzer=GPIO.input(BUZZER_GPIO))

def finish():
    GPIO.cleanup()

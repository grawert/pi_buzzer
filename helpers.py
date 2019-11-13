import sys
import logging
import settings
from flask import request, make_response, jsonify
from RPi import GPIO

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

BUZZER_GPIO = settings.gpio['buzzer']
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_GPIO, GPIO.OUT)

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
        logging.debug('user %s successfully authenticated' % auth.username)
        return True

    logging.debug('user %s authentication failed' % auth.username)
    return False

def log_gpio_action(action, gpio, state):
    if settings.logging_enable:
        logging.info("%s GPIO %s: %s" % (action, gpio, state))

def get_buzzer():
    state = GPIO.input(BUZZER_GPIO)
    log_gpio_action('Get', BUZZER_GPIO, state)
    return jsonify(buzzer=state)

def set_buzzer(enable=False):
    if enable:
        log_gpio_action('Set', BUZZER_GPIO, GPIO.HIGH)
        GPIO.output(BUZZER_GPIO, GPIO.HIGH)
    else:
        log_gpio_action('Set', BUZZER_GPIO, GPIO.LOW)
        GPIO.output(BUZZER_GPIO, GPIO.LOW)

    return jsonify(buzzer=GPIO.input(BUZZER_GPIO))

def finish():
    GPIO.cleanup()

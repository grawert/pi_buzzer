# Pi Buzzer

Pi Buzzer is a simple REST API to control a door buzzer via Rasberry Pi GPIO.
Authentication is required to enable/disable the buzzer. HTTP Basic Auth is used.

## Setup

    sudo apt-get install build-essential libsasl2-dev python-dev libldap2-dev libssl-dev python-pip
    pip install -r requirements.txt

## Run

    python main.py

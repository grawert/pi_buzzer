from main import app
from helpers import finish

if __name__ == "__main__":
    try:
        app.debug = True
        app.run()
    finally:
        finish()

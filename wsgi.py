from main import app
from helpers import finish

if __name__ == "__main__":
    try:
        app.run()
    finally:
        finish()

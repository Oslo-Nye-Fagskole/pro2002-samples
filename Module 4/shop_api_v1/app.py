# app.py
from flask import Flask

# Creates and configures the Flask application
def create_app() -> Flask:
    flask_app = Flask(__name__)
    # Keeps JSON keys in the same order they were added (for consistent output)
    flask_app.config.from_mapping(JSON_SORT_KEYS=False)
    # TODO Register routes

    return flask_app

# Entry point used by "flask run" or production servers
app = create_app()

# For direct local runs (optional):
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from dealership.routes import vehicles, customers, sales

def create_app():
    dealership_app = Flask(__name__)

    # Register blueprints
    dealership_app.register_blueprint(vehicles.bp)
    dealership_app.register_blueprint(customers.bp)
    dealership_app.register_blueprint(sales.bp)

    return dealership_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
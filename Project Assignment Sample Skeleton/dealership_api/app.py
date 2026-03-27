from flask import Flask, jsonify
from dealership.routes import vehicles, customers, sales

def create_app():
    dealership_app = Flask(__name__)

    # Register blueprints
    dealership_app.register_blueprint(vehicles.bp)
    dealership_app.register_blueprint(customers.bp)
    dealership_app.register_blueprint(sales.bp)

    # ---------------------------------------------------------
    # TEMPORARY HEALTHCHECK / PLACEHOLDER ENDPOINT
    # TODO: REMOVE this endpoint once real routes are implemented
    # This exists only to verify the skeleton project runs correctly.
    # ---------------------------------------------------------
    @dealership_app.route("/", methods=["GET"])
    def temp_endpoint():
        return jsonify({
            "message": "Skeleton project - remove this endpoint before implementing real functionality"
        }), 200

    return dealership_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
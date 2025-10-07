from flask import Flask

# Create a new Flask application instance
app = Flask(__name__)

# Define a simple route - We'll for sure make more soon ;)
@app.route('/')
def home():
    return 'Hello, shoppers! Our shop will soon be open for business via a sweet API!'

# Run the app only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True) # Enable live reloading, very convenient for development

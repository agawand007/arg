from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Jenkins CI/CD Lab Assessment</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #333; }
            .container { background-color: #f0f0f0; padding: 20px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello World!</h1>
            <h2>Welcome to the Jenkins CI/CD Lab Assessment</h2>
            <p>✓ Flask application is running successfully</p>
            <p>✓ Docker image deployed from Docker registry</p>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

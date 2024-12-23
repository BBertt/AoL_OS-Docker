from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return """
    <html>
        <head>
            <title>Welcome to Flask in Docker!</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #3498db, #9b59b6);
                    color: white;
                    text-align: center;
                    padding: 50px;
                    margin: 0;
                }
                h1 {
                    font-size: 3em;
                    margin: 20px 0;
                }
                p {
                    font-size: 1.2em;
                    margin: 15px 0;
                }
                a {
                    color: #f1c40f;
                    text-decoration: none;
                    font-weight: bold;
                }
                a:hover {
                    color: #e67e22;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Welcome to Flask in Docker! 🌟</h1>
            <p>This is a minimalistic Flask app running inside a Docker container.</p>
            <p>Get started with Docker and Flask, and make something amazing!</p>
            <a href="https://flask.palletsprojects.com/">Learn Flask →</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # host='0.0.0.0' makes the app accesible from any network interface not just localhost.
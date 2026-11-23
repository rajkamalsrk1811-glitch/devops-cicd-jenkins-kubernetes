from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My DevOps Project!</h1>
    <h2>Deployed using Docker on AWS EC2</h2>
    <p>My first containerized application.</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

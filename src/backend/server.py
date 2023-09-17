from Flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')

def hello():
    return "Hello, how are you?"

if __name__ == "__main__" :
    print("Starting Python Flask server For Plant Nursery Managment System")
    app.run(port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    contents = request.json['contents'] # Get the file contents from the request

    # Process the CSV file and extract the desired feature
    # Replace this with your own logic
    feature = contents.split(',')[6]

    return jsonify({'feature': feature})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

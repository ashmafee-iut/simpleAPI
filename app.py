from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route
@app.route('/')
def home_app():
    return "Welcome to the Simple API??!"

# # A route to return data
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     data = {
#         'name': 'John Doe',
#         'age': 30,
#         'email': 'john@example.com'
#     }
#     return jsonify(data)

# # A route to accept POST requests
# @app.route('/api/post', methods=['POST'])
# def post_data():
#     posted_data = request.json
#     return jsonify({
#         'you_posted': posted_data
#     }), 201

if __name__ == '__main__':
    app.run(debug=True)

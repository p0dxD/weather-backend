#!flask/bin/python
from flask import Flask
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello, World!"

@app.route('/weather/api/v1.0/data/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    return "hello" + str(task_id)

if __name__ == '__main__':
            app.run(debug=True)

@app.route('/weather/api/v1.0/insert', methods=['POST'])
def create_task():
    print(request.json)
    return "success", 201


#For error handling
@app.errorhandler(404)
def not_found(error):
    return make_response("The page you're looking for does not exist.", 404)
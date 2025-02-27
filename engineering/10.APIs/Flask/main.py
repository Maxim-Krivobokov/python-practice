# flask is installed in WSL; or use venv
from flask import Flask, request, jsonify
from logging.config import dictConfig

# Defining format of logs
dictConfig({
    "version": 1,
    "formatters": { "default": {
        "format": '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }},
    "handlers": {
        "wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ['wsgi']
    }
})

app = Flask(__name__)

# That type of storage for testing purpose only
COURSES = {}

@app.route('/')
def hello_world():
    return "Hello world\n"

# templated params are defined with <variable_name>
# also we can pre-define type: <int:var_name> - if other type will be passed, error '404' will occur
@app.route("/course/<course_name>", methods=["GET", "DELETE"])
def show_course_by_name(course_name):
    if request.method == "GET":
        app.logger.info(request.args)
        app.logger.info(request.headers)
        app.logger.info(request.cookies)
        return COURSES[course_name]
    if request.method == "DELETE":
        del COURSES[course_name]
        return jsonify({"status": "ok"})

@app.route("/course", methods=["PUT"])
def create_course():
    app.logger.info(request.get_data())
    app.logger.info(request.is_json)
    payload = request.json
    COURSES[payload["name"]] = payload["desc"]
    return jsonify({"status": "ok"})
# flask is installed in WSL; or use venv
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world\n"

# templated params are defined with <variable_name>
# also we can pre-define type: <int:var_name> - if string will be passed, error '404' will occur
@app.route("/course/<course_name>/unit/<int:unit_id>")
def show_course_by_name(course_name, unit_id):
    return f"course {type(course_name)} {course_name} and unit {type(unit_id)} {unit_id}\n", 202
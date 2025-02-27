# How to work with flask
### Install venv

## Run
need to setup env var before launch:

```sh
export FLASK_APP=main
flask run
```

### How to test local webserver:
example with args, tokens, cookies:
```sh
curl "localhost:5000/course/cpp/unit/002.1?sort=id&order=asc" -H "x-auth-token: ahdgcajhsdgasjhgd2132" --cookie "ga=2376452367452367"
```
example PUT request, to add the course:

```sh
curl "localhost:5000/course" -X PUT -d '{"name": "kafka", "desc": "apache kafka installation"}' -H "Content-Type: application/json"
```

## Working in async mode;
### Gunicorn
install with pip: ```pip3 install gunicorn```

How to launch:
```sh
guniciorn -w 4 -b 0.0.0.0:4000 main:app
# -w 4 = 4 workers
# -b = bind address and port
# main.py = main, application is called app;
```
Important!
Gunicorn won't work with scripts, that stores data in internal dict-list objects, like COURSES = {}
Each worker will have own COURSES;
Must use external storage (DB for example)
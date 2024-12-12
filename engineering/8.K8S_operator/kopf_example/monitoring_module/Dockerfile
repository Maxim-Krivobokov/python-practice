FROM python:3-buster

RUN pip install flask faker

ENV PYTHONPATH=/app/lib

COPY main.py /app/lib/monitoring/main.py

WORKDIR /app/lib

ENTRYPOINT python3 monitoring/main.py
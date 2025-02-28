from flask import Flask, request, Response
from prometheus_client.core import REGISTRY, CounterMetricFamily, HistogramMetricFamily
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, GCColeector

"""
REGISTRY = Storage of all metrics, that we scrape
CONTENT_TYPE_LATEST = constant, enables to pass header "content_type" via http request
"""

app = Flask(__name__)

class CustomServiceExporter:
    stored_req_count = {}
    stored_latency = {}
    # Buckets are used to build histograms
    BUCKETS = {
        "0.01": 0,
        "0.5": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "10": 0,
    }

    def collect(self):
        request_total = CounterMetricFamily(
            "http_service_requests_total",
            "Service HTTP requests count with status code",
            labels=["status"]
        )
        
        latency = HistogramMetricFamily(
            "http_service_latency",
            "Service HTTP requests duration",
            labels=["endpoint"]
        )
        for status, count in self.stored_req_count.items():
            request_total.add_metric([status], count)
        
        yield request_total

# Need to register class with custom metrics
REGISTRY.register(CustomServiceExporter)


@app.route("/metric-receiver")
def track_metric():
    data = request.json
    CustomServiceExporter.stored_req_count[str(data["status"])] = CustomServiceExporter.stored_req_count.get(str(data["status"]), 0) + 1
    build_histogram(data["endpoint"], data["time"])
    return Response(status=200)

def build_histogram(endpoint, duration):
    endpoint_storage = CustomServiceExporter.stored_latency.setdefault(endpoint, {})
    bucket_storage = endpoint_storage.setdefault("buckets", CustomServiceExporter.BUCKETS)

    for bucket in bucket_storage.keys():
        if duration < float(bucket):
            bucket_storage[bucket] += 1

    endpoint_storage["sum"] = endpoint_storage.get("sum", 0) + duration

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
# Writing custom prometheus exporter

Prometheus exporters work with 'pull' principle;
prometheus_client lib has classes CounterMetricFamily, HistogramMetricFamily, to work with corresponding metrics types

## How to run:

```sh
# Run exporter
export FLASK_APP=main
flask run

# Run service
export FLASK_APP=push_metric_service
flask run --port=4000
```
How to test:

```sh
# Test service:
curl "localhost:4000/process-finances"

# Test exporter:
curl "localhost:5000/metrics"
```

### TODO:
- short notes about most popular Flask methods;
- notes about prometheus_client entities and usage cases;
- debug exporter, add docstrings;



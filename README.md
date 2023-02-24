# flask-otel
Playing around with OpenTelemetry instrumentation

## Flask Auto Instrumentation
From [OpenTelemetry's documentation](https://opentelemetry.io/docs/instrumentation/python/automatic/), using this command:

`
opentelemetry-instrument --traces_exporter console,otlp --metrics_exporter console --service_name test-server --exporter_otlp_endpoint 0.0.0.0:4317 python3 server.py
`

to export data into the console.

## Running the collector locally
Following [OpenTeletry's documentation](https://opentelemetry.io/docs/instrumentation/python/getting-started/) for collector config and python commands.

Running the colllector locally with Docker based on [these instructions from OTel](https://opentelemetry.io/docs/collector/getting-started/#docker)
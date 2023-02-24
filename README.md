# flask-otel
Playing around with OpenTelemetry instrumentation

## Flask Auto Instrumentation
From [OpenTelemetry's documentation](https://opentelemetry.io/docs/instrumentation/python/automatic/), using this command:

`
opentelemetry-instrument --traces_exporter console,otlp --metrics_exporter console --service_name your-service-name --exporter_otlp_endpoint 0.0.0.0:4317 python3 server.py
`

to export data into the console.
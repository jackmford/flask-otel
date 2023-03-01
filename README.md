# flask-otel
Playing around with OpenTelemetry instrumentation

## Flask Auto Instrumentation
From [OpenTelemetry's documentation](https://opentelemetry.io/docs/instrumentation/python/automatic/), using this command:

`
OTEL_SERVICE_NAME="jacks-service" opentelemetry-instrument --metrics_exporter console --traces_exporter otlp python3 server.py
`

to export metrics data into the console and trace data to whatever otel collector you have running alongside your app (in this case locally).

## Running the collector locally
Following [OpenTeletry's documentation](https://opentelemetry.io/docs/instrumentation/python/getting-started/) for collector config and python commands.

Running the colllector locally with Docker based on [these instructions from OTel](https://opentelemetry.io/docs/collector/getting-started/#docker).

## Running Jaeger locally to evaluate trace data
Followed [this blog](https://rehansaeed.com/exporting-open-telemetry-data-to-jaeger/)

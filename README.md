# flask-otel
Playing around with OpenTelemetry instrumentation

## Flask Auto Instrumentation
From [OpenTelemetry's documentation](https://opentelemetry.io/docs/instrumentation/python/automatic/), using this command:

`
opentelemetry-instrument python3 server.py
`

to export data into the console.

## Running the collector locally
Following [OpenTeletry's documentation](https://opentelemetry.io/docs/instrumentation/python/getting-started/) for collector config and python commands.

Running the colllector locally with Docker based on [these instructions from OTel](https://opentelemetry.io/docs/collector/getting-started/#docker)
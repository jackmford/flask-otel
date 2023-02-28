import random
import requests
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

app = Flask(__name__)
provider = TracerProvider()
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

@app.route("/roll")
def dyce_roll():
    with tracer.start_as_current_span("random_roll"):  
        span = trace.get_current_span()
        num = random.randint(1,6)
        span.add_event( "log", {
            "num": num,
        })
    print(num)

    return str(num)

@app.route("/")
def main():
    response = requests.get('https://jackmitchellfordyce.com')
    print(response)

    return str(response.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
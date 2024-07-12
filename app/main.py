from flask import Flask
from prometheus_client import Counter, generate_latest
from prometheus_client.core import CollectorRegistry
from flask import Response

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total App Requests')


@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()
    return 'Bem-vindo ao mundo do DevOps!'


@app.route('/metrics')
def metrics():
    registry = CollectorRegistry()
    registry.register(REQUEST_COUNT)
    return Response(generate_latest(registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

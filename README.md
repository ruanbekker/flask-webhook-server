# flask-webhook-server
Webhook Server that accepts POST requests

## About

This is a very basic flask service that accepts POST requests that I use for tinkering with clients that requires webhook endpoints.

## Usage

Run a container for the webhook server:

```
$ docker run -it -p 5000:5000 ruanbekker/webhook
```

Health check endpoint:

```
$ curl http://localhost:5000/health
{"status":"up"}
```

Make a POST request:

```
$ curl -XPOST -d '{"key": "x"}' http://localhost:5000/
{"key":"x"}
```

The content is also returned on the server side:

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
 * Running on http://172.17.0.4:5000/ (Press CTRL+C to quit)
{'key': 'x'}
172.17.0.1 - - [08/Jun/2021 09:49:59] "POST / HTTP/1.1" 200 -
```

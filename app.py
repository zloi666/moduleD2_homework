import sentry_sdk
import os

from bottle import Bottle, request, response, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

SERVER_URL = "https://powerful-reaches-50289.herokuapp.com"

sentry_sdk.init(
    dsn="https://c8cf36597da3461589eff1cc607d2b6e@o495253.ingest.sentry.io/5567698",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    page = """
    <!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>module D2 homework </title>
        </head>
        <body>
            <a href='/success'>return status 200/OK</a>
            <a href='fail'>Rise error</a>
        </body>
    </html>
    """
    return page


@app.route('/success')
def success():  
    return HTTPResponse(status=200, body="200/OK")


@app.route('/fail')  
def fail():  
    raise RuntimeError("There is an error!")  
    return  


if __name__ == "__main__":
    if os.environ.get("APP_LOCATION") == "heroku":
        app.run(
            host="0.0.0.0",
            port=int(os.environ.get("PORT")),
            server="gunicorn",
            workers=3,
        )
    else:
        app.run(host="localhost", port=8080, debug=True)

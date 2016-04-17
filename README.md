# python-react and eve

This is a super simple, monolithic app that uses server-side rendering to
deliver precompiled React to the frontend that avoids further page requests by
querying eve's REST API for data.

## Installation

Install dependencies

```command
apt-get install mongodb
pip install -r requirements.txt
npm install
```

Start the render server

```command
node render_server.js
```

Start the Python server

```command
python run.py
```

Visit http://127.0.0.1:8000

For a more production-y feel, you can also use gunicorn

```command
gunicorn run:app --threads 2
```

Make sure you change [run.py](run.py) so it doesn't run in `debug` mode anymore
and `threaded=False`.

## Thanks

- [@markfinger](https://github.com/markfinger) for [python-react](https://github.com/markfinger/python-react)
- [@nicolaiarocci](https://github.com/nicolaiarocci) for [Eve](https://github.com/nicolaiarocci/eve)

## NOTE

This code is not best-practice; it's minimum viable. It's meant to help
one get started.

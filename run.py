import os

from eve import Eve
from routes.comments import comments
from settings import CONFIG

PWD = os.environ.get('PWD')
static = os.path.join(PWD, 'static')

app = Eve(static_folder=static, settings=CONFIG)
app.register_blueprint(comments)
app.debug = True

if __name__ == '__main__':
    # app.run()
    app.run(port=8000, threaded=True)

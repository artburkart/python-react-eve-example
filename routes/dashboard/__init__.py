import os
import requests

from flask import Blueprint
from flask import render_template
from react.render import render_component


dashboard = Blueprint('dashboard', __name__, template_folder='templates')


@dashboard.route('/')
def index():
    r = requests.get('http://localhost:8000/api/v1/comments')
    rendered = render_component(
        os.path.join(os.getcwd(), 'static', 'js', 'CommentBox.jsx'),
        {
            'comments': r.json().get('data'),
            'url': '/comment/',
        },
        to_static_markup=True,
    )

    return render_template('dashboard.html', rendered=rendered)

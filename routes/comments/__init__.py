import os
import requests

from flask import Blueprint
from flask import render_template
from react.render import render_component


comments = Blueprint('comments', __name__, template_folder='templates')


@comments.route('/')
def index():
    r = requests.get('http://localhost:8000/api/v1/comments')
    comments = r.json().get('data')
    rendered = render_component(
        os.path.join(
            os.getcwd(), 'static', 'js', 'comments', 'CommentBox.jsx'
        ),
        {
            'comments': comments,
            'url': '/api/v1/comments',
        },
        to_static_markup=True,
    )

    return render_template(
        'comments.html', rendered=rendered, comments=comments)

import ReactDOM from 'react-dom'
import React from 'react'
import CommentBox from '../comments/CommentBox.jsx'

ReactDOM.render(<CommentBox comments={window.APP_PROPS} url='/api/v1/comments'/>, document.getElementById('container'))

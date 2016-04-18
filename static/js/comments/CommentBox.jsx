import React from 'react';
import CommentList from './CommentList.jsx';
import CommentForm from './CommentForm.jsx';
import fetchival from 'fetchival';

class CommentBox extends React.Component {
  constructor(props) {
    super(props)
    this.state = {comments: props.comments}
  }
  submitComment(author, text) {
    // Get previous comments
    let comments = this.state.comments.slice()
    const comment = {author, text}

    // POST new comment
    fetchival('/api/v1/comments')
      .post(comment)
      .then((json) => {
        // Render component with new comments
        comments.push(Object.assign(json, comment))
        this.setState({comments})
      })
  }
  render() {
    return (
      <div>
        <CommentList comments={this.state.comments} />
        <CommentForm submitComment={this.submitComment.bind(this)} />
      </div>
    );
  }
}

export default CommentBox;
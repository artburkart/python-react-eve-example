import React from 'react';

class CommentForm extends React.Component {
  handleSubmit(evt) {
    evt.preventDefault()

    // Get values
    const author = this.refs.author.value.trim()
    const text = this.refs.text.value.trim()

    // Clear inputs
    this.refs.author.value = ''
    this.refs.text.value = ''

    // Submit values
    this.props.submitComment(author, text)
  }
  render() {
    return (
      <form onSubmit={this.handleSubmit.bind(this)}>
        <h2>Submit a comment</h2>
        <div className="form-group">
          <label>
            Your name
            <input ref="author" name="author" type="text" className="form-control" placeholder="..." />
          </label>
        </div>
        <div className="form-group">
          <label>
            Say something...
            <textarea ref="text" name="text" className="form-control" placeholder="..." />
          </label>
        </div>
        <div className="text-right">
          <button type="reset" className="btn btn-default">Reset</button>
          <button type="submit" className="btn btn-primary">Submit</button>
        </div>
      </form>
    );
  }
}

export default CommentForm;
import React, { Component } from 'react';

class PostInLine extends Component {
  render() {
    const {title} = this.props
    return (
      <div>
        <h1>Post's {title}</h1>
      </div>
    );
  }
}

export default PostInLine;

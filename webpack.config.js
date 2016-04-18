module.exports = {
  entry: "./static/js/app/App.jsx",
  output: {
    path: __dirname,
    filename: "./static/js/bundle.js",
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  }
}

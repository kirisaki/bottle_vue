const webpack = require('webpack');

module.exports = {
  entry: './scripts/app.js',
  output: {
    path: __dirname,
    publicPath: '/',
    filename: './scripts/bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            js: 'babel-loader'
          }
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    alias: {
    }
  }
};

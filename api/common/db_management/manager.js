"use strict";

const connecter = require('./connector');
module.exports.start = (callback) => {
  connecter.start(callback);
}

module.exports.close = (callback) => {
  connecter.close(callback)
}

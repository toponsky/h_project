'user strict';

const bag_handler = require('./bag/router')

module.exports = function(app) {
  bag_handler(app)
};

'user strict';
const auth = require('./auth/router');
const bag_handler = require('./bag/router');

module.exports = function(app) {
  auth(app);
  bag_handler(app)
};

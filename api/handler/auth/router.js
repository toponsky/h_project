const authCtl = require('./handler');

module.exports = function(app) {
  let prefix = config.api_version

  console.log("API :" + prefix + 'token');
  app.route(prefix + 'token').
    post(authCtl.grantToken);
}
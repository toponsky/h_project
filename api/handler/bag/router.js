'user strict';

const handler = require("./handler");
let prefix = config.api_version + config.api_secured;

module.exports = function(app) {
  app.route(prefix + 'get_all_bag').get(handler.getAllBag)
  app.route(prefix + 'checked_bag').post(handler.checkedBag)
}
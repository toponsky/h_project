'user strict';

const handler = require("./handler");


module.exports = function(app) {
  app.route(config.api_version + 'get_all_bag').get(handler.getAllBag)
  app.route(config.api_version + 'checked_bag').post(handler.checkedBag)
}
'use strict';

var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var bag_info  = new Schema({
  id: { type: String },
  url: { type: String },
  img_url: { type: String },
  name: { type: String },
  color: { type: String, default: '' },
  p_price: { type: String },
  create_time: { type: Date },
  is_blocked: { type: Boolean, default: false },
  is_available: { type: Boolean, default: false },
  is_destroy: { type: Boolean, default: false },
  is_checking: { type: Boolean, default: false }
});

module.exports = mongoose.model('bag_info', bag_info);
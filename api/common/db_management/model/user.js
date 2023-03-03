'use strict';

var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var user  = new Schema({
  username: { type: String },
  password: { type: String },
  email: { type: String },
  phone_no: { type: String },
  email_alert: { type: Boolean, default: true },
  sms_alert: { type: Boolean, default: false },
});

module.exports = mongoose.model('user', user);
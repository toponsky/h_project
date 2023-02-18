'user strict';


require('./config/config');
const express = require('express'),
    bodyParser = require("body-parser"),
    app = express();

app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    console.log((new Date()).toString() + " -- Request host: " + req.hostname + ", URL: " + req.url);
    next();
});


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.listen(config.port);
console.log('API Server start on port ' + config.port);
exports = module.exports = app;
'user strict';


require('./common/config/config');
const express = require('express'),
    bodyParser = require("body-parser"),
    app = express();
const dbMger = require('./common/db_management/manager');


function main() {
  const router = require('./handler/router');
      
  app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
      console.log((new Date()).toString() + " -- Request host: " + req.hostname + ", URL: " + req.url);
      next();
  });
  
  
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use(bodyParser.json());
  router(app)
  app.on('close', ()=>{
    dbMger.close()
    console.log('Connection terminated');
  });
  app.listen(config.port);
  console.log('API Server start on port ' + config.port);

 
  exports = module.exports = app;
}

dbMger.start(main)

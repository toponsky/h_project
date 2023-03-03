'user strict';

require('./common/config/config');
const cors = require('cors');
const express = require('express');
const bodyParser = require("body-parser");
const app = express();
const dbMgr = require('./common/db_management/manager');
const sessionHelper = require('./common/session/helper')

function main() {
  const router = require('./handler/router');
      
  app.use(function (req, res, next) {
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS');
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Credentials", "true");
    res.setHeader("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
    console.log((new Date()).toString() + " -- Request host: " + req.hostname + ", URL: " + req.url);
    next();
  });
  
  app.use(cors())
  app.use(sessionHelper.verifyToken);
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use(bodyParser.json());
  router(app)
  app.on('close', ()=>{
    dbMgr.close()
    console.log('Connection terminated');
  });
  app.listen(config.port);
  console.log('API Server start on port ' + config.port);

 
  exports = module.exports = app;
}

dbMgr.start(main)

const jwt = require('jsonwebtoken');
exports.verifyToken = function(req, res, next) {
  //Get auth header value
  if(req.url.indexOf(config.api_secured) < 0) {
    next();
  } else {
    try {
      const bearer = req.headers['authorization'].split(' ');
      console.log(bearer);
      console.log(config.api_secured)
      req.token = bearer[1];
      req.user = jwt.verify(bearer[1], config.api_secret_key);
      console.log("User is: " +req.user.email)
      next();
    }
    catch (ex) { 
      console.log(ex)
      res.sendStatus(403);
    }
  }
}

exports.getReqBaseUrl = function(req) {
  return req.url
}
const mongoose = require('mongoose'),
  bcrypt = require('bcrypt'),
  jwt = require('jsonwebtoken');

let User = mongoose.model('user');
exports.grantToken = async function(req,res) {

  let reqData = req.body,
    errMsg = ''
  if(reqData.email == undefined) {
    errMsg += " Empty Email.";
    return res.sendStatus(400);
  }
  if(reqData.password == undefined){
    errMsg += " Empty Passord.";
    return res.sendStatus(400);
  } 
  const user = await User.findOne({
    email: reqData.email
  });

  if(user && reqData.password == user.password) {
    let userObj = {
      username:         user.username,
      password:         user.password,
      email:            user.email,
      phone_no:         user.phone_no,
      email_alert:      user.email_alert,
      sms_alert:        user.sms_alert
    };
    let token = jwt.sign(userObj, config.api_secret_key, {
      expiresIn: '2 days'
    });
    res.json({
      "access_token": token
    });
  } else {
    return res.status(400).send({
      message: "Invalid username or password"
    });
  }
}
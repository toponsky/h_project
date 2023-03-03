'user strict';

const mongoose = require('mongoose');
mongoose.pluralize(null)

module.exports.start = (callback) => {
  mongoose.Promise = global.Promise;

  const MONGO_HOST = config.db_connection['db_host'] ;
  const MONGO_PORT = config.db_connection['db_port'];
  const MONGO_DB   = config.db_connection['db_name'];
  const MONGO_USER = config.db_connection['username'];
  const MONGO_PASS = config.db_connection['password'];

  let connectStr = "mongodb://"+ MONGO_USER +":"+ MONGO_PASS +"@"+ MONGO_HOST +":"+ MONGO_PORT +"/"+ MONGO_DB;
  mongoose.set("strictQuery", false);
  mongoose.connect(connectStr, {
    socketTimeoutMS: 0,
    useNewUrlParser: true,
    useUnifiedTopology: true
  }).then(()=>{
    console.log("MongoDB successfully connected");
    console.log("Start Application");
    require('./model/bagInfo')
    require('./model/user')
    if(callback) {
      callback()
    }
    
  }).catch(err=> {
    console.log("error connecting to the database'", err);
    process.exit();
  });
}

module.exports.close = (callback) => {
  mongoose.connection.close();
  if(callback) {
    callback()
  }
}
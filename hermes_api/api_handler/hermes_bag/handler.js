'user strict';

'user strict';

const mongoose = require('mongoose');

const bagInfo = mongoose.model('bag_info');

exports.getAllBag = function(req, res) {

  bagInfo.find({"is_destroy": {"$nin": ["null", "false"]}}, function(err, bags) {
    if(err) 
      res.send(err)
    res.json(bags)
  });
}
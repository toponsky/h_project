'user strict';

const mongoose = require('mongoose');
const bagInfo = mongoose.model('bag_info');

exports.getAllBag = function(req, res) {

  bagInfo.find({is_destroy: false}).sort({ create_time: 'desc' }).exec(function(err, bags) {
    if(err) 
      res.send(err)
    res.json(bags)
  });
}


exports.checkedBag = function(req, res) {
  let bag = req.body;
  let query = {id: bag.id};
					
  bagInfo.findOneAndUpdate(query, {"is_checking": bag.is_checking}, {upsert: false}, function(err, result) {
    if(err) {
      res
        .status(err.status)
        .send("Fail to update bag")
        console.log("Fail to update bag");
    } else {
      res.json({
        'ok': 'true'
      })
      console.log("Bag "+ bag.id + "is update successfully");
    }
  })
}
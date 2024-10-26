const mongoose = require('mongoose');

const userSchema = new mongoose.Schema(
  {
    FullName: String,
    Num_Of_actions: Number
  },
  { versionKey: false }
);

const user = mongoose.model('user', userSchema, 'users');

module.exports = user;
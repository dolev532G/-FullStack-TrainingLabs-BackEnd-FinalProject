const mongoose = require('mongoose');

const departmentSchema = new mongoose.Schema(
  {
    Name: String,
    Manager: { type: mongoose.Schema.Types.ObjectId, ref: 'employees' }


  },
  { versionKey: false }
);

const department = mongoose.model('department', departmentSchema, 'departments');

module.exports = department;
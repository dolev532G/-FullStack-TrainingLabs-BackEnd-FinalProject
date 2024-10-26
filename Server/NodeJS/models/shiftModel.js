const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema(
  {
    ID: [{ type: mongoose.Schema.Types.ObjectId, ref: 'employees' }],
    Date: Date,
    StartingHour: Number,
    EndingHour: Number


  },
  { versionKey: false }
);

const employee = mongoose.model('shift', employeeSchema, 'shifts');

module.exports = employee;
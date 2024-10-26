const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema(
  {
    FirstName: String,
    LastName: String,
    StartWorkYear: Number,
    DepartmentID: { type: mongoose.Schema.Types.ObjectId, ref: 'departments' }


  },
  { versionKey: false }
);

const Employee = mongoose.model('employee', employeeSchema, 'employees');

module.exports = Employee;
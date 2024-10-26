const employee = require('../models/employeeModel');

// Get All
const getAllemployees = (filters) => {
  return employee.find(filters);
};

// Get By ID
const getById = (id) => {
  return employee.findById(id);
};

// Create
const addemployee = (obj) => {
  const employee_obj = new employee(obj);
  return employee_obj.save();
};

// Update
const updateemployee = (id, obj) => {
  return employee.findByIdAndUpdate(id, obj);
};

// Delete
const deleteemployee = (id) => {
  return employee.findByIdAndDelete(id);
};

const deleteMany = (obj) => {
  return employee.deleteMany(obj);
}

module.exports = {
  getAllemployees,
  deleteMany,
  getById,
  addemployee,
  updateemployee,
  deleteemployee,
};

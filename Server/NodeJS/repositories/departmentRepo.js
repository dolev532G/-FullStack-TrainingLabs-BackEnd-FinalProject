const department = require('../models/departmentModel');

// Get All
const getAlldepartments = (filters) => {
  return department.find(filters);
};

// Get By ID
const getById = (id) => {
  return department.findById(id);
};

// Create
const adddepartment = (obj) => {
  const dep = new department(obj);
  return dep.save();
};

// Update
const updatedepartment = (id, obj) => {
  return department.findByIdAndUpdate(id, obj);
};

// Delete
const deletedepartment = (id) => {
  return department.findByIdAndDelete(id);
};

module.exports = {
  getAlldepartments,
  getById,
  adddepartment,
  updatedepartment,
  deletedepartment,
};

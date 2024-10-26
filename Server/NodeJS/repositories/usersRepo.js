const user = require('../models/UserModel');

// Get All
const getAllusers = (filters) => {
  return user.find(filters);
};

// Get By ID
const getById = (id) => {
  return user.findById(id);
};

// Create
const adduser = (obj) => {
  const user = new user(obj);
  return user.save();
};

// Update
const updateuser = (id, obj) => {
  return user.findByIdAndUpdate(id, obj);
};

// Delete
const deleteuser = (id) => {
  return user.findByIdAndDelete(id);
};

module.exports = {
  getAllusers,
  getById,
  adduser,
  updateuser,
  deleteuser,
};

const departmentsRepo = require('../repositories/departmentRepo');
const employeesRepo = require('../repositories/employeesRepo');
const ShiftsRepo = require('../repositories/shiftsRepo');
const { ObjectId } = require('mongodb');

const getAlldepartments = (filters) => {
  return departmentsRepo.getAlldepartments(filters);
};

const getById = (id) => {
  return departmentsRepo.getById(id);
};


const adddepartment = (obj) => {
  return departmentsRepo.adddepartment(obj);
};

const updatedepartment = (id, obj) => {
  return departmentsRepo.updatedepartment(id, obj);
};

const deletedepartment = async (id) => {
  return departmentsRepo.deletedepartment(id);
};

module.exports = {
  getAlldepartments,
  getById,
  adddepartment,
  updatedepartment,
  deletedepartment,
};

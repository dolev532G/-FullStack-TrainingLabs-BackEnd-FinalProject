const shiftsRepo = require('../repositories/shiftsRepo');

const getAllshifts = (filters) => {
  return shiftsRepo.getAllshifts(filters);
};

const getById = (id) => {
  return shiftsRepo.getById(id);
};

const addshift = (obj) => {
  return shiftsRepo.addshift(obj);
};

const updateshift = (id, obj) => {
  return shiftsRepo.updateshift(id, obj);
};

const allocateEmployee = (id, IDEmployee) => {
  return shiftsRepo.allocateEmployee(id, IDEmployee);
};

const deleteshift = (id) => {
  return shiftsRepo.deleteshift(id);
};

module.exports = {
  getAllshifts,
  allocateEmployee,
  getById,
  addshift,
  updateshift,
  deleteshift,
};

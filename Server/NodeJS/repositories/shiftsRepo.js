const shift = require('../models/shiftModel');

// Get All
const getAllshifts = (filters) => {
  return shift.find(filters);
};

// Get By ID
const getById = (id) => {
  return shift.findById(id);
};


const allocateEmployee = async (id, employeeId) => {

  try {
    // Find the shift by its ID first
    const shiftDocument = await shift.findById(id);

    // If the shift is not found
    if (!shiftDocument) {
      return 'Shift not found';
    }

    // Check if the employee is already in the ID array
    if (shiftDocument.ID.includes(employeeId)) {
      return 'Employee is already allocated to this shift';
    }

    // If not, push the employee ID into the ID array
    shiftDocument.ID.push(employeeId);

    // Save the updated shift document
    const updatedShift = await shiftDocument.save();

    return {
      message: 'Employee allocated successfully',
      updatedShift
    };
  } catch (err) {
    return `Error adding employee ID: ${err.message}`;
  }
};



// Create
const addshift = (obj) => {
  const shi = new shift(obj);
  return shi.save();
};

// Update
const updateshift = (id, obj) => {
  return shift.findByIdAndUpdate(id, obj);
};

// Delete
const deleteshift = (id) => {
  return shift.findByIdAndDelete(id);
};

module.exports = {
  getAllshifts,
  allocateEmployee,
  getById,
  addshift,
  updateshift,
  deleteshift,
};

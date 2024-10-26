const { ObjectId } = require('mongodb');

const employee = require('../models/employeeModel');
const department = require('../models/departmentModel');

const employeesRepo = require('../repositories/employeesRepo');
const DepertmantsRepo = require('../repositories/departmentRepo');
const ShiftsRepo = require('../repositories/shiftsRepo');

const getAllemployees = (filters) => {
  return employeesRepo.getAllemployees(filters);
};


const GetEmployeesPage = async () => {
  let employees = await employeesRepo.getAllemployees();
  const Departments = await DepertmantsRepo.getAlldepartments();
  const shifts = await ShiftsRepo.getAllshifts();

  let EPage = []

  employees.forEach(elemnt => {

    let dep = Departments.filter(d => d._id.equals(elemnt.DepartmentID))
    let shiftsforID = shifts.filter(s =>
      s.ID.some(s1 => s1.equals(elemnt._id)) // Use 'some' to check for existence
    ).map(X => ({
      "Date": X.Date,
      "StartingHour": String(X.StartingHour),
      "EndingHour": String(X.EndingHour)
    }));



    EPage.push({
      "Id": String(elemnt._id),
      "Full name": elemnt.FirstName + " " + elemnt.LastName,
      "Department": dep.length > 0 ? dep[0].Name : "Not assigned",
      "Shifts": shiftsforID

    })
  })

  return EPage

};


const getById = async (id) => {
  let employees = await employeesRepo.getById(id);
  let Departments = await DepertmantsRepo.getById(employees.DepartmentID);

  const obj = {

    "_id": employees._id,
    "FirstName": employees.FirstName,
    "LastName": employees.LastName,
    "StartWorkYear": employees.StartWorkYear,
    "DepartmentID": employees.DepartmentID,
    "Department": Departments ? Departments.Name : "",
  }

  return obj;

};

const addemployee = (obj) => {
  if (obj.DepartmentID && !(obj.DepartmentID instanceof ObjectId)) {
    obj.DepartmentID = new ObjectId(obj.DepartmentID);
  }

  if (obj.DepartmentID.length == 0)
    delete obj.DepartmentID;

  return employeesRepo.addemployee(obj);
};

const updateemployee = (id, obj) => {
  if (obj.DepartmentID && !(obj.DepartmentID instanceof ObjectId)) {
    obj.DepartmentID = new ObjectId(obj.DepartmentID);
  }

  return employeesRepo.updateemployee(id, obj);
};

const deleteemployee = (id) => {
  return employeesRepo.deleteemployee(id);
};

const deleteMany = (obj) => {
  return employee.deleteMany(obj);
}

module.exports = {
  getAllemployees,
  GetEmployeesPage,
  deleteMany,
  getById,
  addemployee,
  updateemployee,
  deleteemployee,
};

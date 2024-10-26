const express = require('express');
const employeesService = require('../services/employeesService');
const ValidationService = require('../services/ValidationService');

const router = express.Router();

// Entry point: http://localhost:3000/employees

// Get All employees
router.get('/', async (req, res) => {
  try {
    const filters = req.query;
    const employees = await employeesService.getAllemployees(filters);
    res.json(employees);
  } catch (error) {
    res.json(error);
  }
});


// Get All employees
router.get('/EmployeesPage', async (req, res) => {
  try {
    const filters = req.query;
    const emp = await employeesService.GetEmployeesPage();
    res.json(emp);
  } catch (error) {
    res.json(error);
  }
});


// Get a employee By ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const employee = await employeesService.getById(id);
    res.json(employee);
  } catch (error) {
    res.json(error);
  }
});

// Add a new employee
router.post('/', async (req, res) => {

  const validreq = await ValidationService.ServerRequest(req.body.token);
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const obj = req.body.employee;
    console.log(obj)
    const result = await employeesService.addemployee(obj);

    res.status(201).json(result);
  } catch (error) {
    res.status(500).json(error.message);
  }
});

// Update a employee
router.put('/:id', async (req, res) => {

  const validreq = await ValidationService.ServerRequest(req.body.token);
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const { id } = req.params;
    const obj = req.body.employee;
    const result = await employeesService.updateemployee(id, obj);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

// Delete a employee
router.delete('/:id/', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  if ( validreq === 0 ||  validreq.length === 0)
  {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const { id } = req.params;
    const result = await employeesService.deleteemployee(id);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

module.exports = router;

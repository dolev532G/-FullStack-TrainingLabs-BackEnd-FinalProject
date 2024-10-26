const express = require('express');
const departmentsService = require('../services/departmentsService');
const employeesService = require('../services/employeesService');
const { ObjectId } = require('mongodb');
const ValidationService = require('../services/ValidationService');

const router = express.Router();

// Entry point: http://localhost:3000/departments

// Get All departments
router.get('/', async (req, res) => {
  try {
    const filters = req.body;
    const departments = await departmentsService.getAlldepartments(filters);
    res.json(departments);
  } catch (error) {
    res.json(error);
  }
});

// Get a department By ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const department = await departmentsService.getById(id);
    res.json(department);
  } catch (error) {
    res.json(error);
  }
});

// Add a new department
router.post('/', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  console.log(req.body.token)
  if (validreq === 0 || validreq.length === 0) {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const obj = req.body.department;
    const result = await departmentsService.adddepartment(obj);
    res.status(201).json(result);
  } catch (error) {
    res.status(500).json(error.message);
  }
});

// Update a department
router.put('/:id', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  console.log(req.body.token)
  if (validreq === 0 || validreq.length === 0) {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const { id } = req.params;
    const obj = req.body.department;
    const result = await departmentsService.updatedepartment(id, obj);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

// Delete a department
router.delete('/:id/', async (req, res) => {
  const validreq = await ValidationService.ServerRequest(req.body.token);
  console.log(req.body.token)
  if (validreq === 0 || validreq.length === 0) {
    res.status(500).json("Can't do another actions today")
    return;
  }
  try {
    const { id } = req.params;
    const result = await departmentsService.deletedepartment(id);
    const result2 = await employeesService.deleteMany({ "DepartmentID": new ObjectId(id) })
    res.json(result + result2);
  } catch (error) {
    res.json(error);
  }
});

module.exports = router;

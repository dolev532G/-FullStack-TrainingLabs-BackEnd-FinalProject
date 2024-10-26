const express = require('express');
const usersService = require('../services/usersService');

const router = express.Router();

// Entry point: http://localhost:3000/users

// Get All users
router.get('/', async (req, res) => {
  try {
    const filters = req.query;
    const users = await usersService.getAllusers(filters);
    console.log(users)
    res.json(users);
  } catch (error) {
    res.json(error);
  }
});

// Get a User By ID
router.get('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const User = await usersService.getById(id);
    res.json(User);
  } catch (error) {
    res.json(error);
  }
});

// Add a new User
router.post('/', async (req, res) => {
  try {
    const obj = req.body;
    const result = await usersService.addUser(obj);
    res.status(201).json(result);
  } catch (error) {
    res.status(500).json(error.message);
  }
});

// Update a User
router.put('/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const obj = req.body;
    const result = await usersService.updateUser(id, obj);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

// Delete a User
router.delete('/:id/', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await usersService.deleteUser(id);
    res.json(result);
  } catch (error) {
    res.json(error);
  }
});

module.exports = router;

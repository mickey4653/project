const express = require('express');
const router = express.Router();
const userController = require('../controllers/user.controller');

//retrieve all users
router.get('/api/user_signup', userController.findAll);

//create a new user
router.post('/api/user_signup', userController.create);

module.exports = router
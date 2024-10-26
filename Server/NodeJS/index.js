const express = require('express');
const cors = require('cors');
const connectDB = require('./configs/db');

const usersRouter = require('./controllers/usersController');
const employeeRouter = require('./controllers/employeesController');
const departmentRouter = require('./controllers/departmentsController');
const shiftRouter = require('./controllers/shiftsController');
const ValidationRouter = require('./controllers/usersValidationController');


const app = express();
const PORT = 3000;

connectDB();

app.use(cors());

app.use('/', express.json());

app.use('/users', usersRouter);
app.use('/employees', employeeRouter);
app.use('/departments', departmentRouter);
app.use('/shifts', shiftRouter);
app.use('/Validation', ValidationRouter);

app.listen(PORT, () => {
  console.log(`app is listening at http://localhost:${PORT}`);
});





# Dolev's Factory Management

## Description
Dolev's Factory Management is a web-based system that allows users to manage factory operations by adding employees, creating and managing departments, and allocating shifts to workers. It includes both a client-side interface and two server-side implementations for flexibility.

The system uses a dataset that consists of shifts, employees, departments, and users. For example:

**Shift Example**:
```json
{
    "_id" : ObjectId("6716d1daa477624aa7a92189"),
    "ID" : ["6713aa36a477624aa7a9210a", "6713aa36a477624aa7a9210c", "671acdd6a15e98679d7dceb0", "671abe995d84e800d41a922d"],
    "Date" : "2024-10-25",
    "StartingHour" : 8,
    "EndingHour" : 16
}
```

**User Example**:
```json
{
    "_id" : ObjectId("67139f65a477624aa7a920ea"),
    "FullName" : "Leanne Graham",
    "Num_Of_actions" : 8
}
```

**Department Example**:
```json
{
    "_id" : ObjectId("6718c94751cd6b0e11900482"),
    "Name" : "Research and Development",
    "Manager" : ObjectId("671acdf1733c0b7d80484795")
}
```

**Employee Example**:
```json
{
    "_id" : ObjectId("671b9f086db89b1d35904e60"),
    "FirstName" : "My",
    "LastName" : "4",
    "StartWorkYear" : 500,
    "DepartmentID" : ObjectId("671b8f89bf06146a9296d732")
}
```

## Project Structure
```
Dolev's Factory Management
|
+---Client
|       add_department.html
|       add_employee.html
|       departments.html
|       edit_department.html
|       edit_employee.html
|       employees.html
|       login.html
|       shifts.html
|       styles.css
|       users.html
|
\---Server
    +---Data
    |   |   Readme.txt
    |   |   System_Users_Actions.json
    |   |   Tokens.txt
    |   \---MongoBackup
    |           departments.json
    |           employees.json
    |           shifts.json
    |           users.json
    +---Flask
    |   |   main.py
    |   +---BLL
    |   +---DAL
    |   +---routers
    +---NodeJS
        |   index.js
        +---configs
        +---controllers
        +---models
        +---repositories
        \---services
```

## Running the Project

### Node.js (Port 3000)
To run the server with Node.js, follow these steps:
1. Navigate to the `/Server/NodeJS` folder.
2. Run the following command:
    ```bash
    nodemon index.js
    ```

### Flask Python (Port 5000)
To run the Flask-based server, follow these steps:
1. Navigate to the `/Server/Flask` folder.
2. Run one of the following commands:
    - Debug Mode:
      ```bash
      python -m flask --app main.py run --debug
      ```
    - Production Mode:
      ```bash
      python -m flask --app main.py run --no-debugger --reload 2> $null
      ```

### MongoDB & Studio 3T
- The project uses MongoDB, which runs on **port 27017**. The database is called `MyDB`.
- You can interact with the database using **Studio 3T** to manage and visualize collections.

### HTML Web Client
To run the client side, follow these steps:
1. Navigate to the `/Client` folder.
2. Start a server using `browser-sync` with the following command:
    ```bash
    browser-sync start --server --files "*.html, *.css, *.js"
    ```

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: 
  - **Node.js** (Port 3000)
  - **Flask (Python)** (Port 5000)
- **Database**: MongoDB (for storing employee, department, and shift data)
  - **Web Service**: The project also connects to a web service for retrieving data.
  - **JSON Log**: Local JSON files are used as logs for storing system user actions.

## Contributions
Feel free to contribute by submitting a pull request or reporting issues. All contributions and feedback are welcome!

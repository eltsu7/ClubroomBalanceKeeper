# Clubroom Balance Keeper

An application + API to keep track of club members virtual balance.

## Contributing
Fork & PR.

## Endpoints
User
- GET returns user data
- PUT registers new user
- DELETE deletes user

Product
- GET returns available products
- PUT adds new product
- DELETE deletes product

Transaction
- PUT adds new transaction

## Application components
- router, validates input and passes it to controller
- controller, hosts logic, passes commands to repository 
- repository, takes care of database access

## TODOs
- Rename if necessary
- Choose technologies and database
- Finalize endpoints
- Make the damn thing

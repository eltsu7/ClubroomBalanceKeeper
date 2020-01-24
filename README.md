# Clubroom Balance Keeper

An application + API to keep track of club members virtual balance.

## Contributing
Fork & PR.

## Endpoints

/user
- GET returns all users
- POST registers new user

/user/id
- GET returns user data
- PUT update user data (nickname)
- DELETE deletes user

/user/id/transactions
- GET returns users transactions
- PUT adds new transaction

/product
- GET returns available products
- POST adds new product
- DELETE deletes product

## Application components
- router, validates input and passes it to controller
- controller, hosts logic, passes commands to repository 
- repository, takes care of database access

## TODOs
- Rename if necessary
- Choose technologies and database
- Finalize endpoints
- Make the damn thing

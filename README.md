## Local setup
* run `pip install -r requirements.txt`
* Browse and Enjoy APIs I buit

## API endpoints
### `http://127.0.0.1:8000/register/`
* creates new user
* POST method
* takes input as json
* example : 
`{
    "username": "lucky_new",
    "password": "lucky"
}`

### `http://127.0.0.1:8000/api-token-auth/`
* Provide token to existing user
* POST method
* takes input same as above

### `http://127.0.0.1:8000/api/v1`
* GET/POST method
* Lists all user related tasks in GET
* Add new task in POST

### `http://127.0.0.1:8000/api/v1/<int:id>`
* GET/PUT/DELETE method
* See single task in GET
* update single task in PUT
* delete single task in DELETE

## Features
* HMAC based Token Authentication and Authorization
* DjangoRest Framework
* CRUD operations

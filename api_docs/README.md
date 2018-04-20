# Viraja Pay Backend Docs


### Create User

Anyone can create a user, the only required field is a password. Creating a new user with only a password will generate a random username.

```
$ curl http://localhost:8000/api/create_user/ -X POST -d "username=my-username&password=my-password"
```

Response will be data submitted.

### Token authentication

To avoid basic authentication we will require token authentication. You can retrieve the token by using (once) the username and password of the user.

```
$ curl http://localhost:8000/api/token/ -X POST -d "username=my-username&password=my-password"
```

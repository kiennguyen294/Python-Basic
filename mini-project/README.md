## Introduce
This is a small project with the purpose of increasing python code skills.
An http request includes user_name, age, id sent to API. The API then sends the information to service hash via rabbitmq (using rpc).
Service 1 will hash the above 3 fields and then store the value in mysql
## Architecture
![img](../img/arcitecture%20.png)
## Code
## Running
## API
```buildoutcfg
curl -i -H "Content-Type: application/json" -X POST -d '{"user": "kienn","age":"18","customerId":"10000000"}' http://localhost:5656/api/person
```
## deploy-examples/services

Basic python services to show how containers communicate through the stack. 

#### Web

See [`web/`](./web)

Basic frontend web application using flask, communicates with the logger api to pull data from the database. Shows details on which container(s) are handling the request.

#### Logger

See [`logger/`](./logger)

Flask based logging API with a Postgres database. 

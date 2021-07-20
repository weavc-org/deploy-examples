## deploy-examples

Testing continuous integration & deployment strategies using python, github actions & docker swarm. This is made to demonstrate a 'production-like' docker stack where we have multiple containers doing different jobs, replicas load balancing and communicating with one another via networks.

Over time I would like to incorporate more of the docker swarm features and explore the different ways the different services/containers should be handled in a production environment.

### Stack
- nginx reverse proxy ([`weavc-nginx`](https://github.com/weavc/weavc-nginx))
- python web frontend (see `services/`)
- python logger api (see `services/`)
- postgres database with replica sets
- network tools for testing (`praqma/network-multitool`)


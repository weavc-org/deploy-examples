### deploy-examples

Testing continuous integration & deployment stragies using python, github actions & docker swarm. This is made to demonstrate a 'production-like' docker stack where we have multiple containers doing different jobs, replicas load balancing and containers communicating with one another via overlay networks.

The stack consists of
- nginx reverse proxy ([`weavc-nginx`](https://github.com/weavc/weavc-nginx))
- python web frontend (see `services/src/web`)
- python logger api (see `services/src/logger`)
- postgres database
- network tools for testing (`praqma/network-multitool`)

Over time I would like to incorporate more of the docker swarm features and explore the different ways the different services/containers should be handled in a production environment.


deploy:
	docker stack deploy -c compose-stack.yml deploy-examples

ssl:
	openssl req -newkey rsa:4096 -new -nodes -x509 -days 3650 -keyout ./secrets/privkey.pem -out ./secrets/fullchain.pem
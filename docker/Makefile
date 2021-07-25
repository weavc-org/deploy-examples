
deploy:
	make deploy-db & make deploy-metrics & make deploy-services

vm-deploy:
	make vm-deploy-db & make vm-deploy-metrics & make vm-deploy-services

deploy-services:
	docker stack deploy -c ./compose-services.yml deploy-examples

vm-deploy-services:
	docker -c m1 stack deploy -c ./compose-services.yml deploy-examples

deploy-metrics:
	docker stack deploy -c ./compose-metrics.yml deploy-examples-metrics

vm-deploy-metrics:
	docker -c m1 stack deploy -c ./compose-metrics.yml deploy-examples-metrics

deploy-db:
	docker stack deploy -c ./compose-databases.yml deploy-examples-db

vm-deploy-db:
	docker -c m1 stack deploy -c ./compose-databases.yml deploy-examples-db

ssl:
	openssl req -newkey rsa:4096 -new -nodes -x509 -days 3650 -keyout ./secrets/privkey.pem -out ./secrets/fullchain.pem

install-zxpy:
	pip3 install --quiet zxpy

setup-vms:
	vagrant up && ./vagrant-hosts.py

rm-vms:
	./vagrant-hosts.py clean || vagrant halt


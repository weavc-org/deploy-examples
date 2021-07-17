
deploy:
	docker stack deploy -c compose-stack.yml deploy-examples

deploy-vm:
	docker -c m1 stack deploy -c compose-stack.yml deploy-examples

ssl:
	openssl req -newkey rsa:4096 -new -nodes -x509 -days 3650 -keyout ./secrets/privkey.pem -out ./secrets/fullchain.pem

install-zxpy:
	pip3 install --quiet zxpy

setup-vms:
	vagrant up && ./vagrant-hosts.py

rm-vms:
	./vagrant-hosts.py clean || vagrant halt


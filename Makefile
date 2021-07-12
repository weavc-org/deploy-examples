
setup:
	python3 -m pip install pipenv && pipenv install

deploy:
	docker stack deploy -c compose-stack.yml deploy-examples
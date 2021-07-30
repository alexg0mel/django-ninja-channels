up: down build
	docker-compose up

build:
	docker-compose build

down:
	docker-compose down

test:
	docker-compose exec app python manage.py test

help:
	cat ./Makefile

#c=<command>
run:
	docker-compose exec app python manage.py $(c)

perm:
	sudo chown -R alexgomel backend/
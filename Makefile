
.PHONY: up
up:
	docker-compose up -d

.PHONY: up-nod
up-nod:
	docker-compose up

.PHONY: down
down: 
	docker-compose down -v --remove-orphans


DOMAIN_NAME ?= localhost

DOCKER := docker-compose -p books-explorer
DOCKER_COMPOSE :=  $(DOCKER) --env-file .env_

BACKEND := Compose.Backend.yml
FRONTEND := Compose.Frontend.yml
PROXY := Compose.Proxy.yml

UP := -d --build

.PHONY: ssl-certificate example_data_extraction example __example_complement developer_data_extraction developer __dev_complement deploy_production down

ssl-certificate:
	mkdir -p Proxy/ssl/local_cert && \
	cd Proxy/ssl/local_cert && \
	openssl req -x509 -nodes -days 31 -newkey rsa:2048 \
		-keyout privkey.pem \
		-out fullchain.pem \
		-subj "/CN=$(DOMAIN_NAME)" \
		-addext "subjectAltName=DNS:${DOMAIN_NAME},DNS:localhost,IP:127.0.0.1"


example_data_extraction:
	$(DOCKER_COMPOSE)example --file $(BACKEND) up $(UP)
	$(MAKE) __example_complement

example:
	$(DOCKER_COMPOSE)example --file $(BACKEND) up BooksDatabase RecommenderSystem $(UP)
	$(MAKE) __example_complement

__example_complement:
	$(DOCKER_COMPOSE)example --file $(FRONTEND) up $(UP)
	$(DOCKER_COMPOSE)example --file $(PROXY) up Proxy $(UP)


developer_data_extraction:
	$(DOCKER_COMPOSE)dev --file $(BACKEND) up $(UP)
	$(MAKE) __dev_complement

developer:
	$(DOCKER_COMPOSE)dev --file $(BACKEND) up BooksDatabase RecommenderSystem $(UP)
	$(MAKE) __dev_complement

__dev_complement:
	$(DOCKER_COMPOSE)dev --file $(FRONTEND) up $(UP)
	$(DOCKER_COMPOSE)dev --file $(PROXY) up Proxy $(UP)


deploy_production:
	$(DOCKER_COMPOSE)prod --file $(BACKEND) up $(UP)
	$(DOCKER_COMPOSE)dev --file $(FRONTEND) up $(UP)
	$(DOCKER_COMPOSE)dev --file $(PROXY) up $(UP)


down:
	$(DOCKER) down
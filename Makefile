DOMAIN_NAME ?= localhost

DOCKER := docker-compose -p books-explorer
DOCKER_COMPOSE :=  $(DOCKER) --env-file .env_

BACKEND := Compose.Backend.yml
FRONTEND := Compose.Frontend.yml
PROXY := Compose.Proxy.yml

UP := up -d --build

.PHONY: ssl-certificate example_data_extraction example __example_complement developer_data_extraction developer __dev_complement deploy_production down down_volume

ssl-certificate:
	mkdir -p Proxy/ssl/local_cert && \
	cd Proxy/ssl/local_cert && \
	openssl req -x509 -nodes -days 31 -newkey rsa:2048 \
		-keyout privkey.pem \
		-out fullchain.pem \
		-subj "/CN=$(DOMAIN_NAME)" \
		-addext "subjectAltName=DNS:${DOMAIN_NAME},DNS:localhost,IP:127.0.0.1"


example_data_extraction:
	$(DOCKER_COMPOSE)example --file $(BACKEND) $(UP)
	$(MAKE) __example_complement

example:
	$(DOCKER_COMPOSE)example --file $(BACKEND) $(UP) BooksDatabase RecommenderSystem 
	$(MAKE) __example_complement

__example_complement:
	$(DOCKER_COMPOSE)example --file $(FRONTEND) $(UP)
	$(DOCKER_COMPOSE)example --file $(PROXY) $(UP) Proxy


developer_data_extraction:
	$(DOCKER_COMPOSE)dev --file $(BACKEND) $(UP)
	$(MAKE) __dev_complement

developer:
	$(DOCKER_COMPOSE)dev --file $(BACKEND) $(UP) BooksDatabase RecommenderSystem
	$(MAKE) __dev_complement

__dev_complement:
	$(DOCKER_COMPOSE)dev --file $(FRONTEND) $(UP)
	$(DOCKER_COMPOSE)dev --file $(PROXY) $(UP) Proxy


deploy_production:
	$(DOCKER_COMPOSE)prod --file $(BACKEND) $(UP)
	$(DOCKER_COMPOSE)dev --file $(FRONTEND) $(UP)
	$(DOCKER_COMPOSE)dev --file $(PROXY) $(UP)


down:
	$(DOCKER) down

down_volume:
	$(DOCKER) down -v
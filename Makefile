DOMAIN_NAME ?= localhost
ENV ?= example
LENGTH ?= 12

DOCKER := docker-compose -p books-explorer
DOCKER_COMPOSE :=  $(DOCKER) --env-file .env_

BACKEND := Compose.Backend.yml
FRONTEND := Compose.Frontend.yml
PROXY := Compose.Proxy.yml

UP := up -d --build

.PHONY: ssl_certificate secret_key pre_up pre_up_data_extraction dev dev_data_extraction deploy deploy_restart down down_volume
 
ssl_certificate:
	mkdir -p Proxy/ssl/live/$(DOMAIN_NAME) && \
	cd Proxy/ssl/live/$(DOMAIN_NAME) && \
	openssl req -x509 -nodes -days 31 -newkey rsa:2048 \
		-keyout privkey.pem \
		-out fullchain.pem \
		-subj "/CN=$(DOMAIN_NAME)" \
		-addext "subjectAltName=DNS:${DOMAIN_NAME}"

secret_key:
	openssl rand -base64 $(LENGTH) | tr -dc 'A-Za-z0-9' | head -c $(LENGTH) ; echo

pre_up:
	$(DOCKER_COMPOSE)$(ENV) --file $(BACKEND) $(UP)
	$(DOCKER_COMPOSE)$(ENV) --file $(FRONTEND) $(UP)

pre_up_data_extraction:
	$(DOCKER_COMPOSE)$(ENV) --file $(BACKEND) $(UP) BooksDatabase RecommenderSystem
	$(DOCKER_COMPOSE)$(ENV) --file $(FRONTEND) $(UP)

dev: pre_up
	$(DOCKER_COMPOSE)$(ENV) --file $(PROXY) $(UP) Proxy

dev_data_extraction: pre_up_data_extraction
	$(DOCKER_COMPOSE)$(ENV) --file $(PROXY) $(UP) Proxy

deploy: pre_up
	$(DOCKER_COMPOSE)$(ENV) --file $(PROXY) $(UP)

deploy_restart: pre_up_data_extraction
	$(DOCKER_COMPOSE)$(ENV) --file $(PROXY) $(UP) Proxy

down:
	docker compose -p books-explorer down

down_volume:
	docker compose -p books-explorer down -v
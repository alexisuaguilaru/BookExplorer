DOMAIN_NAME ?= localhost
ENV ?= example
LENGTH ?= 12

DOCKER := docker-compose -p books-explorer
DOCKER_COMPOSE :=  $(DOCKER) --env-file .env_

BACKEND := Compose.Backend.yml

UP_BUILD := up -d --build
UP := up -d

.PHONY: help secret_key deploy deploy_restart down down_volume

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

secret_key: ## Generate a Secrete Key
	openssl rand -base64 $(LENGTH) | tr -dc 'A-Za-z0-9' | head -c $(LENGTH) ; echo

deploy: ## Deploy API/Microservice 
	$(DOCKER_COMPOSE)$(ENV) --file $(BACKEND) $(UP_BUILD)

deploy_restart: ## Restart API/Microservice
	$(DOCKER_COMPOSE)$(ENV) --file $(BACKEND) $(UP) BooksDatabase RecommenderSystem

down: ## Stop API/Microservice without delete volumes
	$(DOCKER) down

down_volume: ## Stop API/Microservice and delete volumes
	$(DOCKER) down -v
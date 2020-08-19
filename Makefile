include .env

COMPOSER_DEV=docker-compose
IMAGE_REPO=$(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO_NAME)
IMAGE_TAG=$(IMAGE_REPO):$(shell date +'%Y%m%d')

nb-build:
	$(COMPOSER_DEV) build notebooks

nb-up:
	$(COMPOSER_DEV) up notebooks

be-build:
	$(COMPOSER_DEV) build backend

be-up:
	$(COMPOSER_DEV) up backend

be-bash:
	$(COMPOSER_DEV) run --service-ports backend bash


be-prod-build:
	docker build -t $(IMAGE_TAG) -f ./backend/Dockerfile ./

be-prod-push:
	aws ecr get-login-password --region $(AWS_REGION) | \
	docker login --username AWS --password-stdin $(IMAGE_REPO)
	docker push $(IMAGE_TAG)


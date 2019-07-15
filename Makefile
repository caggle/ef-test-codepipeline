ROOT_DIR	:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
AWS_REGION	:= 
AWS_PROFILE := 

ZOOM_TOKEN = ${ZTOKEN}

all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile

.SILENT: setup
.PHONY: setup
ifneq ($(ZOOM_TOKEN), )
  setup:
	export AWS_SDK_LOAD_CONFIG=true && \
	aws --profile $(AWS_PROFILE) ssm put-parameter --name "ZOOM_AUTH_TOKEN" \
	--value $(ZOOM_TOKEN) --type SecureString --overwrite
else
  $(error Zoom token is not specified)
endif

.PHONY: validate
validate: export AWS_SDK_LOAD_CONFIG=true
validate:
	sls deploy --noDeploy --region $(AWS_REGION) --aws-profile $(AWS_PROFILE)


.PHONY: deploy
deploy: export AWS_SDK_LOAD_CONFIG=true
deploy:
	npm install serverless-python-requirements --save-dev && \
	npm install serverless-pseudo-parameters --save-dev && \
	npm install serverless-prune-plugin --save-dev && \
	npm install serverless-domain-manager --save-dev
	sls deploy --region $(AWS_REGION) --aws-profile $(AWS_PROFILE)


.PHONY: flake8
flake8:
	flake8 ./*py
	flake8 handlers/*py
	flake8 core/*py
	flake8 tests/*py

.PHONY: clean
clean:
	find . -name .pytest_cache -type d -exec rm -rf {}\;
	find . -name __pycache__ -type d -exec rm -rf {}\;
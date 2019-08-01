ROOT_DIR		:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
LAMBDA_PACKAGE_CMD	:= docker run --rm \
	-e AWS_DEFAULT_REGION=us-west-2 \
	-v ${HOME}/.aws:/root/.aws \
	-v $(ROOT_DIR)/..:/var/task <IMAGE>

EF_MODULE_PATH	:= python-modules
PY_DIR			:= python/lib/python3.7/site-packages
PIP_CMD			:= pip install --upgrade
LAYER_NAME		:= mozdef-ef
STAGE			:= ${STAGE}
STAGE			:= $(if $(STAGE),$(STAGE),qa)
AWS_REGION		:= us-west-2
ZOOM_TOKEN      := ${ZTOKEN}


.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile
	@echo $(STAGE)


.PHONY:clean-layer
clean-layer:
	rm -rf $(ROOT_DIR)/layer/*
	rm -rf $(ROOT_DIR)/build/*
	rm -f $(ROOT_DIR)/mozdef-ef.zip


.SILENT:setup
.PHONY:setup
ifneq ($(ZOOM_TOKEN), )
  setup:
	aws --profile $(AWS_PROFILE) ssm put-parameter --name "/mozdef-event-framework/ZOOM_AUTH_TOKEN" \
	--value $(ZOOM_TOKEN) --type SecureString --overwrite
endif


.PHONY:layer
layer:
	$(LAMBDA_PACKAGE_CMD) \
	/bin/bash -c "\
	$(PIP_CMD) $(EF_MODULE_PATH)/custom_logger/ \
	$(EF_MODULE_PATH)/event/ \
	$(EF_MODULE_PATH)/response/ \
	ls /var/task/serverless-functions/build/ && \
	zip -r /var/task/serverless-functions/mozdef-ef.zip /var/task/serverless-functions/build/ && \
	aws lambda publish-layer-version \
	--layer-name $(LAYER_NAME)_$(STAGE) --compatible-runtimes python3.7 \
	--zip-file fileb:///var/task/serverless-functions/mozdef-ef.zip && \
	aws ssm put-parameter --name "/mozdef-event-framework/ZOOM_AUTH_TOKEN" \
	--value $(ZOOM_TOKEN) --type SecureString --overwrite


.PHONY: layer-codebuild
layer-codebuild:
	mkdir -p /tmp/build/$(PY_DIR)
	$(PIP_CMD) ../$(EF_MODULE_PATH)/custom_logger/ \
	../$(EF_MODULE_PATH)/event/ \
	../$(EF_MODULE_PATH)/response/ -t /tmp/build/$(PY_DIR)
	cd /tmp/build && zip -r /tmp/mozdef-ef.zip .
	aws lambda publish-layer-version \
	--layer-name $(LAYER_NAME)_$(STAGE) --compatible-runtimes python3.7 \
	--zip-file fileb:///tmp/mozdef-ef.zip
	

.PHONY:deploy-ingest-zoom
deploy-ingest-zoom:
	cd $(ROOT_DIR)/ingest-zoom && \
	npm install serverless-pseudo-parameters --save-dev && \
	npm install serverless-prune-plugin --save-dev && \
	sls deploy --region $(AWS_REGION) --stage $(STAGE)


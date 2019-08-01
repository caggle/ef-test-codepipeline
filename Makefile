ROOT_DIR	:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
AWS_REGION	:= 
AWS_PROFILE := 
STAGE			:= ${STAGE}
STAGE			:= $(if $(STAGE),$(STAGE),qa)

all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile


.PHONY: build
build:
	$(MAKE) -C serverless-functions layer-codebuild STAGE=$(STAGE)


.PHONY: release
release:
	$(MAKE) -C serverless-functions deploy-ingest-zoom STAGE=$(STAGE)

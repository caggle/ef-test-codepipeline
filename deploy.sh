#!/bin/bash

echo "Begin deploy MozDef Event Framework."
echo "$CODEBUILD_WEBHOOK_TRIGGER"

if [[ "branch/master" == "$CODEBUILD_WEBHOOK_TRIGGER" ]]
	then
		echo "Deploying the QA environment."
		make build STAGE=qa
		make release STAGE=qa
elif [[ "$CODEBUILD_WEBHOOK_TRIGGER" =~ ^tag\/[0-9]\.[0-9]\.[0-9](\-(prod))?$ ]]
	then
		echo "Deploying the production environment."
		make build STAGE=prod
		make release STAGE=prod
fi

echo "$CODEBUILD_WEBHOOK_TRIGGER"
echo "End deploy MozDef Event Framework."
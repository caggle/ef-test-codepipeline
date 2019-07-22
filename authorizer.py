import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def generate_policy(principalId, effect, resource):
    authResponse = {}
    authResponse['principalId'] = principalId
    if effect and resource:
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'].append(statementOne)
        authResponse['policyDocument'] = policyDocument

    return authResponse


def test(event, context):
    print(json.dumps(event))

    if 'authorizationToken' not in event:
        logger.error("No token, no auth!")
        return {
            'statusCode': 403,
            'body': json.dumps('Unauthorized.')
        }
    else:
        token = event['authorizationToken']
        if str(token).lower() == '112233445566':
            # Correct token
            logger.info("Correct token, you shall pass!")
            allow_response = generate_policy('zoom_webhook', 'Allow', event['methodArn'])
            return allow_response
        else:
            # Incorrect token
            logger.warning("Incorrect token, thou shalt not pass!")
            deny_response = generate_policy('zoom_webhook', 'Deny', event['methodArn'])
            return deny_response

    # Default response
    return {
        'statusCode': 403,
        'body': json.dumps('Unauthorized.')
    }

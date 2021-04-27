import boto3
import json
import pytest
import os
import boto3.session

from botocore.config import Config

def lambda_local(name):
    lambda_client = boto3.client('lambda',
                                        endpoint_url="http://127.0.0.1:3001",
                                        use_ssl=False,
                                        verify=False,
                                        config=Config(region_name = 'eu-west-2',
                                                    signature_version='v4',
                                                    read_timeout=10,
                                                    retries={'max_attempts': 3}))

    response = lambda_client.invoke(FunctionName=name)

    response_payload = json.loads(response['Payload'].read())["Response"]

    return response_payload


def test_lambda():
    data = lambda_local("rLambdaFunction")
    expected = "Sucessfully executed Scenario 1 Lambda!"
    assert data == expected

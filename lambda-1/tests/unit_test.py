import boto3
import botocore
import json
import pytest
import os

from botocore.config import Config

FunctionLogicalID = "rLambdaFunction"
ExpectedResponse = "Sucessfully executed Lambda-1!"

def lambda_local(FunctionLogicalID):
    lambda_client = boto3.client('lambda',
                                        endpoint_url="http://127.0.0.1:3001",
                                        use_ssl=False,
                                        verify=False,
                                        config=Config(region_name = 'eu-west-2',
                                                    signature_version=botocore.UNSIGNED,
                                                    read_timeout=1,
                                                    retries={'max_attempts': 0}))

    response = lambda_client.invoke(FunctionName=FunctionLogicalID)

    response_payload = json.loads(response['Payload'].read())["Response"]

    return response_payload

def test_lambda():
    data = lambda_local(FunctionLogicalID)
    assert data == ExpectedResponse

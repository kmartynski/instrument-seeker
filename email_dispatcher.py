import boto3
import json

from config import get_settings

settings = get_settings()


def send_email(results: dict):
    ses_client = boto3.client('ses', region_name="eu-central-1")
    CHARSET = "UTF-8"

    ses_client.send_email(
        Destination={
            "ToAddresses": [
                settings.email_address
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": json.dumps(results),
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "List of pianos from Ebay"
            }
        },
        Source=settings.email_address
    )


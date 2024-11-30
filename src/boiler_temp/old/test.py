from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')
table = dynamodb.Table('hometemp')

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

sensor = "3b-000000186e4a"
dt = "2018-01-01 09:22:03"

response = table.put_item(
   Item={
        'datetime': dt,
        'sensor' : sensor,
        'info': {
            'temperature': decimal.Decimal(118.5)
        }
    }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4, cls=DecimalEncoder))
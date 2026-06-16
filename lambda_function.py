import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter') # type: ignore

def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'id': 'counter'
        }
    )

    visitors = response['Item']['visitors']

    visitors += 1

    table.update_item(
        Key={
            'id': 'counter'
        },
        UpdateExpression='SET visitors = :v',
        ExpressionAttributeValues={
            ':v': visitors
        }
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"""
        <html>
        <head>
        <title>Visitor Counter</title>
        </head>

        <body style="
            font-family:Arial;
            text-align:center;
            padding-top:100px;
            background:beige;
        ">

            <h1>Website Visitor Counter</h1>

            <div style="
                font-size:60px;
                color:green;
                font-weight:bold;
            ">
                {int(visitors)}
            </div>

            <h3>Total Visitors</h3>

        </body>
        </html>
        """
    }
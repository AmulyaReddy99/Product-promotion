import boto3
from botocore.exceptions import ClientError

SENDER = "Starein <amulyareddyk97@gmail.com>"
AWS_REGION = "us-west-2"
CONFIGURATION_SET = "diligenceir"


def template_mail(RECIPIENTS,SUBJECT,NAME,INFO,pdf_link):
                
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1></h1>
      <p>Email alert!
        <div>
            """+NAME+"""
        </div>
        <div>
            """+INFO+"""
        </div>
        <a href='"""+pdf_link+"""'>This is a new update link to pdf</a>
      </p>
    </body>
    </html>
                """            

    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': RECIPIENTS,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            ConfigurationSetName=CONFIGURATION_SET,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


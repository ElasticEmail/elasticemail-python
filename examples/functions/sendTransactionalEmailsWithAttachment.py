import ElasticEmail
from pprint import pprint
import base64
from pathlib import Path

configuration = ElasticEmail.Configuration(
    host = "https://api.elasticemail.com/v4"
)

configuration.api_key['apikey'] = "YOUR_API_KEY"

with ElasticEmail.ApiClient(configuration) as api_client:
    api_instance = ElasticEmail.EmailsApi(api_client)

    invoice_path = Path(__file__).with_name("invoice.pdf")
    if not invoice_path.exists():
        print(f"Attachment file not found: {invoice_path}. Skipping send.")
        raise SystemExit(0)

    with open(invoice_path, 'rb') as file:
        binData = file.read()

    email_transactional_message_data = ElasticEmail.EmailTransactionalMessageData(
        Recipients=ElasticEmail.TransactionalRecipient(
            To=[
                "RECIPIENT@EMAIL.ADDRESS",
            ],
        ),
        Content=ElasticEmail.EmailContent(
            Body=[
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("HTML"),
                    Content="<strong>Mail content.<strong>",
                    Charset="utf-8",
                ),
                ElasticEmail.BodyPart(
                    ContentType=ElasticEmail.BodyContentType("PlainText"),
                    Content="Mail content.",
                    Charset="utf-8",
                ),
            ],
            From="SENDER@EMAIL.ADDRESS",
            ReplyTo="SENDER@EMAIL.ADDRESS",
            Subject="Example transactional email with attachment",
            Attachments=[
                ElasticEmail.MessageAttachment(
                    BinaryContent=base64.b64encode(binData).decode('utf-8'),
                    Name="Invoice.pdf"
                )
            ]
        ),
    )


    try:
        api_response = api_instance.emails_transactional_post(email_transactional_message_data)
        print("The response of EmailsApi->emails_transactional_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailsApi->emails_transactional_post: %s\n" % e)

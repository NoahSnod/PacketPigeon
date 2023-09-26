from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "EMPTY_FOR_PRIVACY_REASONS"
auth_token  = "EMPTY_FOR_PRIVACY_REASONS" 

client = Client(account_sid, auth_token)

totPackets = 100
threatPackets = 4

numbers_to_message = ["+19513845423"]
for number in numbers_to_message:
    client.messages.create (
        from_ = "+18557432796",
        to = number,
        body = "ALERT: Suspicious Network Traffic Detected\n\n" +
                str(threatPackets) + " packets out of " + str(totPackets) + " are suspected to be malicious" +
                "\n\nSuspect Ip Address: 192.168.0.1."
    )

# from google.colab import drive
# drive.mount('/content/gdrive/MyDrive', force_remount = True)

#CHOOSE FILE PATH
file_name = 'demo_count.csv'

import csv
import pandas as pd
from collections import defaultdict
from twilio.rest import Client

# df = pd.read_csv(file_name, usecols = ['parent', 'Count'])
# print(df)

with open(file_name) as file:
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        if index == 1:
            overall = int(row[3])
            print(overall)
        if index == 2:
            packets = int(row[3])
            print(packets)
        if index == 2:
            ip = str(row[2])
            print(ip)

percentVal = float(packets / overall)
print(percentVal)
badPacketPercent = float(percentVal * 100)
badPacketPercent = round(badPacketPercent, 2)
print(badPacketPercent)

if badPacketPercent >= 90:

    # Your Account SID and Auth Token from console.twilio.com
    account_sid = "AC60c650f80593372c40fec45c6bd1ecae"
    auth_token  = "a06100094ba29d7fc2bf973561e8bd2e"

    client = Client(account_sid, auth_token)

    totPackets = 100
    threatPackets = 4

    numbers_to_message = ["+19513845423", "+19095122449"]
    for number in numbers_to_message:
        client.messages.create (
            from_ = "+18557432796",
            to = number,
            body = "ALERT: Suspicious Network Traffic Detected\n\n" +
                    str(packets) + " packets out of " + str(overall) + " are suspected to be malicious" +
                    "\n\nSuspected IP Address: " + str(ip) + "\n\nThis means " + str(badPacketPercent) + 
                    "% of your traffic is potentially RISKY\n"
        )


# with open(file_name) as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         for (i, v) in row.items():
#             columns[i].append(v)
# print (columns[0])

# result = pandas.read_csv(file_name)


# print("\Before sorting:")
# print(result)


# result.sort_values(["Count"],
#                     axis=0,
#                     ascending=[False],
#                     inplace=True)

# print("\nAfter sorting:")
# print(result)

# for row in result:
#     content = list(row[i] for i in included_cols)
#     print(content)

# largePacketSend = result[]

    






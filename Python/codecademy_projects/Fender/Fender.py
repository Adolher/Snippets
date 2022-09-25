import csv
import os
import sys
import json

slash_null_sig = "signature"

compromised_users = []
with open(os.path.join(sys.path[0], "passwords.csv")) as pw_f:
    pw_csv = csv.DictReader(pw_f)
    for row in pw_csv:
        compromised_users.append(row)
        print(row)

with open(os.path.join(sys.path[0], "compromised_users.txt"), "w") as com_user_file:
    for user in compromised_users:
        com_user_file.write(user["Username"])

with open(os.path.join(sys.path[0], "boss_message.json"), "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

with open(os.path.join(sys.path[0], "new_passwords.csv"), "w") as new_passw_obj:
    new_passw_obj.write(slash_null_sig)

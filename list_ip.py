import requests
import json


try:
    with open("./CF_dns_manager/user_id.json", "r") as json_file:
        user_data = json.load(json_file)

    email = user_data["email"]
    api_token = user_data["api_token"]
    zone_id = user_data["zone_id"]
    domain = user_data["domain"]
    dns_record_name = user_data["dns_record_name"]
    print("=====================================")
except:
    print("=====================================")
    user_data = {
        "email": input("Enter your email (example@gmail.com):"),
        "api_token": input("Enter your api_token (xxxxxxxxxxxx):"),
        "zone_id": input("Enter zone_id (xxxxxxxxxxxx):"),
        "domain": input("Enter your Domain (example.com):"),
        "dns_record_name": input("Enter DNS record name:")
    }
    with open("user_id.json", "w") as json_file:
        json.dump(user_data, json_file)
                                                                # reread data!
    with open("user_id.json", "r") as json_file:
        user_data = json.load(json_file)

    email = user_data["email"]
    api_token = user_data["api_token"]
    zone_id = user_data["zone_id"]
    domain = user_data["domain"]
    dns_record_name = user_data["dns_record_name"]
    print("=====================================")

url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'


headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_token,
    'Content-Type': 'application/json'
}
response = requests.request('GET', url, headers=headers
)
data = response.json()['result']

i_num = 0
for i in range(len(data)):
    sub_domain = data[i]['name']
    this_domain = data[i]['zone_name']
    this_dns_record = sub_domain.replace(f".{this_domain}", "")
    if this_dns_record == dns_record_name:
        content = data[i]['content']
        i_num += 1
        print(f"{i_num}) {sub_domain}: {content}")
print(f"Total IPs: {i_num}")
print("=====================================")
print("github: https://github.com/ImanMontajabi/CF_dns_manager")
print("twitter: https://twitter.com/imanmontajabi")
print("=====================================")

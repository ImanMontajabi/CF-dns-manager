import requests
import json

def listip():
    with open("./CF_dns_manager/user_id.json", "r") as json_file:
        user_data = json.load(json_file)

    email = user_data["email"]
    api_token = user_data["api_token"]
    zone_id = user_data["zone_id"]
    dns_record_name = user_data["dns_record_name"]
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
    "X-Auth-Email": email,
    "X-Auth-Key": api_token,
    "Content-Type": "application/json"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()["result"]
    ip = []
    for i in range(len(data)):
        sub_domain = data[i]["name"]
        this_domain = data[i]["zone_name"]
        this_dns_record = sub_domain.replace(f".{this_domain}", "")
        if this_dns_record == dns_record_name:
            ip.append(data[i]["content"])
    return ip

# ====================================================================
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
    with open("./CF_dns_manager/user_id.json", "w") as json_file:
        json.dump(user_data, json_file)
                                                                # reread data!
    with open("user_id.json", "r") as json_file:
        user_data = json.load(json_file)

params_name = f'{user_data["dns_record_name"]}.{user_data["domain"]}'
url = f'https://api.cloudflare.com/client/v4/zones/{user_data["zone_id"]}/dns_records'
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": user_data["email"],
    "X-Auth-Key": user_data["api_token"]
}
params = {
    "name": params_name,
    "per_page": 100
}
response = requests.get(url, headers=headers, params=params)
dns_records = response.json()['result']
iplist = listip()
dns_record_name = user_data["dns_record_name"]
domain = user_data["domain"]
i_num = 0
for ip in iplist:
    for dns_record in dns_records:
        if dns_record['content'] == ip:
            i_num += 1
            url_del = f"{url}/{dns_record['id']}"
            response = requests.delete(url_del, headers=headers)
            print(f"{i_num}){dns_record_name}.{domain}: {dns_record['content']}\t deleted")
print(f"Total delted IPs: {i_num}")
            
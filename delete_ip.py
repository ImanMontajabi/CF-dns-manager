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
    with open("./CF_dns_manager/user_id.json", "w") as json_file:
        json.dump(user_data, json_file)
                                                                # reread data!
    with open("./CF_dns_manager/user_id.json", "r") as json_file:
        user_data = json.load(json_file)
    print("=====================================")
email = user_data["email"]
api_token = user_data["api_token"]
zone_id = user_data["zone_id"]
domain = user_data["domain"]
dns_record_name = user_data["dns_record_name"]
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
"X-Auth-Email": email,
"X-Auth-Key": api_token,
"Content-Type": "application/json"
}
page_num = 1
dns_records = []
i_num = 0    
while True:
    params = {"page": page_num,"per_page": 100}
    response = requests.request("GET", url, headers=headers, params=params)
    data = response.json()["result"]
    if not data:
        break

    for record in data:
        if record["name"] == f"{dns_record_name}.{domain}":
            url_del = f"{url}/{record['id']}"
            requests.delete(url_del, headers=headers)
            i_num += 1
            print(f"{i_num}){dns_record_name}.{domain}: {record['content']}  deleted")    
    page_num += 1
print(f"Total delted IPs: {i_num}")
print("=====================================")
print("github: https://github.com/ImanMontajabi/CF_dns_manager")
print("twitter: https://twitter.com/imanmontajabi")
print("=====================================")
import requests
import json

def listip():
    with open('user_id.json', 'r') as json_file:
        user_data = json.load(json_file)

    email = user_data['email']
    api_token = user_data['api_token']
    zone_id = user_data['zone_id']
    ip_name = user_data["ip_dns_record"]
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_token,
    'Content-Type': 'application/json'
    }
    response = requests.request('GET', url, headers=headers)
    data = response.json()['result']
    ip = []
    for i in range(len(data)):
        a = data[i]['name']
        b = data[i]['zone_name']
        c = a.replace(f".{b}", "")
        if c == ip_name:
            ip.append(data[i]['content'])
    return ip

# ====================================================================
with open('user_id.json', 'r') as json_file:
    user_data = json.load(json_file)
email = user_data['email']
api_token = user_data['api_token']
zone_id = user_data['zone_id']
ip_name = user_data["ip_dns_record"]
params_name = f'{user_data["ip_dns_record"]}.{user_data["domain"]}'
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": email,
    "X-Auth-Key": api_token
}
params = {
    "name": params_name,
    "per_page": 100
}
response = requests.get(url, headers=headers, params=params)
dns_records = response.json()['result']
iplist = listip()
for ip in iplist:
    for dns_record in dns_records:
        if dns_record['content'] == ip:
            url_del = f"{url}/{dns_record['id']}"
            response = requests.delete(url_del, headers=headers)
            print(response.text)
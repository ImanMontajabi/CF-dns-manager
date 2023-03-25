import requests
import json

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
response = requests.request('GET', url, headers=headers
)
data = response.json()['result']

i_num = 0
for i in range(len(data)):
    a = data[i]['name']
    b = data[i]['zone_name']
    c = a.replace(f".{b}", "")
    if c == ip_name:
        content = data[i]['content']
        id = data[i]['id']
        i_num += 1
        print(f"{c}({i_num}): {content} \t id: {id}")
print(f"Total IPs: {i_num}")
print("github: https://github.com/ImanMontajabi/CF_dns_manager/blob/main/requirements.txt")

import requests
import json
import re


max_ips = 100
try:
    with open("./CF_dns_manager/user_id.json", "r") as json_file:
        data = json.load(json_file)
    json_file.close()
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
    json_file.close()
                                                                         # reread data!
    with open("./CF_dns_manager/user_id.json", "r") as json_file:
        user_data = json.load(json_file)
    json_file.close()

# ============= change scan.json from morteza bashsiz's app to ip.txt =================
def scan_to_iplist():
    f = open('./CF_dns_manager/scan.json')
    data = json.load(f)
    ip_list = [i['ip'] for i in data['workingIPs']]
    f.close()
    return ip_list
def linux_scan_to_iplist():
    with open('./CF_dns_manager/scan.cf', 'r') as f:
        data = f.readlines()
    ips = []

    # iterate over the list items
    for item in data:
    # extract the IP using regular expression
        result = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', item)
    # check if IP is found and add to the list
        if result:
            ips.append(result.group(0))
    return ips

def iplist_to_iptext():
    try:
        iplist = scan_to_iplist()
    except:
        iplist = linux_scan_to_iplist()
    with open('./CF_dns_manager/ip.txt', 'w') as f:
            f.write('\n'.join(iplist))
iplist_to_iptext()
# ================= Read ip.txt =======================
def ip_list():
    with open ('./CF_dns_manager/ip.txt', 'r') as f:
        myip = [line.strip() for line in f]
        f.close()
        return myip
# ================= put best 100 ip to bestip.txt =====================
all_ips = ip_list()
lenscan = len(all_ips)

def bestip():
    ipn = 0
    filename = "./CF_dns_manager/best_ip.txt"
    topUnder100ip = []
    while(ipn < lenscan):
        topUnder100ip.append(all_ips[ipn])
        ipn += 1
        if ipn >= max_ips:
            break
    with open(filename, "w") as f:
        f.write("\n".join(topUnder100ip))
    f.close()
bestip()
# ============ create dns records ===============
with open("./CF_dns_manager/best_ip.txt", "r") as ip:
    ilist = ip.readlines()
with open('./CF_dns_manager/user_id.json', 'r') as json_file:
    user_data = json.load(json_file)
email = user_data['email']
api_token = user_data['api_token']
zone_id = user_data['zone_id']
domain = user_data['domain']
ip_name = user_data["dns_record_name"]
params_name = f'{user_data["dns_record_name"]}.{user_data["domain"]}'
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_token
    }
ipn = 0
print("=====================================")
while (ipn < lenscan):
    data = {
        "type": "A",
        "name": params_name,
        "content": f"{ilist[ipn].strip()}",
        "ttl": 1,
        "proxied": False
    }
    ipn += 1
    response = requests.post(url, headers=headers, json=data)
    if (response.status_code == 200):
        print(f"{ipn}){response.json()['result']['name']}: {response.json()['result']['content']} added")
        ipn += 1
    else:
        print(f"{ipn}){ip_name}.{domain}: {ilist[ipn].strip()}  already exist")
        ipn += 1
    if ipn > max_ips:
        break
print(f"Total IPs: {ipn}")
print("=====================================")
print("github: https://github.com/ImanMontajabi/CF_dns_manager")
print("twitter: https://twitter.com/imanmontajabi")
print("=====================================")
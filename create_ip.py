import requests
import json

# ============= change scan.json from morteza bashsiz's app to ip.txt =================
def scan_to_iplist():
    f = open('scan.json')
    data = json.load(f)
    ip_list = [i['ip'] for i in data['workingIPs']]
    f.close()
    return ip_list
iplist = scan_to_iplist()
def iplist_to_iptext(iplist):
    with open('ip.txt', 'w') as f:
            f.write('\n'.join(iplist))
# ================= Read ip.txt =======================
def ip_list():
    with open ('ip.txt', 'r') as f:
        myip = [line.strip() for line in f]
        f.close()
        return myip
# ================= put best 100 ip to bestip.txt =====================
def bestip():
    filename = "best_ip.txt"
    top100ip = []
    for i in range(100):
        top100ip.append(ip_list()[i])
    try:    
        with open(filename, "r") as f:
            lines = f.readlines()
            print(f"cuurent IPs: {len(lines)}")
            if len(lines) >= 100:
                print("Maximum number of lines is 100!")
            else:
                    with open(filename, "a") as f:
                        if len(lines) == 0:
                            f.write("\n".join(top100ip))
                        else:
                            f.write("\n")
                            f.write("\n".join(top100ip))
    except:
            with open(filename, "w") as f:
                f.write("\n".join(top100ip))
    f.close()
# ============ create dns records ===============
with open("best_ip.txt", "r") as ip:
    ilist = ip.readlines()
with open('user_id.json', 'r') as json_file:
    user_data = json.load(json_file)
email = user_data['email']
api_token = user_data['api_token']
zone_id = user_data['zone_id']
ip_name = user_data["ip_dns_record"]
params_name = f'{user_data["ip_dns_record"]}.{user_data["domain"]}'
url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_token
    }
for i in range(100):
    data = {
        "type": "A",
        "name": params_name,
        "content": f"{ilist[i]}",
        "ttl": 1,
        "proxied": False
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)
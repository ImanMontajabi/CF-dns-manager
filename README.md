# CF_dns_manager
:smile: create delete list DNS records in Cloudflare
========================
For using this script, you will need following requirements:
1. [install python](https://www.python.org/downloads/) >= 3.9
2. create a new folder for project
3. clone this script [link](https://github.com/ImanMontajabi/CF_dns_manager.git) or [download](https://github.com/ImanMontajabi/CF_dns_manager/archive/refs/heads/main.zip) in your folder
4. enter your information in user_id.json
5. copy result (.json file) from [Morteza Bashsiz](https://github.com/MortezaBashsiz/CFScanner) script/ app and paste in your folder
6. rename it to scan.json
7. open CMD (for windows users) locate your folder
8. follow the commands:
```python
python -m venv venv
```
9. locate to ...\venv\Scripts
10. in CMD:
```cmd
.\activate.bat
```
after activate your venv install 'requests' library:
```python
pip install requests
```

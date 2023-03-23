# CF_dns_manager
![icons8-orange-48](https://user-images.githubusercontent.com/52942515/227340008-faeeb65b-507e-40cf-b3a7-fd740ee38cb9.png) create delete list DNS records in Cloudflare
========================
For using this script, you will need following requirements:
1. [install python](https://www.python.org/downloads/) >= 3.9 :bangbang: add python to your PATH :bangbang:
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
10. for activate type in CMD:
```cmd
.\activate.bat
```
11. for deactivate type in CMD
```cmd
.\deactivate.bat
```
12. after activate your venv install 'requests' library:
```python

pip install requests
```
13. locate to your project folder in CMD 

:running_man: run create_ip.py:
```python
python create_ip.py
```
:running_man: run list_ip.py
```python
python list_ip.py
```
:running_man: run delete_ip.py
```python
python delete_ip.py
```

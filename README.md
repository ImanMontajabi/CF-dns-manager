# ![icons8-orange-48](https://user-images.githubusercontent.com/52942515/227340008-faeeb65b-507e-40cf-b3a7-fd740ee38cb9.png) Cloudflare DNS Record Manager

This Python script allows you to create, list, and delete DNS records in Cloudflare. It is designed to work with Python 3.6 or higher and requires the requests library.
# Dependencies

- [python](https://www.python.org/downloads/) (version 3.6 or higher)
- Libraries
  - `requests`

# Installation and Setup
1. Install Python 3.6 or higher if you haven't already.
2. Create a new folder for the project.
3. Clone the 1CF_dns_manager1 repository into your project folder:
```cmd
git clone https://github.com/ImanMontajabi/CF_dns_manager.git
```
4. Edit the user_id.json file with your Cloudflare account-related information.
5. Obtain a scan.json file from Morteza Bashsiz script/ app that contains your Cloudflare DNS scan data. Save it to your project folder.
6. Open a command prompt or terminal window and navigate to your project folder.
7. Create a Python virtual environment by running:





For using this script, you will need following requirements:
1. [install python](https://www.python.org/downloads/) (version 3.6 or higher) :bangbang: add python to your PATH :bangbang:
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

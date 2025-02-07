import requests
version = 0

txturl = 'https://raw.githubusercontent.com/BONGO-BYTES/update/refs/heads/main/update.txt'
pyurl = 'https://raw.githubusercontent.com/BONGO-BYTES/update/refs/heads/main/update.py'

py = requests.get(py)
txt = requests.get(txturl)


updateFile = link.text
if int(updateFile) > version:
    with open('update.py', 'w') as file:
      file.write(py)
      
else:
    print('No update found')

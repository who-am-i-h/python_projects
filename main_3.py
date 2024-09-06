import subprocess
shell_output = (subprocess.getoutput("netsh wlan show profile"))

# print(shell_output, type(shell_output))

output_lst = shell_output.splitlines()

ssid = []


for items in output_lst:
    if items.startswith("    All"):
        a = items.replace("    All User Profile     : ", "")
        ssid.append(a)
    else:
        pass
# print(ssid)
password_dict = {}
for item in ssid:
    password_raw_output = subprocess.getoutput(f'netsh wlan show profile "{item}" key = clear ')
    password_raw_output = password_raw_output.splitlines()
    for i in password_raw_output:
        if i.startswith("    Key Content"):
            password = i.replace("    Key Content            : ", "")
            password_dict.setdefault(item, password)
print(password_dict)            


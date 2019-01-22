import subprocess as sp
a = sp.check_output('netsh wlan show profiles').decode('utf-8')
a = a.split('\n')
a = [i.split(':')[1][1:-1]for i in a if 'All User Profile' in i]

for profile in a:    
    results = sp.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(profile, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(profile, ""))
import nmap 


nm = nmap.PortScanner() 
"""
cidr2='127.0.0.1/24'

a=nm.scan(hosts=cidr2, arguments='-sP') 

for k,v in a['scan'].items(): 
    if str(v['status']['state']) == 'up':
        #print(str(v))
        try:    print(str(v['addresses']['ipv4']) + ' => ' + str(v['addresses']['mac']))
   except: print('k')  #print(str(v['addresses']['ipv4']))
"""

nm.scan('192.168.0.0/24', arguments='-O')
for h in nm.all_hosts():
    print("k")
    print(nm[h])
    if 'mac' in nm[h]['addresses']:
        print(nm[h]['addresses'], nm[h]['vendor'])


import subprocess

def mac_addresses():
    subprocess.check_output(['arp','--all'])
    output = subprocess.check_output(['arp','-a'])
    '''
    ? (192.168.0.1) at d4:5:98:11:a2:97 on en0 ifscope [ethernet]
    ? (192.168.0.9) at 8:d4:c:70:f8:8c on en0 ifscope [ethernet]
    ? (192.168.0.13) at a4:5e:60:c6:a7:ef on en0 ifscope permanent [ethernet]
    ? (192.168.0.17) at b8:27:eb:71:15:52 on en0 ifscope [ethernet]
    ? (192.168.0.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
    ? (224.0.0.251) at 1:0:5e:0:0:fb on en0 ifscope permanent [ethernet]
    ? (239.255.255.250) at 1:0:5e:7f:ff:fa on en0 ifscope permanent [ethernet]
    broadcasthost (255.255.255.255) at ff:ff:ff:ff:ff:ff on en0 ifscope [ethernet]
    '''

    #split the output by each line
    lines = output.split('\n')
    lines = lines[0:-1]
    mac_addresses = []

    #loop through each line of the output
    for line in lines:
        #notice that on each output line, the information is split by a space.
        #we can split each line by a space to get that information
        print(line)
        tokens = line.split(' ')
        
        #the mac address on each line is the 4th element
        mac_addresses.append(tokens[3])
    return mac_addresses

mac_addresses()

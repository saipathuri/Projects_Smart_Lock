from time import sleep
import savedData
import servo

should_be_open = False
is_open = False

def main():
    savedData.clearDB()
    savedData.sendMacIntoDB()
    wlst = savedData.get_all_WhiteList()
    adrs = savedData.get_all_Addresses()
    
    for w in wlst:
        if w[1] in adrs:
            print('working')
            print(str(w[1]) + ' ' + str(adrs)) 
            should_be_open = True
        else:
            should_be_open = False
    
    if should_be_open:
        servo.unlock()
        sleep(10)
    else:
        servo.lock()
        
    

if __name__ == "__main__":
    servo.lock()
    print(True)
    sleep(5)
    while(True):
        main()
    

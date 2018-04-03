import savedData
import servo

should_be_open = False
is_open = False

def main():
    wlst = savedData.get_all_WhiteList()
    adrs = savedData.get_all_Addresses()
    for w in wlst:
        print(w)
        if w[1] in adrs:
            print('working')
            servo.unlock()
        else:
            servo.lock()

if __name__ == "__main__":
    servo.clean_up()
    while(True):
        main()
    

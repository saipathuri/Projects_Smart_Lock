import savedData
import servo

should_be_open = False
is_open = False

if __name__ == "__main__":
    wlst = savedData.get_all_WhiteList()
    adrs = savedData.get_all_Addresses()
    for w in wlst:
        #print(w)
        if w[1] in adrs:
            servo.unlock()
        else:
            servo.lock()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time


class oderwork(object):
    orderinfo = {}
    errinfo = {}
    def __init__(self):
        super().__init__()
        #self.browserinit()

    def gettime(self):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        return t


    def browserinit(self):          
        #set options
        brower_options = Options()
        #use headless driver
        brower_options.add_argument('--headless')
        brower_options.add_argument('--disable-gpu')
        #ignore errors
        brower_options.add_argument('--ignore-certificate-errors')
        brower_options.add_argument('--ignore-ssl-errors')

        print('Login...')

        self.browser = webdriver.Chrome(chrome_options=brower_options) #use chrome
        try:
            self.browser.get('https://store.t.com/')
        except Exception as e:
            print(e)
            self.errinfo[self.gettime()] = e
            print('Tool could not work properly, please send error messages above to yuanming.')

    def accountlogin(self, *list):
        #self.browser.get('website')
        if list == ():
            self.browser.get('https://store.t.com/login.aspx')
            with open('cookies.json','r') as f:
                ck = json.load(f) #load json file
        else:
            ck = list[0] #get parameters from tuple list
        """
        for i in ck:
            #print(i)
            self.browser.add_cookie(i) #add cookie, be aware of that i must be a dict.
        """
        self.setcookie(ck)
        time.sleep(1)

        self.browser.refresh()

        time.sleep(1)

    
        if self.browser.find_element_by_xpath("//*[contains(@href,'http://store.t.com/Logout.aspx')]"):
            print('Login completed.')
            msg = 'Login completed.'
        else:
            print('Login failed.')
            msg = 'Login failed'
        return msg
    
    #cookie must be cookie json data
    def setcookie(self, cookie):
        for i in cookie:
            #print(i)
            self.browser.add_cookie(i) #add cookie, be aware of that i must be a dict.

        
    #check if num meets the requirement
    def isnum(self, num):
        if num.isdigit():
            if len(num) == 7:
                print('Valid: Order number is {}'.format(num))
                return True
            else:
                print('Invalid: Order number must be 7 digits!')
                return False
        else:
            print('Invalid: Only digits are allowed!')
            return False

    #split order list by ',' add remove those doesn't confirm to order rule.
    def splitorder(self, list):
        newlist = list.split(',')
        for i in newlist:
            if self.isnum(i) == False:
                newlist.remove(i)
        return newlist
    #make a order list
    def getorderlist(self, list):
        orderlist = []
        for i in list:
            j = "https://store.t.com/members/endcustomervalidation.aspx?ordernumber=" + str(i)
            orderlist.append(j)
        return orderlist

    def acceptorder(self, list):
        acceptinfo = {}
        for i in list:
            o = i[-7:] #get 7 digital number from string
            acceptinfo[o] = self.getorderpage(i)
        return acceptinfo

    #request order page and aceep order, order parameter must be an url, browser must be a webdriver object
    def getorderpage(self, order):    
        browser = self.browser    
        browser.get(order)
        #print('get url_order')
        time.sleep(1)

        #show order status if order has been accepted/rejected
        title = browser.title
        if title == 'End Customer Validation':   

            agree = browser.find_element_by_id("ctl00_ctl00_NestedMaster_PageContent_ctl00_rblAgreeToTerms_0")
            agree.click()

            accept = browser.find_element_by_id("ctl00_ctl00_NestedMaster_PageContent_ctl00_btnAccept")
            accept.click()
            time.sleep(1)

            statustwo = browser.find_element_by_xpath("//*[@id='ctl00_ctl00_NestedMaster_PageContent_ctl00_reviewPage']/div[1]/div[2]/h3")
            print(str(statustwo.text))      
            
            #browser.close()
            return str(statustwo.text)
            #exit()

        else:
            status = browser.find_element_by_xpath("//*[@id='ctl00_ctl00_NestedMaster_PageContent_ctl00_lblAcceptedOOrRejectedOrder']")
            print(title + ": " + status.text)

            #if 'Order Already Accepted' in status.text:
                #browser.close()
                #print('close browser')
            
            return str((title + ": " + status.text))

    def quit(self):
        self.browser.quit()
            



"""

time.sleep(1)
while True:
    ordernumber = input("Please input order number:")
    if isnum(ordernumber):
        print('Order validation application starts...')
        break

url_order = "https://store.t.com/members/endcustomervalidation.aspx?ordernumber=" + str(ordernumber)
 


browser.get(url_order)
#print('get url_order')
time.sleep(1)

#show order status if order has been accepted/rejected

title = browser.title
if title == 'End Customer Validation':   

    agree = browser.find_element_by_id("ctl00_ctl00_NestedMaster_PageContent_ctl00_rblAgreeToTerms_0")
    agree.click()

    accept = browser.find_element_by_id("ctl00_ctl00_NestedMaster_PageContent_ctl00_btnAccept")
    accept.click()
    time.sleep(1)

    statustwo = browser.find_element_by_xpath("//*[@id='ctl00_ctl00_NestedMaster_PageContent_ctl00_reviewPage']/div[1]/div[2]/h3")
    print(str(statustwo.text))
    
    browser.close()
    print('Exit')
    exit()

else:
    status = browser.find_element_by_xpath("//*[@id='ctl00_ctl00_NestedMaster_PageContent_ctl00_lblAcceptedOOrRejectedOrder']")
    print(title + ": " + status.text)
    print('Check order number!')


    if 'Order Already Accepted' in status.text:
        browser.close()
        print('Exit')
        exit()
        """

if __name__ == '__main__':
    work = oderwork()
    work.browserinit()
    work.accountlogin()
    num = input('Pleast input order number: ')
    n = []
    n.append(num)
    t = work.getorderlist(n)
    print(t)
    work.acceptorder(t)













# coding=utf-8
import time, bs4
from selenium import webdriver
import requests

def go(username, pwd):
    weblocation = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=780038201&target=top&proxy_url=https%3A%2F%2Fpassport.book.qq.com%2Findex.php%2Findex%2Fproxy.html&s_url=https%3A%2F%2Fpassport.book.qq.com%2Findex%2Flogin.html%3Ftype%3Dqq%26site%3Dchuangshi%26sid%3Dqq3i47lud4heuio6qj3ajqliq1%26http_referer%3Dlocal'
    b.get(weblocation)
    #r = requests.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=780038201&target=top&proxy_url=https%3A%2F%2Fpassport.book.qq.com%2Findex.php%2Findex%2Fproxy.html&s_url=https%3A%2F%2Fpassport.book.qq.com%2Findex%2Flogin.html%3Ftype%3Dqq%26site%3Dchuangshi%26sid%3Dqq3i47lud4heuio6qj3ajqliq1%26http_referer%3Dlocal')
    #r.encoding = 'utf-8'
    #print(r.text)
    print('Initailization Complete')
    b.find_element_by_id('switcher_plogin').click()
    b.find_element_by_id('u').send_keys(username)
    b.find_element_by_id('p').send_keys(pwd)
    time.sleep(0.5)
    b.find_element_by_id('login_button').click()
    time.sleep(10)
    print('Prepared to login')
    while True:
        print(b.current_url)
        if 'chuangshi.qq.com' in b.current_url:
            break
        # if '安全验证' in b.page_source:
        #     print('Succeeded in Verification')
        #     print("I'm awake now!!!")
        #     time.sleep(2)
        #     print("Later: "+b.current_url)
        #     b.save_screenshot("myscreen.png")
        #     b.switch_to.frame(b.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe'))
        #     # print(b.page_source)
        #     print('ok')
        #     time.sleep(3)
        #     image_url = b.find_element_by_xpath('//*[@id="capImg"]').get_attribute('src')
        #     # imageurl = bs4.BeautifulSoup(b.page_source, 'html.parser').find(id="capImg")['src']
        #     print(image_url)
        #     r = requests.get(image_url)
        #     with open("hahaha.jpg", "wb") as img:
        #         img.write(r.content)
        #     b.find_element_by_id('capAns').send_keys(input())
        #     b.find_element_by_class_name('btn_verify').click()

        time.sleep(1)

    #while 'chuangshi' not in b.current_url:
    #    time.sleep(1)
    #time.sleep(1)
    # WebDriverWait(b, 500).until(EC.presence_of_element_located((By.ID, "user_center")))
    print('Login Success')
    b.find_element_by_class_name('user_center').click()
    # b.get('http://account.book.qq.com/usercenter/index.html')
    try:
        b.find_element_by_xpath("//a[@title='签到']").click()
        print('Task 1 Complete')
    except Exception:
        print('Task 1 Failure (Already done?)')
    time.sleep(2)
    b.get('http://account.book.qq.com/userfavorite/index.html')
    el = bs4.BeautifulSoup(b.page_source, 'html.parser').find(attrs={"id": "bookListByBookshelf"})\
        .find_all(attrs={"class": "green"})
    print('Initialization Complete')
    for x in el:
        gogo(x['href'])


def gogo(href):
    b.get(href)
    time.sleep(2)
    b.find_element_by_class_name('btnTuijian').click()
    time.sleep(2)
    b.find_element_by_class_name('confirm').click()
    print('Recommendation Complete')
    # b.execute_script('submitRecommend;')
    time.sleep(2)

b = webdriver.PhantomJS()
b.implicitly_wait(10)
go('2435534588', 'wangjiahao')
print("hahaha!")
b.quit()
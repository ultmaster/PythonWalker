# coding=utf-8
import time, bs4
from selenium import webdriver


def go(username, pwd):
    b.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=780038201&target=top&proxy_url=https%3A%2F%2Fpassport.book.qq.com%2Findex.php%2Findex%2Fproxy.html&s_url=https%3A%2F%2Fpassport.book.qq.com%2Findex%2Flogin.html%3Ftype%3Dqq%26site%3Dchuangshi%26sid%3Dqq3i47lud4heuio6qj3ajqliq1%26http_referer%3Dlocal')
    #r = requests.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=780038201&target=top&proxy_url=https%3A%2F%2Fpassport.book.qq.com%2Findex.php%2Findex%2Fproxy.html&s_url=https%3A%2F%2Fpassport.book.qq.com%2Findex%2Flogin.html%3Ftype%3Dqq%26site%3Dchuangshi%26sid%3Dqq3i47lud4heuio6qj3ajqliq1%26http_referer%3Dlocal')
    #r.encoding = 'utf-8'
    #print(r.text)
    b.find_element_by_id('switcher_plogin').click()
    b.find_element_by_id('u').send_keys(username)
    b.find_element_by_id('p').send_keys(pwd)
    b.find_element_by_id('login_button').click()
    #while 'chuangshi' not in b.current_url:
    #    time.sleep(1)
    #time.sleep(1)
    # WebDriverWait(b, 500).until(EC.presence_of_element_located((By.ID, "user_center")))
    b.find_element_by_class_name('user_center').click()
    # b.get('http://account.book.qq.com/usercenter/index.html')
    try:
        b.find_element_by_xpath("//a[@title='签到']").click()
        print('签到成功')
    except Exception:
        print('签到失败')
    # time.sleep(5)
    b.get('http://account.book.qq.com/userfavorite/index.html')
    el = bs4.BeautifulSoup(b.page_source, 'html.parser').find(attrs={"id": "bookListByBookshelf"})\
        .find_all(attrs={"class": "green"})
    for x in el:
        gogo(x['href'])


def gogo(href):
    b.get(href)
    time.sleep(5)
    b.find_element_by_class_name('btnTuijian').click()
    time.sleep(2)
    b.find_element_by_class_name('confirm').click()
    print('推荐票完成')
    # b.execute_script('submitRecommend;')
    time.sleep(3)

b = webdriver.PhantomJS()
b.implicitly_wait(10)
go('2435534588', 'wangjiahao')
print("hahaha!")
b.quit()
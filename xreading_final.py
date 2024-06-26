from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import winsound
import random


# use to login in xreading

def login(student_id):
    time.sleep(3)
    # find username buttom
    target = browser.find_element(By.XPATH,'//*[@id="username"]').send_keys(student_id + '@o365.fcu.edu.tw')
    # find pwd buttom
    target = browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(student_id)
    # find login buttom
    target = browser.find_element(By.XPATH,'//*[@id="loginbtn"]')
    target.click()


# find the last time book the user have saw and keep read it

def keep_read():
    target = WebDriverWait(browser,5).until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="region-main"]/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/a')))
    target.click()


# scroll the page

def scroll(stage):
    if(stage % 2 != 0 ):
        height = stage * 200
    else:
        height = stage * 10
    js=f"var q=document.documentElement.scrollTop={height}"  
    browser.execute_script(js)
    print(f"scroll this page {stage} times")
# wait some time and trun page
def wait_and_page_turn(wpp,wpm):
    for i in range(100):

        # to calculate waitting time and put some random time to prevent being caught
        waittime = (float(wpp) / float(wpm) * 60.0 + random.randint(1,10)) / 5 
        print(f"wait for {waittime} seconds")
        # prevnt scroll fail and quit current page i divide them in 5 pieces and scroll for 5 times
        stage = 1
        for j in range (6):
            waittime = (float(wpp) / float(wpm) * 60.0 + random.randint(1,10) * 4) / 5 
            while(waittime > 0):
                time.sleep(3)
                waittime -=3
                try:
                    target = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/section/div/div[3]/div/div/div[3]/button')
                    target.click()
                except:
                    continue
            scroll(stage)
            stage+=1 
        time.sleep(1)

        next_page = browser.find_element(By.XPATH,'//*[@id="region-main"]/div/div[4]/div/div[3]/div/button[2]')
        next_page.click()
        print(f'next page scuess! computer has turn page for {i+1} times')
        # make a sound info that has turn the page

        winsound.PlaySound('SystemExclamation',winsound.SND_ALIAS) 
 
#enter your student information 
def studentinfo():
    student_id = str(input('input student id:'))
    print(f'your id is :{student_id}')
    if(len(student_id) != 8):
        print("Error: fake student_id or type error")
        studentinfo()
    else:
        student_id = student_id.upper()
        return student_id

student_id = studentinfo()
wpm = int(input('word per minutes:'))
wpp = int(input('word per page:'))
wait_flag = input('if true press y:')
url = 'https://xreading.com/login/index.php'
browser = webdriver.Chrome('C:\\Users\\chromedriver.exe')#change the path here
browser.get(url)
browser.maximize_window()
login(student_id)
keep_read()
wait_and_page_turn(wpp,wpm)
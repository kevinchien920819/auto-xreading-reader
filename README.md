
# Description
這是一個可以幫你自動完成xreading的外掛程式
this is a plug-in to help you finish your xreading program
# Notice!!!!!

* chromedriver版本要跟電腦的chrome版本相符 
your chromedriver version should same as your chrome version 

* https://helpcenter.trendmicro.com/zh-tw/article/tmka-08277/ (查看你的chrome 版本)
help you to check your chrome version
* https://chromedriver.chromium.org/downloads (chromedriver 下載網址)
the path to download chrome driver

* 預設chrome driver 路徑(請將chrome driver 下載於此): C:\Users\chromedriver.exe
this is the preset patrh of chromedriver put the file in this path :C:\Users\chromedriver.exe
* 若使用非windows 請將6、68行刪除!!
if your device is not windows, please delete 6 and 68 line

# package:
* 執行前先確定有沒有這些packpage
sure you have package in your device 
 - 若沒有請在terminal輸入pip install (要裝的package)
    if not please key "pip install (package name)" in your terminal
 - 1. selenium
# How to use:
- 1. 更改註解裡面的path(86行)或是將chrome driver安裝在預設路徑
    change the chromedriver path if you don't put it in the default path
- 2. 執行程式輸入學號
    enter your student id
- 3. 輸入 wpm(一分鐘讀多少字)
    enter words per min
- 4. 輸入 wpp(一頁有多少字)
    enter words per page
- 5. 按下鍵盤y按下回車
    emter y to keep going

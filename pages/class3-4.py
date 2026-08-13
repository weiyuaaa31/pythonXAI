import random

ans= random.randint(1, 100) #隨機產生 1到100的整數
max_num = 100
min_num = 1
while True: #無窮迴圈
    #可以把想要測試的程式碼放在try裡面，如果程式碼有錯誤，就會執行except裡面的程式碼 
    #try跟except是一對的，最少要有一個try跟一個except也可以有多個except
    try:
        num = int(input(f"請輸入{min_num}到{max_num}的整數:")) #輸入數字
    except: #如果輸入的不是數字
        print("請輸入1到100的整數數字,不要亂輸入!")    
        continue # 就是跳過這次迴圈，直接進入下一次迴圈

    if num < 0 or num > 100: #如果輸入超出範圍
        print("請輸入1到100的整數")
    elif num > ans: #如果輸入的數字大於答案
        print("太大了!")
        if num < max_num: # 檢查 num 是否小於 max_num
            max_num = num # 如果 num 小於 max_num就更新範圍
    elif num < ans: # 如果的輸入數字小于答案 
        print("太小了!") 
        if num > min_num: # 檢查 num 是否大於 min_num
            min_num = num # 如果 num 大於 min_num就更新範圍
    else: #如果 num 等於 ans
        print("答對了!")
        break # 跳出迴圈

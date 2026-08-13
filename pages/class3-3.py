# 算術指定運算子 
a= 1
a+= 1 # a = a + 1
print(a) # 2
a-= 1 # a = a-1
print(a) # 1
a*= 2 # a = a * 2
print(a) # 2
a /= 2 # a = a / 2
print(a) # 1.0
a //=2 # a = a // 2
print(a) # 0
a %= 2 # a = a % 2
print(a) # 0.0
a **= 2 # a = a ** 2
print(a) # 0.0
# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算數指定運算子

# while 迴圈
#while 會搭配一個條件式來使用
# 條件式為True時會一直執行迴圈
# 條件式為false時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成false
i = 0
while i < 5:
    print(i)
    i+= 1 # i = i+1

# break 可以強制跳出迴圈   
# 先判斷break屬于哪個迴圈，然後跳出該迴圈 
i=0
while i<5:
    print(i)

    for J in range(5):
        print(J)

        
    if i == 3:
         break # 跳出迴圈,屬於while迴圈
    i+= 1
    
for i in range(5):
    print(i)
    if i == 3:
        break # 跳出迴圈

import random # 匯入random模組

 # random.randrange()設定抽簽范圍的方式跟range()一樣
print(random.randrange(7)) # 0～6
print(random.randrange(1,6)) #1～6
print(random.randrange(1, 6, 2)) #1～6, 間隔2

#random.randrange()設定抽簽范圍的方式一定要設定開始與結束
#結束的數字會包含在內
print(random.randrange(1, 6)) #1～6

answer = random.randint(1, 100) # 答案
min = 1
max = 100
while True:
    a= int(input(f"請輸入{min}到{max}之間的整數"))
    if answer >a:
        print("太小了")
        min = a
    elif answer <a:    
        print("太大了")
        max = a
    else:
        print("答對了")
        break
            
            

        

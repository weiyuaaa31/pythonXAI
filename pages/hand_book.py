import streamlit as st
with st.expander("class1 課堂筆記"):
    st.write(
        """    
當然可以！我會把今天的內容整理成一份**像國小生也能看懂的 Python 小筆記**，把指令分門別類，並搭配簡單的例子，讓你之後複習時可以快速找到。

# 🐍 Python 入門筆記

## 1. 💬 註解：寫給人看的文字

有時候我們會想在程式裡寫一些「提醒自己的話」，但又不希望 Python 執行這些文字，這時候就可以使用**註解**。

### 單行註解

在文字前面加上 `#`：

```python
# 這是一個註解
print("Hello")
```

Python 看到 `#` 後面的內容，就不會執行它。

### 多行註解

如果想一次寫很多行，可以使用：

```python
'''
這是多行註解
可以寫很多行
這些文字不會被當成一般程式執行
'''
```

### 💡 小技巧

在很多編輯器中：

**Ctrl + ?**

可以快速把程式變成註解，也可以取消註解。

---

# 2. 🖥️ print()：讓電腦說話

`print()` 是 Python 非常重要的指令。

它的功能就是：

> **把東西顯示在螢幕上。**

例如：

```python
print("Hello, World!")
```

電腦就會顯示：

```text
Hello, World!
```

也可以顯示數字：

```python
print(123)
```

---

# 3. 📦 Python 裡的基本資料型態

Python 裡面的資料有很多不同種類，就像我們生活中有：

- 數字
- 文字
- 是或不是

Python 會用不同的「資料型態」來表示它們。

## 🔢 int：整數

沒有小數點的數字叫做**整數**。

```python
print(1)
print(0)
print(-1)
print(100)
```

它們的型態都是：

```text
int
```

可以把 `int` 想成：

> **integer（整數）**

---

## 🔢 float：小數

有小數點的數字叫做**浮點數**。

```python
print(1.0)
print(1.234)
print(3.14)
```

它們的型態都是：

```text
float
```

---

## 🍎 str：文字

文字在 Python 裡叫做**字串（string）**。

通常要放在：

```python
" "
```

或

```python
' '
```

裡面。

例如：

```python
print("apple")
print("Hello")
print("123")
```

注意：

```python
123
```

是數字。

但是：

```python
"123"
```

是文字！

雖然看起來很像，但是它們是不同的資料型態。

---

## ✅ bool：真假值

`bool` 是用來表示：

> **是真的，還是假的？**

只有兩種答案：

```python
True
False
```

例如：

```python
print(True)
print(False)
```

⚠️ `True` 和 `False` 的第一個字母一定要大寫。

---

# 4. 📦 變數：幫資料取名字

變數可以想像成一個**有名字的小盒子**。

我們可以把資料放進盒子裡，以後就可以透過盒子的名字找到它。

例如：

```python
a = 10
```

意思是：

> 建立一個叫做 `a` 的變數，把 `10` 放進去。

然後：

```python
print(a)
```

電腦就會顯示：

```text
10
```

---

## 🔄 變數裡的東西可以改變

例如：

```python
a = 10
print(a)

a = "apple"
print(a)
```

結果：

```text
10
apple
```

原本 `a` 裡面放的是 `10`，後來換成了 `"apple"`。

### ⭐ 記住

```python
a = 10
```

這裡的 `=` **不是「等於」的意思**。

它比較像：

> 「把右邊的東西放進左邊的盒子裡。」

---

# 5. ➕➖✖️➗ 運算子

Python 可以幫我們做數學運算。

| 符號 | 意思   | 範例      |
| ---- | ------ | --------- |
| `+`  | 加法   | `1 + 1`   |
| `-`  | 減法   | `5 - 2`   |
| `*`  | 乘法   | `3 * 4`   |
| `/`  | 除法   | `10 / 2`  |
| `//` | 取商   | `10 // 3` |
| `%`  | 取餘數 | `10 % 3`  |
| `**` | 次方   | `2 ** 3`  |

例如：

```python
print(1 + 1)
```

結果：

```text
2
```

### 📌 取商 `//`

```python
print(10 // 3)
```

10 ÷ 3 = 3 …… 1

所以：

```text
3
```

### 📌 取餘數 `%`

```python
print(10 % 3)
```

10 ÷ 3 = 3 …… 1

所以：

```text
1
```

### 📌 次方 `**`

```python
print(2 ** 3)
```

意思是：

```text
2 × 2 × 2
```

答案：

```text
8
```

---

# 6. 🧮 運算的優先順序

如果一行裡面有很多運算，Python 會按照順序計算。

記住這個順序：

### 🥇 第一名：括號 `()`

```python
( )
```

### 🥈 第二名：次方 `**`

```python
**
```

### 🥉 第三名：乘、除、取商、取餘數

```python
*  /  //  %
```

### 🏅 第四名：加、減

```python
+  -
```

例如：

```python
print(2 + 3 * 4)
```

會先算：

```text
3 × 4 = 12
```

再算：

```text
2 + 12 = 14
```

所以答案是：

```text
14
```

如果加上括號：

```python
print((2 + 3) * 4)
```

就會先算：

```text
2 + 3 = 5
```

再算：

```text
5 × 4 = 20
```

所以答案變成：

```text
20
```

---

# 7. 🍎 字串也可以做運算

Python 不只能計算數字，**文字也可以做一些運算！**

## ➕ 字串相加

```python
print("apple" + "pen")
```

結果：

```text
applepen
```

就是把兩個文字接在一起。

---

## ✖️ 字串乘法

```python
print("apple" * 3)
```

結果：

```text
appleappleapple
```

也就是把 `"apple"` 重複 3 次。

---

# 8. 📝 f-string：把資料放進文字裡

如果想要把變數放進一句話裡，可以使用 **f-string**。

例如：

```python
name = "apple"
age = 18

print(f"Hello, my name is {name}, I'm {age} years old.")
```

結果：

```text
Hello, my name is apple, I'm 18 years old.
```

### ⭐ 重點

前面要加：

```python
f
```

然後想放入變數的地方使用：

```python
{變數名稱}
```

例如：

```python
name = "小明"
age = 10

print(f"我的名字是{name}，我今年{age}歲。")
```

---

# 9. 📏 len()：計算有幾個字

`len()` 是一個**函式**。

它可以幫我們計算字串有多長。

例如：

```python
print(len("apple"))
```

結果：

```text
5
```

因為：

```text
a p p l e
```

總共有 5 個字。

也可以計算中文：

```python
print(len("你好"))
```

結果：

```text
2
```

---

# 10. 🔍 type()：查看資料是什麼種類

有時候我們不知道某個資料到底是：

- 整數
- 小數
- 文字
- True / False

就可以使用：

```python
type()
```

例如：

```python
print(type(1))
```

會得到：

```text
int
```

其他例子：

```python
print(type(1.0))
print(type("apple"))
print(type(True))
```

分別是：

```text
float
str
bool
```

### 🧠 記憶方法

| 型態    | 意思   | 範例      |
| ------- | ------ | --------- |
| `int`   | 整數   | `10`      |
| `float` | 小數   | `3.14`    |
| `str`   | 文字   | `"apple"` |
| `bool`  | 真或假 | `True`    |

---

# 11. 🔄 型態轉換

有時候我們需要把一種資料變成另一種資料。

這就叫做：

> **型態轉換**

---

## int()：變成整數

```python
print(int(1.0))
```

結果：

```text
1
```

小數變成整數時，小數部分會被去掉：

```python
print(int(1.234))
```

結果：

```text
1
```

⚠️ 它不是四捨五入，而是直接把小數部分去掉。

---

## float()：變成小數

```python
print(float(1))
```

結果：

```text
1.0
```

也可以把數字文字變成小數：

```python
print(float("1.234"))
```

結果：

```text
1.234
```

---

## str()：變成文字

```python
print(str(123))
```

會把數字 `123` 變成文字 `"123"`。

---

## bool()：變成真假值

例如：

```python
print(bool(1))
```

會得到：

```text
True
```

---

## ⚠️ 不是所有資料都可以轉換

例如：

```python
int("hello")
```

就會出錯。

因為：

```text
hello
```

不是數字，Python 沒辦法把它變成整數。

---

# 12. ⌨️ input()：讓使用者輸入資料

如果希望使用者可以自己輸入資料，就可以使用：

```python
input()
```

例如：

```python
input("請輸入你的名字：")
```

電腦會顯示：

```text
請輸入你的名字：
```

然後等待使用者輸入。

---

## ⚠️ input() 得到的資料都是文字

這是一個非常重要的觀念！

假設使用者輸入：

```text
10
```

Python 會把它當成：

```python
"10"
```

也就是**字串**。

如果想把它變成數字，就需要使用：

```python
int()
```

例如：

```python
a = int(input("請輸入你的數字："))
```

這樣輸入的數字就可以拿來做數學運算。

例如：

```python
b = int(input())
print(b * b * 3.14)
```

如果輸入：

```text
2
```

就會計算：

```text
2 × 2 × 3.14
```

結果：

```text
12.56
```

---

# 13. 🌐 Streamlit：把 Python 做成網頁

前面學到的 Python 大多是在**終端機**裡看到結果。

如果想把 Python 做成一個漂亮的小網頁，就可以使用：

```python
import streamlit as st
```

這裡的意思可以簡單想成：

> 「把 Streamlit 工具拿進來使用。」

`st` 是我們幫 Streamlit 取的簡短名字。

---

# 14. 🏷️ st.title()：網頁的大標題

```python
st.title("這是標題")
```

可以在網頁上顯示一個很大的標題。

就像：

# 這是標題

---

# 15. ✏️ st.write()：顯示內容

```python
st.write("Hello!")
```

可以在網頁上顯示文字。

而且 `st.write()` 很方便，可以處理很多不同種類的資料。

例如：

```python
st.write("你好")
st.write(123)
```

---

# 16. 📄 st.text()：顯示純文字

```python
st.text("這是一段文字")
```

它主要就是用來顯示**普通文字**。

它不像 Markdown 那樣，可以使用粗體、標題等格式。

---

# 17. ✨ st.markdown()：讓文字變漂亮

Markdown 是一種可以幫文字增加格式的方法。

Streamlit 可以使用：

```python
st.markdown()
```

例如：

```python
st.markdown("**這是粗體**")
```

就可以顯示粗體文字。

---

## ⭐ Markdown 常用符號

### 粗體

```text
**粗體**
```

### 斜體

```text
*斜體*
```

### 大標題

```text
# 最大標題
```

### 第二大標題

```text
## 第二大標題
```

### 第三大標題

```text
### 第三大標題
```

一直到：

```text
######
```

數字越多，標題通常越小。

---

# 18. 📋 Markdown 的項目清單

在文字前面加上：

```text
-
```

就可以製作清單。

例如：

```text
- 蘋果
- 香蕉
- 西瓜
```

會變成：

- 蘋果
- 香蕉
- 西瓜

---

# 19. 💻 Markdown 裡的程式碼

如果想在網頁上顯示 Python 程式碼，可以使用三個反引號：

````text
```python
print("Hello World!")
```
````

這樣就可以讓程式碼看起來比較清楚。

---

# 🧠 今天學到的 Python 快速總整理

最後可以把今天學到的內容想成這張「小抄」：

| 指令 / 符號     | 功能             | 範例                    |
| --------------- | ---------------- | ----------------------- |
| `#`             | 單行註解         | `# 哈囉`                |
| `''' '''`       | 多行文字         | `'''說明'''`            |
| `print()`       | 顯示東西         | `print("Hi")`           |
| `int`           | 整數             | `10`                    |
| `float`         | 小數             | `3.14`                  |
| `str`           | 文字             | `"apple"`               |
| `bool`          | 真 / 假          | `True`                  |
| `=`             | 把資料放進變數   | `a = 10`                |
| `+`             | 加法 / 字串連接  | `1 + 2`                 |
| `-`             | 減法             | `5 - 2`                 |
| `*`             | 乘法 / 重複文字  | `"A" * 3`               |
| `/`             | 除法             | `10 / 2`                |
| `//`            | 取商             | `10 // 3`               |
| `%`             | 取餘數           | `10 % 3`                |
| `**`            | 次方             | `2 ** 3`                |
| `len()`         | 算長度           | `len("apple")`          |
| `type()`        | 查看型態         | `type(10)`              |
| `int()`         | 轉成整數         | `int(3.14)`             |
| `float()`       | 轉成小數         | `float(3)`              |
| `str()`         | 轉成文字         | `str(123)`              |
| `bool()`        | 轉成真假值       | `bool(1)`               |
| `input()`       | 讓使用者輸入     | `input()`               |
| `import`        | 把工具拿進來     | `import streamlit`      |
| `st.title()`    | 網頁標題         | `st.title("Hello")`     |
| `st.write()`    | 顯示內容         | `st.write("Hi")`        |
| `st.text()`     | 顯示純文字       | `st.text("Hi")`         |
| `st.markdown()` | 顯示有格式的文字 | `st.markdown("**Hi**")` |

---

# 🌟 最重要的 10 個觀念

如果今天上完課只記得幾件事情，可以先記住這些：

**① `print()` → 讓電腦把東西顯示出來**

**② `#` → 寫註解，不讓 Python 執行**

**③ `a = 10` → 把 10 放進叫做 `a` 的變數**

**④ `int` → 整數；`float` → 小數**

**⑤ `str` → 文字；`bool` → True / False**

**⑥ `+ - \* / // % **` → Python 的數學運算\*\*

**⑦ `type()` → 查看資料是哪一種型態**

**⑧ `int()`、`float()`、`str()`、`bool()` → 幫資料換型態**

**⑨ `input()` → 讓使用者輸入資料，而且輸入進來預設是文字**

**⑩ `Streamlit` → 可以把 Python 做成網頁**

### 🐍 一句話記住 Python

> **Python 就像是在教電腦做事情：我們用指令告訴電腦「要做什麼」，電腦就按照我們寫的程式一步一步執行。**
    
    """   
        )
        
with st.expander("Class2 課堂筆記"):
    st.write(
        """
當然可以！我把你今天學到的內容重新整理成「**國小學生也看得懂、容易複習**」的 Python 筆記，並把容易搞混的地方特別標出來。

# 🐍 Python 今日學習筆記

## 主題：比較、邏輯、條件判斷、Streamlit、for 迴圈

---

# 一、🔍 比較運算子

「比較運算子」就是拿兩個東西來**比一比**。

比較的結果只有兩種：

* `True` 👉 是、對
* `False` 👉 不是、錯

例如：

```python
print(1 == 1)
```

結果：

```text
True
```

因為 1 和 1 一樣。

### 常見的比較運算子

| 運算子  | 意思    | 範例       | 結果    |
| ---- | ----- | -------- | ----- |
| `==` | 等於    | `1 == 1` | True  |
| `!=` | 不等於   | `1 != 1` | False |
| `>`  | 大於    | `2 > 1`  | True  |
| `<`  | 小於    | `1 < 2`  | True  |
| `>=` | 大於或等於 | `1 >= 1` | True  |
| `<=` | 小於或等於 | `1 <= 1` | True  |

### ⭐ 小提醒

`=` 和 `==` 不一樣！

```python
a = 10
```

`=` 是「**把東西放進變數**」。

```python
a == 10
```

`==` 是「**檢查是不是一樣**」。

可以想成：

> `=` 👉 把東西放進盒子
> `==` 👉 打開盒子檢查是不是一樣

---

# 二、🧠 邏輯運算子

邏輯運算子可以把很多個「對或錯」的條件組合在一起。

有三個重要的運算子：

* `and`
* `or`
* `not`

---

## 1️⃣ and

`and` 可以想成「**而且**」。

👉 **全部都要 True，結果才是 True。**

| 條件1   | 條件2   | 結果      |
| ----- | ----- | ------- |
| True  | True  | ✅ True  |
| True  | False | ❌ False |
| False | True  | ❌ False |
| False | False | ❌ False |

例如：

```python
print(True and True)
```

結果：

```text
True
```

因為兩個條件都是 True。

### 🧠 記憶方法

> `and` = 「而且」
> **全部都要對！**

---

# 2️⃣ or

`or` 可以想成「**或者**」。

👉 **只要有一個是 True，結果就是 True。**

| 條件1   | 條件2   | 結果      |
| ----- | ----- | ------- |
| True  | True  | ✅ True  |
| True  | False | ✅ True  |
| False | True  | ✅ True  |
| False | False | ❌ False |

例如：

```python
print(True or False)
```

結果：

```text
True
```

因為至少有一個 True。

### 🧠 記憶方法

> `or` = 「或者」
> **有一個對就可以！**

---

# 3️⃣ not

`not` 可以想成「**不是、相反**」。

它會把 True 和 False 交換。

```python
print(not True)
```

結果：

```text
False
```

```python
print(not False)
```

結果：

```text
True
```

### 🧠 記憶方法

> `not` = 「反過來！」

---

# 三、📚 Python 的運算優先順序

如果一行程式裡有很多運算，Python 會按照一定的順序計算。

可以把它想成「**誰先做**」。

順序如下：

### ① `()` 括號

最先計算。

```python
(2 + 3) * 4
```

先算 `(2 + 3)`。

---

### ② `**` 次方

```python
2 ** 3
```

意思是：

```text
2 × 2 × 2
```

答案是 `8`。

---

### ③ `* / // %`

這幾個都是乘除相關的運算：

| 運算子  | 意思  |
| ---- | --- |
| `*`  | 乘法  |
| `/`  | 除法  |
| `//` | 取商  |
| `%`  | 取餘數 |

---

### ④ `+ -`

| 運算子 | 意思 |
| --- | -- |
| `+` | 加法 |
| `-` | 減法 |

---

### ⑤ 比較運算子

```text
==  !=  >  <  >=  <=
```

---

### ⑥ `not`

---

### ⑦ `and`

---

### ⑧ `or`

### ⭐ 好記版

```text
() 
↓
**
↓
* / // %
↓
+ -
↓
比較運算子
↓
not
↓
and
↓
or
```

---

# 四、🚪 if、elif、else：讓電腦做選擇

有時候我們希望電腦可以「**判斷事情**」。

例如：

> 如果密碼正確，就歡迎使用者。
> 如果密碼不正確，就說密碼錯誤。

這時候可以使用：

```python
if
elif
else
```

---

## 🔵 if

`if` 的意思是：

> 「如果這個條件成立，就做這件事。」

例如：

```python
if password == "1234":
    print("歡迎Jeffrey")
```

意思是：

> 如果密碼等於 `"1234"`，就顯示「歡迎Jeffrey」。

---

## 🟡 elif

`elif` 可以想成：

> 「不然，如果……」

例如：

```python
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
```

如果第一個條件不成立，就繼續檢查第二個條件。

---

## 🔴 else

`else` 可以想成：

> 「上面的條件都不是，那就做這件事。」

例如：

```python
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
else:
    print("密碼錯誤")
```

---

# 五、🔐 密碼門檢查

完整的例子：

```python
password = input("請輸入密碼：")

if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎chole")
else:
    print("密碼錯誤")
```

電腦會按照順序檢查：

```text
輸入密碼
   ↓
是不是 1234？
   ↓不是
是不是 5678？
   ↓不是
是不是 0000？
   ↓不是
密碼錯誤
```

### ⭐ `if` 和 `if...elif...else` 的差別

如果使用很多個獨立的 `if`：

```python
if 條件1:
    ...

if 條件2:
    ...

if 條件3:
    ...
```

每一個 `if` 都會被檢查。

但是：

```python
if 條件1:
    ...
elif 條件2:
    ...
elif 條件3:
    ...
else:
    ...
```

只要其中一個條件成立，就會停止往下判斷。

### 🧠 簡單記：

> `if`：如果
> `elif`：不然，如果
> `else`：以上都不是

---

# 六、📏 BMI 身體質量指數

我們也練習使用 Python 計算 BMI。

公式：

```text
BMI = 體重 ÷ 身高²
```

程式：

```python
b = float(input("請輸入你的身高："))
a = int(input("請輸入你的體重："))

bmi = a / (b ** 2)
```

這裡：

* `float()` 👉 可以把輸入的資料變成小數
* `int()` 👉 可以把輸入的資料變成整數
* `** 2` 👉 平方

接著可以用 `if` 判斷 BMI：

```python
if bmi < 18.5:
    print("體重過輕")

if bmi >= 18.5 and bmi < 24:
    print("體重正常")
else:
    print("體重過重")
```

### ⚠️ 這裡要特別注意

如果想要做「三種以上的互斥結果」，通常使用：

```python
if
elif
else
```

會比較清楚。

例如：

```python
if bmi < 18.5:
    print("體重過輕")
elif bmi < 24:
    print("體重正常")
else:
    print("體重過重")
```

---

# 七、🌐 Streamlit

`Streamlit` 可以幫我們把 Python 程式做成**簡單的網頁**。

首先要匯入：

```python
import streamlit as st
```

這句的意思是：

> 把 Streamlit 帶進來，並且幫它取一個簡短的名字叫 `st`。

所以之後就可以寫：

```python
st.功能()
```

---

# 八、🔢 st.number_input()

`st.number_input()` 可以在網頁上讓使用者輸入數字。

例如：

```python
number = st.number_input(
    "請輸入一個數字:",
    step=1,
    min_value=0,
    max_value=100
)
```

意思是：

> 在網頁上做一個數字輸入框。

### 常用設定

| 設定              | 意思        |
| --------------- | --------- |
| `step=1`        | 每次增加或減少 1 |
| `min_value=0`   | 最小值是 0    |
| `max_value=100` | 最大值是 100  |

---

# 九、📝 st.markdown()

`st.markdown()` 可以在網頁上顯示文字，而且可以使用 Markdown 語法。

例如：

```python
st.markdown(f"你輸入的數字是: {number}")
```

如果使用者輸入：

```text
50
```

網頁就會顯示：

```text
你輸入的數字是: 50
```

### `f""` 是什麼？

```python
f"你輸入的數字是: {number}"
```

`f` 可以讓我們把變數的內容放進文字裡。

例如：

```python
name = "小明"

print(f"你好，{name}")
```

結果：

```text
你好，小明
```

---

# 十、🏆 分數等級練習

我們可以使用 `if`、`elif`、`else` 做成分數等級判斷。

```python
a = st.number_input(
    "請輸入你的分數",
    step=1,
    min_value=0,
    max_value=100
)

if a >= 90:
    st.write("你的等級是A")
elif a >= 80:
    st.write("你的等級是B")
elif a >= 70:
    st.write("你的等級是C")
elif a >= 60:
    st.write("你的等級是D")
else:
    st.write("你的等級是F")
```

例如輸入：

```text
85
```

電腦會判斷：

```text
85 >= 90 ❌
85 >= 80 ✅
```

所以顯示：

```text
你的等級是B
```

### ⭐ 為什麼不用寫 `a < 90 and a >= 80`？

因為 `elif` 會接著前面的判斷。

當程式走到：

```python
elif a >= 80:
```

代表前面的：

```python
a >= 90
```

已經不成立。

所以只需要寫：

```python
a >= 80
```

就可以了。

---

# 十一、🎈 st.button() 按鈕

`st.button()` 可以在網頁上做出一個**按鈕**。

例如：

```python
st.button("按我一下", key="button1")
```

網頁上就會出現：

> 【按我一下】

---

## 🔑 key 是什麼？

`key` 是按鈕的「**身分證**」。

如果有很多按鈕，就可以用不同的 `key` 來分辨它們。

例如：

```python
key="balloons"
```

和：

```python
key="snow"
```

就是兩個不同的按鈕。

---

# 十二、🎈 按鈕搭配 if

`st.button()` 如果使用者有按下按鈕，就會得到：

```text
True
```

沒有按下：

```text
False
```

所以可以搭配 `if`。

### 🎈 氣球

```python
if st.button("按我一下", key="balloons"):
    st.balloons()
```

意思是：

> 如果使用者按下按鈕，就放氣球！

---

### ❄️ 下雪

```python
if st.button("按我一下", key="snow"):
    st.snow()
```

意思是：

> 如果使用者按下按鈕，就下雪！

---

# 十三、🔁 for 迴圈

`for` 迴圈是一個非常重要的功能。

它可以讓電腦：

> **重複做很多次事情。**

例如：

```python
for i in range(5):
    print(1)
```

這會把 `1` 印出 5 次。

---

# 十四、🔢 range()

`range()` 可以幫我們產生一個「數字範圍」。

### `range(5)`

```python
range(5)
```

會產生：

```text
0
1
2
3
4
```

⚠️ **不包含 5！**

所以：

```python
for i in range(5):
    print(i)
```

會得到：

```text
0
1
2
3
4
```

---

# 十五、🏁 range(開始, 結束)

我們可以自己設定開始和結束的數字。

```python
range(1, 5)
```

會產生：

```text
1
2
3
4
```

⚠️ 一樣**不包含結束的數字 5**。

例如：

```python
for i in range(1, 5):
    print(i)
```

結果：

```text
1
2
3
4
```

---

# 十六、👣 range(開始, 結束, 間隔)

還可以設定「每次跳幾格」。

```python
range(1, 10, 2)
```

意思是：

> 從 1 開始，每次增加 2，直到 10 前面。

所以會得到：

```text
1
3
5
7
9
```

例如：

```python
for i in range(1, 10, 2):
    print(i)
```

結果：

```text
1
3
5
7
9
```

---

# 十七、🎒 for 裡面的 i 是什麼？

```python
for i in range(5):
    print(i)
```

這裡的 `i` 就像一個小盒子。

每跑一次迴圈，就從 `range(5)` 裡面拿一個數字放進 `i`。

可以想成：

```text
第一次：i = 0
第二次：i = 1
第三次：i = 2
第四次：i = 3
第五次：i = 4
```

其實 `i` 這個名字可以自己取。

例如：

```python
for number in range(5):
    print(number)
```

也是可以的。

---

# 十八、✖️ for 迴圈搭配計算

例如：

```python
for i in range(5):
    a = i * 2
    print(a)
```

每一次都把 `i` 乘以 2。

過程：

|  i | i × 2 |  a |
| -: | ----: | -: |
|  0 | 0 × 2 |  0 |
|  1 | 1 × 2 |  2 |
|  2 | 2 × 2 |  4 |
|  3 | 3 × 2 |  6 |
|  4 | 4 × 2 |  8 |

所以最後會顯示：

```text
0
2
4
6
8
```

---

# ⭐ 今日重點總整理

今天學了很多重要的 Python 基礎：

### 🔍 比較運算子

```text
==  !=  >  <  >=  <=
```

👉 用來「比一比」。

---

### 🧠 邏輯運算子

```text
and
or
not
```

👉 用來把條件組合起來。

記憶：

```text
and → 全部都要對
or  → 一個對就可以
not → 相反
```

---

### 🚦 條件判斷

```python
if
elif
else
```

👉 讓電腦做選擇。

---

### 🌐 Streamlit

```python
import streamlit as st
```

👉 把 Python 程式變成互動式網頁。

常用功能：

```python
st.number_input()
st.markdown()
st.write()
st.button()
st.balloons()
st.snow()
```

---

### 🔁 for 迴圈

```python
for i in range(5):
    print(i)
```

👉 讓電腦重複做事情。

---

### 🔢 range()

```python
range(5)
```

👉 `0, 1, 2, 3, 4`

```python
range(1, 5)
```

👉 `1, 2, 3, 4`

```python
range(1, 10, 2)
```

👉 `1, 3, 5, 7, 9`

### ⭐ 最重要的規則

> **range 的「結束數字」永遠不包含！**

---

# 🧩 今日 Python 小地圖

可以把今天學到的東西想成一個小機器人：

```text
             🐍 Python
                 │
      ┌──────────┼──────────┐
      ↓          ↓          ↓
   🔍 比較     🧠 邏輯     🚦 判斷
      │          │          │
   == !=       and        if
   > <         or         elif
   >= <=       not        else
      │          │          │
      └──────────┼──────────┘
                 ↓
             🌐 Streamlit
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
 number_input  button    markdown
                 │
                 ↓
             🔁 for 迴圈
                 │
                 ↓
              range()
```

## 🎯 一句話記住今天

> **比較運算子負責「比一比」,邏輯運算子負責「想一想」,if/elif/else 負責「做選擇」,Streamlit 負責「做網頁」,for 和 range 負責「重複做事情」。**

如果你接下來還有其他堂課的 Python 指令，也可以直接貼上來，我可以繼續用**同一套格式**幫你整理成一份完整的「Python 初學者筆記」。
    
"""
    )
with st.expander("class3 課堂筆記"):
    st.write(
        """     
    )
    # 🐍 Python 課堂筆記：List 清單與 Streamlit 網頁元件

今天的內容可以分成 **4 大部分**：

1. 🔺 用 Streamlit 做「數字金字塔」
2. 📋 Python 的 List（清單）
3. 🧩 List 的新增、刪除、排序與複製
4. 🖥️ Streamlit 的 Columns、Button、文字輸入

---

# 一、🔺 用 Streamlit 做「數字金字塔」

## 1. 匯入 Streamlit

```python
import streamlit as st
```

👉 `import` 就像是「把工具拿過來使用」。

這裡把 `streamlit` 拿進來，並且取一個簡短的名字 `st`。

之後就可以寫：

```python
st.title()
st.write()
st.button()
```

而不用一直寫 `streamlit.title()`。

---

## 2. 建立標題

```python
st.title("數字金字塔")
```

👉 `st.title()` 可以在網頁上顯示**大標題**。

畫面會看到：

# 數字金字塔

---

## 3. 讓使用者輸入數字

```python
a = st.number_input(
    "請輸入一個整數（1到9）",
    min_value=1,
    max_value=9,
    step=1
)
```

`st.number_input()` 是一個「**數字輸入框**」。

### 這些設定是什麼意思？

| 指令               | 意思        |
| ---------------- | --------- |
| `number_input()` | 讓使用者輸入數字  |
| `min_value=1`    | 最小只能輸入 1  |
| `max_value=9`    | 最大只能輸入 9  |
| `step=1`         | 每次增加或減少 1 |

例如使用者輸入：

```text
5
```

那麼：

```python
a
```

就是 `5`。

---

## 4. `for` 迴圈做數字金字塔

```python
for i in range(1, a+1):
    st.write(f"{i}" * i)
```

假設：

```python
a = 5
```

`range(1, a+1)` 就會產生：

```text
1
2
3
4
5
```

而：

```python
f"{i}" * i
```

就是把 `i` 重複很多次。

例如：

```python
"3" * 3
```

結果：

```text
333
```

所以最後會變成：

```text
1
22
333
4444
55555
```

🎯 **小提醒：**

`f"{i}"` 是把 `i` 放進文字裡。

而 `* i` 是讓這個文字重複 `i` 次。

---

# 二、📋 Python 的 List 是什麼？

List 可以想像成一個**大盒子**。

盒子裡面可以放很多東西，而且不同種類的東西也可以放在一起。

List 使用：

```python
[ ]
```

中括號來表示。

---

## 1. 空的 List

```python
print([])
```

這是一個**空的 List**。

就像：

📦 空盒子

裡面什麼都沒有。

---

## 2. 有資料的 List

```python
print([1, 2, 3])
```

裡面有：

```text
1
2
3
```

所以它有 **3 個元素**。

---

## 3. 不同種類的資料也可以放在一起

```python
print([1, 2, 3, "a", "b", "c"])
```

裡面有 6 個元素：

```text
1
2
3
"a"
"b"
"c"
```

List 裡面可以放：

* 整數 `1`
* 小數 `1.23`
* 文字 `"a"`
* `True` / `False`
* 甚至另一個 List

例如：

```python
print([1, 2, 3, ["a", "b", "c"]])
```

這裡總共有 **4 個元素**。

⚠️ 最後面的：

```python
["a", "b", "c"]
```

雖然裡面有 3 個東西，但是對外面的 List 來說，它是一個**元素**。

---

# 三、🔢 List 的 Index（索引）

List 裡面的每一個東西都有自己的「座位號碼」。

這個座位號碼叫做：

> **Index（索引）**

⚠️ Python 的 Index 是從 **0 開始**！

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

可以想成：

| Index |  0 |  1 |  2 | 3     | 4     | 5     |
| ----- | -: | -: | -: | ----- | ----- | ----- |
| 資料    |  1 |  2 |  3 | `"a"` | `"b"` | `"c"` |

所以：

```python
print(L[0])
```

得到：

```text
1
```

```python
print(L[1])
```

得到：

```text
2
```

```python
print(L[2])
```

得到：

```text
3
```

```python
print(L[3])
```

得到：

```text
a
```

### ⭐ 最重要的記憶方法

> **第一個不是 Index 1，而是 Index 0！**

---

# 四、✂️ List 的切片 Slice

Slice 可以想像成：

> 「從 List 裡面切一段資料出來。」

格式：

```python
L[開始:結束:間隔]
```

⚠️ **結束的位置不會包含。**

---

## 1. 每隔 2 個拿一次

```python
L = [1, 2, 3, "a", "b", "c"]

print(L[::2])
```

Index 是：

```text
0  1  2   3   4   5
1  2  3   a   b   c
```

從 Index 0 開始，每次跳 2：

```text
0 → 2 → 4
```

所以結果：

```python
[1, 3, "b"]
```

---

## 2. `L[1:4]`

```python
print(L[1:4])
```

意思是：

> 從 Index 1 開始，拿到 Index 4 **之前**。

所以拿到：

```text
Index 1 → 2
Index 2 → 3
Index 3 → "a"
```

結果：

```python
[2, 3, "a"]
```

---

## 3. `L[1:4:2]`

```python
print(L[1:4:2])
```

意思：

> 從 Index 1 開始，到 Index 4 前，每次跳 2 格。

所以：

```text
Index 1 → 2
Index 3 → "a"
```

結果：

```python
[2, "a"]
```

### ⭐ Slice 小公式

```text
L[開始:結束:每次跳幾格]
```

而且：

> **結束 Index 不包含！**

---

# 五、🚶 List 的走訪

「走訪」就是：

> **一個一個把 List 裡的資料拿出來看。**

有兩種常見方法。

---

## 方法一：使用 Index

```python
L = [1, 2, 3, "a", "b", "c"]

for i in range(0, len(L), 2):
    print(L[i])
```

這裡的：

```python
len(L)
```

是計算 List 裡有幾個元素。

這個 List 有 6 個元素，所以：

```python
len(L)
```

結果是：

```text
6
```

`range(0, 6, 2)` 會得到：

```text
0
2
4
```

因此會印出：

```text
1
3
b
```

👉 這種方法適合「**需要知道 Index**」的時候。

---

## 方法二：直接拿 List 裡的資料

```python
for i in L:
    print(i)
```

Python 會一個一個拿出來：

```text
1
2
3
a
b
c
```

👉 如果只是想把 List 裡的東西一個一個拿出來，這種方法比較簡單。

### ⭐ 記住

```python
for i in L:
```

意思就是：

> 「把 L 裡面的東西，一個一個拿出來。」

---

# 六、📦 Call by Value：複製「值」

```python
a = 1
b = a
b = 2

print(a, b)
```

這裡可以想成：

```text
a → 1
b → 複製 a 的值 → 1
```

後來：

```python
b = 2
```

只是把 `b` 改成 2。

所以：

```text
a = 1
b = 2
```

👉 `a` 不會跟著改變。

---

# 七、🔗 List 的 Call by Reference

這次不一樣：

```python
a = [1, 2, 3]
b = a
```

可以把它想像成：

```text
       ┌─────────────┐
a ───→ │ [1, 2, 3]   │
       └─────────────┘
              ↑
b ────────────┘
```

`a` 和 `b` 指向同一個 List。

所以：

```python
b[0] = 2
```

修改 `b` 的第一個元素後：

```text
a = [2, 2, 3]
b = [2, 2, 3]
```

😮 **a 也跟著變了！**

---

# 八、📋 使用 `copy()` 複製 List

如果不希望 `a` 跟著改變，可以使用：

```python
a = [1, 2, 3]
b = a.copy()

b[0] = 2
```

這樣會產生一份新的 List。

所以：

```text
a = [1, 2, 3]
b = [2, 2, 3]
```

### ⭐ 簡單記憶

```python
b = a
```

👉 共用同一個 List。

```python
b = a.copy()
```

👉 做一份新的 List。

---

# 九、➕ List 的 `append()`

`append()` 是：

> **把東西加到 List 的最後面。**

例如：

```python
L = [1, 2, 3]

L.append(4)

print(L)
```

結果：

```python
[1, 2, 3, 4]
```

📦 原本：

```text
[1, 2, 3]
```

⬇️ `append(4)`

```text
[1, 2, 3, 4]
```

---

# 十、❌ List 移除資料：`remove()`

```python
L = ["a", "b", "c", "d", "a"]

L.remove("a")
```

`remove()` 可以：

> **找到指定的資料，然後把它刪掉。**

⚠️ 如果有很多個相同的資料：

```python
["a", "b", "c", "d", "a"]
```

使用：

```python
L.remove("a")
```

只會刪掉**第一個找到的 `"a"`**。

---

# 十一、🗑️ List 移除資料：`pop()`

`pop()` 是使用 **Index** 來刪除資料。

例如：

```python
L = ["a", "b", "c", "d", "a"]

L.pop(0)
```

Index 0 是：

```text
"a"
```

所以刪掉後：

```python
["b", "c", "d", "a"]
```

---

## `pop()` 不寫 Index

如果寫：

```python
L.pop()
```

就是：

> **刪掉最後一個元素。**

例如：

```python
L = [1, 2, 3, 4]

L.pop()
```

結果：

```python
[1, 2, 3]
```

### ⭐ `remove()` 和 `pop()` 的差別

| 指令            | 用什麼找？    |
| ------------- | -------- |
| `remove("a")` | 找「資料」    |
| `pop(0)`      | 找「Index」 |
| `pop()`       | 刪除最後一個   |

---

# 十二、🔤 List 排序：`sort()`

```python
L = [1, 3, 2, 4, 5]

L.sort()

print(L)
```

結果：

```python
[1, 2, 3, 4, 5]
```

`sort()` 預設會：

> **從小排到大。**

⚠️ 而且 `sort()` 會直接修改原本的 List。

---

# 十三、🖥️ Streamlit 的 Columns 欄位

Streamlit 可以把網頁畫面切成好幾欄。

例如：

```python
col1, col2 = st.columns(2)
```

意思是：

> 把畫面分成 2 欄。

可以想像成：

```text
┌────────────┬────────────┐
│   col1     │    col2    │
│            │            │
└────────────┴────────────┘
```

---

# 十四、🔘 在欄位裡放 Button

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

意思是：

* `col1` 放「按鈕1」
* `col2` 放「按鈕2」

`key` 可以想成按鈕的**身分證號碼**。

如果有很多按鈕，最好給每個按鈕不同的 `key`。

例如：

```python
key="btn1"
key="btn2"
```

---

# 十五、📏 Columns 可以設定寬度比例

```python
col1, col2 = st.columns([1, 2])
```

這不是平均分配。

而是：

```text
col1 : col2
 1   :  2
```

可以想像成：

```text
┌──────┬────────────┐
│col1  │    col2    │
│  1   │      2     │
└──────┴────────────┘
```

---

## 3 欄也可以設定比例

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

意思是：

```text
col1 : col2 : col3
 1   :  2   :  3
```

所以 `col3` 最寬。

---

# 十六、🔁 用 `for` 建立很多 Columns

如果有很多欄，不需要一個一個寫。

例如：

```python
cols = st.columns(4)
```

會產生 4 個欄位：

```text
cols[0]
cols[1]
cols[2]
cols[3]
```

接著：

```python
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")
```

就可以利用迴圈，一次建立很多按鈕。

### ⭐ 這裡要注意

```python
with cols[i]:
```

意思是：

> 「接下來寫的東西，都放進第 `i` 個欄位裡。」

---

# 十七、🎈 `with` 的使用方式

例如：

```python
col1, col2 = st.columns([1, 2])

with col1:
    st.button("按鈕1")
    st.write("這是col1")

with col2:
    st.button("按鈕2")
    st.write("這是col2")
```

可以想像成：

```text
┌────────────┬──────────────────┐
│   col1     │      col2        │
│  按鈕1     │      按鈕2       │
│  這是col1  │      這是col2    │
└────────────┴──────────────────┘
```

👉 `with col1:` 就像是在說：

> 「現在我要進入 col1 工作。」

---

# 十八、🎈 按下按鈕後出現氣球

```python
if st.button("按鈕1"):
    st.balloons()
```

意思是：

> 如果使用者按下「按鈕1」，就放氣球！

這裡的：

```python
if
```

就是：

> **如果……就……**

---

# 十九、📝 Streamlit 文字輸入

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

`st.text_input()` 可以建立一個：

> **文字輸入框**

使用者可以在裡面輸入文字。

---

## `value` 是什麼？

```python
value="這是預設文字"
```

代表：

> 一開始輸入框裡面先放好的文字。

所以一開始會看到：

```text
請輸入文字
[這是預設文字]
```

---

# 二十、💬 顯示使用者輸入的文字

```python
st.write(f"你輸入的文字是:{text}")
```

假設使用者輸入：

```text
小明
```

那麼：

```python
text
```

就是：

```text
小明
```

網頁上就會顯示：

```text
你輸入的文字是:小明
```

---

# 🧠 今天最重要的重點整理

## 📋 List

| 指令         | 功能          | 例子              |
| ---------- | ----------- | --------------- |
| `[]`       | 建立 List     | `L = [1,2,3]`   |
| `L[0]`     | 取得第 1 個元素   | `1`             |
| `L[1:4]`   | 切出一段資料      | 不包含 Index 4     |
| `len(L)`   | 計算元素數量      | `len(L)`        |
| `append()` | 加到最後面       | `L.append(4)`   |
| `remove()` | 移除指定資料      | `L.remove("a")` |
| `pop()`    | 移除最後一個      | `L.pop()`       |
| `pop(0)`   | 移除指定 Index  | `L.pop(0)`      |
| `sort()`   | 排序          | `L.sort()`      |
| `copy()`   | 複製一份新的 List | `b = a.copy()`  |

---

## 🖥️ Streamlit

| 指令                       | 功能           |
| ------------------------ | ------------ |
| `import streamlit as st` | 使用 Streamlit |
| `st.title()`             | 顯示大標題        |
| `st.write()`             | 顯示文字或資料      |
| `st.number_input()`      | 輸入數字         |
| `st.text_input()`        | 輸入文字         |
| `st.button()`            | 建立按鈕         |
| `st.balloons()`          | 顯示氣球動畫       |
| `st.columns()`           | 把畫面分成幾欄      |
| `with col1:`             | 把內容放進指定欄位    |

---

# 🌟 超級重要的 Python 小口訣

### 🔢 Index

> **Python 從 0 開始數！**

```text
第一個 → 0
第二個 → 1
第三個 → 2
```

### ✂️ Slice

> **開始有包含，結束不包含！**

```python
L[1:4]
```

就是：

```text
1、2、3
```

不包含 `4`。

### 📦 List

> **List 就像一個可以裝很多東西的盒子。**

### ➕

> `append()` → **加到最後**

### ❌

> `remove()` → **用資料找來刪**

> `pop()` → **用 Index 找來刪**

### 📋

> `sort()` → **排隊伍，從小到大**

### 📄

> `copy()` → **複製一份新的盒子**

### 🖥️ Streamlit

> `columns()` → **切欄位**

> `button()` → **做按鈕**

> `text_input()` → **讓使用者輸入文字**

> `number_input()` → **讓使用者輸入數字**

---

## 🎯 今天的學習地圖

```text
Python
│
├── 🔺 for 迴圈
│     └── 數字金字塔
│
├── 📋 List
│     ├── Index
│     ├── Slice
│     ├── 走訪
│     ├── append
│     ├── remove
│     ├── pop
│     ├── sort
│     └── copy
│
└── 🖥️ Streamlit
      ├── title
      ├── write
      ├── number_input
      ├── text_input
      ├── button
      ├── balloons
      └── columns
```

        # 🐍 Python 課堂筆記：List 清單與 Streamlit 網頁元件

今天的內容可以分成 **4 大部分**：

1. 🔺 用 Streamlit 做「數字金字塔」
2. 📋 Python 的 List（清單）
3. 🧩 List 的新增、刪除、排序與複製
4. 🖥️ Streamlit 的 Columns、Button、文字輸入

---

# 一、🔺 用 Streamlit 做「數字金字塔」

## 1. 匯入 Streamlit

```python
import streamlit as st
```

👉 `import` 就像是「把工具拿過來使用」。

這裡把 `streamlit` 拿進來，並且取一個簡短的名字 `st`。

之後就可以寫：

```python
st.title()
st.write()
st.button()
```

而不用一直寫 `streamlit.title()`。

---

## 2. 建立標題

```python
st.title("數字金字塔")
```

👉 `st.title()` 可以在網頁上顯示**大標題**。

畫面會看到：

# 數字金字塔

---

## 3. 讓使用者輸入數字

```python
a = st.number_input(
    "請輸入一個整數（1到9）",
    min_value=1,
    max_value=9,
    step=1
)
```

`st.number_input()` 是一個「**數字輸入框**」。

### 這些設定是什麼意思？

| 指令             | 意思             |
| ---------------- | ---------------- |
| `number_input()` | 讓使用者輸入數字 |
| `min_value=1`    | 最小只能輸入 1   |
| `max_value=9`    | 最大只能輸入 9   |
| `step=1`         | 每次增加或減少 1 |

例如使用者輸入：

```text
5
```

那麼：

```python
a
```

就是 `5`。

---

## 4. `for` 迴圈做數字金字塔

```python
for i in range(1, a+1):
    st.write(f"{i}" * i)
```

假設：

```python
a = 5
```

`range(1, a+1)` 就會產生：

```text
1
2
3
4
5
```

而：

```python
f"{i}" * i
```

就是把 `i` 重複很多次。

例如：

```python
"3" * 3
```

結果：

```text
333
```

所以最後會變成：

```text
1
22
333
4444
55555
```

🎯 **小提醒：**

`f"{i}"` 是把 `i` 放進文字裡。

而 `* i` 是讓這個文字重複 `i` 次。

---

# 二、📋 Python 的 List 是什麼？

List 可以想像成一個**大盒子**。

盒子裡面可以放很多東西，而且不同種類的東西也可以放在一起。

List 使用：

```python
[ ]
```

中括號來表示。

---

## 1. 空的 List

```python
print([])
```

這是一個**空的 List**。

就像：

📦 空盒子

裡面什麼都沒有。

---

## 2. 有資料的 List

```python
print([1, 2, 3])
```

裡面有：

```text
1
2
3
```

所以它有 **3 個元素**。

---

## 3. 不同種類的資料也可以放在一起

```python
print([1, 2, 3, "a", "b", "c"])
```

裡面有 6 個元素：

```text
1
2
3
"a"
"b"
"c"
```

List 裡面可以放：

- 整數 `1`
- 小數 `1.23`
- 文字 `"a"`
- `True` / `False`
- 甚至另一個 List

例如：

```python
print([1, 2, 3, ["a", "b", "c"]])
```

這裡總共有 **4 個元素**。

⚠️ 最後面的：

```python
["a", "b", "c"]
```

雖然裡面有 3 個東西，但是對外面的 List 來說，它是一個**元素**。

---

# 三、🔢 List 的 Index（索引）

List 裡面的每一個東西都有自己的「座位號碼」。

這個座位號碼叫做：

> **Index（索引）**

⚠️ Python 的 Index 是從 **0 開始**！

例如：

```python
L = [1, 2, 3, "a", "b", "c"]
```

可以想成：

| Index |   0 |   1 |   2 | 3     | 4     | 5     |
| ----- | --: | --: | --: | ----- | ----- | ----- |
| 資料  |   1 |   2 |   3 | `"a"` | `"b"` | `"c"` |

所以：

```python
print(L[0])
```

得到：

```text
1
```

```python
print(L[1])
```

得到：

```text
2
```

```python
print(L[2])
```

得到：

```text
3
```

```python
print(L[3])
```

得到：

```text
a
```

### ⭐ 最重要的記憶方法

> **第一個不是 Index 1，而是 Index 0！**

---

# 四、✂️ List 的切片 Slice

Slice 可以想像成：

> 「從 List 裡面切一段資料出來。」

格式：

```python
L[開始:結束:間隔]
```

⚠️ **結束的位置不會包含。**

---

## 1. 每隔 2 個拿一次

```python
L = [1, 2, 3, "a", "b", "c"]

print(L[::2])
```

Index 是：

```text
0  1  2   3   4   5
1  2  3   a   b   c
```

從 Index 0 開始，每次跳 2：

```text
0 → 2 → 4
```

所以結果：

```python
[1, 3, "b"]
```

---

## 2. `L[1:4]`

```python
print(L[1:4])
```

意思是：

> 從 Index 1 開始，拿到 Index 4 **之前**。

所以拿到：

```text
Index 1 → 2
Index 2 → 3
Index 3 → "a"
```

結果：

```python
[2, 3, "a"]
```

---

## 3. `L[1:4:2]`

```python
print(L[1:4:2])
```

意思：

> 從 Index 1 開始，到 Index 4 前，每次跳 2 格。

所以：

```text
Index 1 → 2
Index 3 → "a"
```

結果：

```python
[2, "a"]
```

### ⭐ Slice 小公式

```text
L[開始:結束:每次跳幾格]
```

而且：

> **結束 Index 不包含！**

---

# 五、🚶 List 的走訪

「走訪」就是：

> **一個一個把 List 裡的資料拿出來看。**

有兩種常見方法。

---

## 方法一：使用 Index

```python
L = [1, 2, 3, "a", "b", "c"]

for i in range(0, len(L), 2):
    print(L[i])
```

這裡的：

```python
len(L)
```

是計算 List 裡有幾個元素。

這個 List 有 6 個元素，所以：

```python
len(L)
```

結果是：

```text
6
```

`range(0, 6, 2)` 會得到：

```text
0
2
4
```

因此會印出：

```text
1
3
b
```

👉 這種方法適合「**需要知道 Index**」的時候。

---

## 方法二：直接拿 List 裡的資料

```python
for i in L:
    print(i)
```

Python 會一個一個拿出來：

```text
1
2
3
a
b
c
```

👉 如果只是想把 List 裡的東西一個一個拿出來，這種方法比較簡單。

### ⭐ 記住

```python
for i in L:
```

意思就是：

> 「把 L 裡面的東西，一個一個拿出來。」

---

# 六、📦 Call by Value：複製「值」

```python
a = 1
b = a
b = 2

print(a, b)
```

這裡可以想成：

```text
a → 1
b → 複製 a 的值 → 1
```

後來：

```python
b = 2
```

只是把 `b` 改成 2。

所以：

```text
a = 1
b = 2
```

👉 `a` 不會跟著改變。

---

# 七、🔗 List 的 Call by Reference

這次不一樣：

```python
a = [1, 2, 3]
b = a
```

可以把它想像成：

```text
       ┌─────────────┐
a ───→ │ [1, 2, 3]   │
       └─────────────┘
              ↑
b ────────────┘
```

`a` 和 `b` 指向同一個 List。

所以：

```python
b[0] = 2
```

修改 `b` 的第一個元素後：

```text
a = [2, 2, 3]
b = [2, 2, 3]
```

😮 **a 也跟著變了！**

---

# 八、📋 使用 `copy()` 複製 List

如果不希望 `a` 跟著改變，可以使用：

```python
a = [1, 2, 3]
b = a.copy()

b[0] = 2
```

這樣會產生一份新的 List。

所以：

```text
a = [1, 2, 3]
b = [2, 2, 3]
```

### ⭐ 簡單記憶

```python
b = a
```

👉 共用同一個 List。

```python
b = a.copy()
```

👉 做一份新的 List。

---

# 九、➕ List 的 `append()`

`append()` 是：

> **把東西加到 List 的最後面。**

例如：

```python
L = [1, 2, 3]

L.append(4)

print(L)
```

結果：

```python
[1, 2, 3, 4]
```

📦 原本：

```text
[1, 2, 3]
```

⬇️ `append(4)`

```text
[1, 2, 3, 4]
```

---

# 十、❌ List 移除資料：`remove()`

```python
L = ["a", "b", "c", "d", "a"]

L.remove("a")
```

`remove()` 可以：

> **找到指定的資料，然後把它刪掉。**

⚠️ 如果有很多個相同的資料：

```python
["a", "b", "c", "d", "a"]
```

使用：

```python
L.remove("a")
```

只會刪掉**第一個找到的 `"a"`**。

---

# 十一、🗑️ List 移除資料：`pop()`

`pop()` 是使用 **Index** 來刪除資料。

例如：

```python
L = ["a", "b", "c", "d", "a"]

L.pop(0)
```

Index 0 是：

```text
"a"
```

所以刪掉後：

```python
["b", "c", "d", "a"]
```

---

## `pop()` 不寫 Index

如果寫：

```python
L.pop()
```

就是：

> **刪掉最後一個元素。**

例如：

```python
L = [1, 2, 3, 4]

L.pop()
```

結果：

```python
[1, 2, 3]
```

### ⭐ `remove()` 和 `pop()` 的差別

| 指令          | 用什麼找？   |
| ------------- | ------------ |
| `remove("a")` | 找「資料」   |
| `pop(0)`      | 找「Index」  |
| `pop()`       | 刪除最後一個 |

---

# 十二、🔤 List 排序：`sort()`

```python
L = [1, 3, 2, 4, 5]

L.sort()

print(L)
```

結果：

```python
[1, 2, 3, 4, 5]
```

`sort()` 預設會：

> **從小排到大。**

⚠️ 而且 `sort()` 會直接修改原本的 List。

---

# 十三、🖥️ Streamlit 的 Columns 欄位

Streamlit 可以把網頁畫面切成好幾欄。

例如：

```python
col1, col2 = st.columns(2)
```

意思是：

> 把畫面分成 2 欄。

可以想像成：

```text
┌────────────┬────────────┐
│   col1     │    col2    │
│            │            │
└────────────┴────────────┘
```

---

# 十四、🔘 在欄位裡放 Button

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

意思是：

- `col1` 放「按鈕1」
- `col2` 放「按鈕2」

`key` 可以想成按鈕的**身分證號碼**。

如果有很多按鈕，最好給每個按鈕不同的 `key`。

例如：

```python
key="btn1"
key="btn2"
```

---

# 十五、📏 Columns 可以設定寬度比例

```python
col1, col2 = st.columns([1, 2])
```

這不是平均分配。

而是：

```text
col1 : col2
 1   :  2
```

可以想像成：

```text
┌──────┬────────────┐
│col1  │    col2    │
│  1   │      2     │
└──────┴────────────┘
```

---

## 3 欄也可以設定比例

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

意思是：

```text
col1 : col2 : col3
 1   :  2   :  3
```

所以 `col3` 最寬。

---

# 十六、🔁 用 `for` 建立很多 Columns

如果有很多欄，不需要一個一個寫。

例如：

```python
cols = st.columns(4)
```

會產生 4 個欄位：

```text
cols[0]
cols[1]
cols[2]
cols[3]
```

接著：

```python
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")
```

就可以利用迴圈，一次建立很多按鈕。

### ⭐ 這裡要注意

```python
with cols[i]:
```

意思是：

> 「接下來寫的東西，都放進第 `i` 個欄位裡。」

---

# 十七、🎈 `with` 的使用方式

例如：

```python
col1, col2 = st.columns([1, 2])

with col1:
    st.button("按鈕1")
    st.write("這是col1")

with col2:
    st.button("按鈕2")
    st.write("這是col2")
```

可以想像成：

```text
┌────────────┬──────────────────┐
│   col1     │      col2        │
│  按鈕1     │      按鈕2       │
│  這是col1  │      這是col2    │
└────────────┴──────────────────┘
```

👉 `with col1:` 就像是在說：

> 「現在我要進入 col1 工作。」

---

# 十八、🎈 按下按鈕後出現氣球

```python
if st.button("按鈕1"):
    st.balloons()
```

意思是：

> 如果使用者按下「按鈕1」，就放氣球！

這裡的：

```python
if
```

就是：

> **如果……就……**

---

# 十九、📝 Streamlit 文字輸入

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

`st.text_input()` 可以建立一個：

> **文字輸入框**

使用者可以在裡面輸入文字。

---

## `value` 是什麼？

```python
value="這是預設文字"
```

代表：

> 一開始輸入框裡面先放好的文字。

所以一開始會看到：

```text
請輸入文字
[這是預設文字]
```

---

# 二十、💬 顯示使用者輸入的文字

```python
st.write(f"你輸入的文字是:{text}")
```

假設使用者輸入：

```text
小明
```

那麼：

```python
text
```

就是：

```text
小明
```

網頁上就會顯示：

```text
你輸入的文字是:小明
```

---

# 🧠 今天最重要的重點整理

## 📋 List

| 指令       | 功能              | 例子            |
| ---------- | ----------------- | --------------- |
| `[]`       | 建立 List         | `L = [1,2,3]`   |
| `L[0]`     | 取得第 1 個元素   | `1`             |
| `L[1:4]`   | 切出一段資料      | 不包含 Index 4  |
| `len(L)`   | 計算元素數量      | `len(L)`        |
| `append()` | 加到最後面        | `L.append(4)`   |
| `remove()` | 移除指定資料      | `L.remove("a")` |
| `pop()`    | 移除最後一個      | `L.pop()`       |
| `pop(0)`   | 移除指定 Index    | `L.pop(0)`      |
| `sort()`   | 排序              | `L.sort()`      |
| `copy()`   | 複製一份新的 List | `b = a.copy()`  |

---

## 🖥️ Streamlit

| 指令                     | 功能               |
| ------------------------ | ------------------ |
| `import streamlit as st` | 使用 Streamlit     |
| `st.title()`             | 顯示大標題         |
| `st.write()`             | 顯示文字或資料     |
| `st.number_input()`      | 輸入數字           |
| `st.text_input()`        | 輸入文字           |
| `st.button()`            | 建立按鈕           |
| `st.balloons()`          | 顯示氣球動畫       |
| `st.columns()`           | 把畫面分成幾欄     |
| `with col1:`             | 把內容放進指定欄位 |

---

# 🌟 超級重要的 Python 小口訣

### 🔢 Index

> **Python 從 0 開始數！**

```text
第一個 → 0
第二個 → 1
第三個 → 2
```

### ✂️ Slice

> **開始有包含，結束不包含！**

```python
L[1:4]
```

就是：

```text
1、2、3
```

不包含 `4`。

### 📦 List

> **List 就像一個可以裝很多東西的盒子。**

### ➕

> `append()` → **加到最後**

### ❌

> `remove()` → **用資料找來刪**

> `pop()` → **用 Index 找來刪**

### 📋

> `sort()` → **排隊伍，從小到大**

### 📄

> `copy()` → **複製一份新的盒子**

### 🖥️ Streamlit

> `columns()` → **切欄位**

> `button()` → **做按鈕**

> `text_input()` → **讓使用者輸入文字**

> `number_input()` → **讓使用者輸入數字**

---

## 🎯 今天的學習地圖

```text
Python
│
├── 🔺 for 迴圈
│     └── 數字金字塔
│
├── 📋 List
│     ├── Index
│     ├── Slice
│     ├── 走訪
│     ├── append
│     ├── remove
│     ├── pop
│     ├── sort
│     └── copy
│
└── 🖥️ Streamlit
      ├── title
      ├── write
      ├── number_input
      ├── text_input
      ├── button
      ├── balloons
      └── columns
```

**一句話總結：**

> 🐍 **今天學會用 Python 的 List 管理很多資料，再用 Streamlit 把 Python 程式變成有輸入框、按鈕和欄位的互動網頁！**

""")
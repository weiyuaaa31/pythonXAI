# 🐍 Python 課堂筆記：欄位、輸入、迴圈、隨機數與字典

今天學到的內容很多，可以把它想成是在學習「**如何讓 Python 做更多事情**」：

- 🖥️ 用 **Streamlit** 做出漂亮的網頁介面
- 📦 用 **columns** 把東西排成左右或多欄
- ✏️ 用 **text_input** 讓使用者輸入文字
- 💾 用 **session_state** 記住資料
- 🔄 用 **while** 讓程式一直重複
- 🛑 用 **break** 停止迴圈
- 🎲 用 **random** 產生隨機數字
- ⚠️ 用 **try / except** 處理錯誤
- 📖 用 **dict（字典）** 整理很多資料

---

## 一、Streamlit 是什麼？

`streamlit` 可以幫我們把 Python 程式變成一個**可以操作的網頁**。

```python
import streamlit as st
```

這行的意思是：

> 把 Streamlit 工具載入進來，並且取一個簡短的名字叫 `st`。

所以之後看到：

```python
st.title()
st.button()
st.write()
```

就是在使用 Streamlit 的功能。

---

# 二、欄位元件 `st.columns()`

如果我們想讓網頁上的東西**左右排列**，就可以使用：

```python
st.columns()
```

例如：

```python
col1, col2 = st.columns(2)
```

意思是：

> 把畫面分成 **2 個欄位**。

可以想像成：

| col1 | col2 |
| ---- | ---- |
| 左邊 | 右邊 |

---

## 1️⃣ 在欄位裡放按鈕

```python
col1.button("按鈕1", key="btn1")
col2.button("按鈕2", key="btn2")
```

代表：

- `col1` 放「按鈕1」
- `col2` 放「按鈕2」

### 🔑 `key` 是什麼？

`key` 就像是每個按鈕的**身分證號碼**。

例如：

```python
key="btn1"
```

不同的按鈕最好使用不同的 `key`，這樣 Python 才知道是哪一個按鈕。

---

# 三、可以設定欄位的寬度

不一定要讓每個欄位一樣寬。

```python
col1, col2 = st.columns([1, 2])
```

意思是：

> 第一欄寬度是 1，第二欄寬度是 2。

所以畫面大約會變成：

| col1 | col2 |
| ---- | ---- |
| 1份  | 2份  |

第二欄大約是第一欄的 **2 倍寬**。

---

## 1️⃣ 三個欄位

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

會變成：

| col1 | col2 | col3 |
| ---- | ---- | ---- |
| 1份  | 2份  | 3份  |

所以：

- `col1` 最窄
- `col2` 中等
- `col3` 最寬

---

# 四、用 `for` 迴圈建立很多欄位

如果有很多欄位，不需要一個一個寫，可以使用：

```python
cols = st.columns(4)
```

代表建立 4 個欄位：

```text
cols[0]  cols[1]  cols[2]  cols[3]
```

再搭配：

```python
for i in range(len(cols)):
```

就可以一個一個處理欄位。

---

## 五、`with` 是什麼？

例如：

```python
with col1:
    st.button("按鈕1")
    st.write("這是col1")
```

可以把 `with` 想成：

> 「接下來的東西，都放進這個欄位裡！」

所以這兩個東西都會出現在 `col1`：

- 按鈕
- 文字

例如：

```python
with col2:
    st.button("按鈕2")
    st.write("這是col2")
```

就會把內容放到 `col2`。

---

# 六、`st.title()` 和 `st.write()`

### `st.title()`

用來顯示**大標題**：

```python
st.title("點餐機")
```

網頁上就會出現：

# 點餐機

---

### `st.write()`

可以用來顯示文字：

```python
st.write("你好")
```

也可以使用變數：

```python
st.write(f"ans={st.session_state.ans1}")
```

---

# 七、文字輸入 `st.text_input()`

如果希望使用者可以輸入文字，就可以使用：

```python
text = st.text_input("請輸入文字")
```

例如：

```python
text = st.text_input(
    "請輸入文字",
    value="這是預設文字"
)
```

這裡的：

```python
value="這是預設文字"
```

代表輸入框一開始就先顯示：

> 這是預設文字

使用者輸入的內容會被存到：

```python
text
```

裡面。

所以：

```python
st.write(f"你輸入的文字是:{text}")
```

就可以把使用者輸入的內容顯示出來。

---

# 八、`session_state`：幫程式「記住東西」💾

Streamlit 有一個很重要的功能：

```python
st.session_state
```

可以把它想成一個**記憶盒子**。

例如：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

意思是：

> 如果記憶盒子裡還沒有 `ans1`，就把 `ans1` 設定成 1。

---

## 按一下按鈕，數字加 1

```python
if st.button("按下去ans加1"):
    st.session_state.ans1 = st.session_state.ans1 + 1
```

每按一次：

```text
1 → 2 → 3 → 4 → 5 ...
```

所以 `session_state` 很適合用來**保存遊戲分數、購物車、計數器等資料**。

---

# 九、`st.rerun()`：重新執行程式 🔄

有時候按下按鈕後，我們希望網頁馬上更新。

可以使用：

```python
st.rerun()
```

意思就是：

> 「請重新執行一次程式！」

例如：

```python
if st.button("重新整理"):
    st.rerun()
```

按下去後，程式會重新跑一次。

---

# 十、實作：點餐機 🍔

今天還把前面學到的東西組合起來，做成一個小型的「點餐機」。

它使用：

- `st.columns()` → 排版
- `st.text_input()` → 輸入餐點
- `st.button()` → 加入、刪除
- `session_state` → 記住購物籃
- `append()` → 加入餐點
- `pop()` → 刪除餐點
- `rerun()` → 更新畫面

---

## 🛒 購物籃

先建立一個空的 List：

```python
if "cart" not in st.session_state:
    st.session_state.cart = []
```

可以把 `cart` 想成：

> 🛒 一個空空的購物籃。

---

### 加入餐點

```python
st.session_state.cart.append(meal_input)
```

`append()` 的意思是：

> 把新的東西放到 List 的最後面。

例如：

```text
[]
```

加入漢堡：

```text
["漢堡"]
```

再加入薯條：

```text
["漢堡", "薯條"]
```

---

### 刪除餐點

```python
st.session_state.cart.pop(idx)
```

`pop()` 可以把指定位置的資料拿掉。

例如：

```text
["漢堡", "薯條", "可樂"]
```

如果刪除位置 `1`：

```text
["漢堡", "可樂"]
```

---

# 十一、算術指定運算子

這些寫法可以讓我們**更快修改變數**。

假設：

```python
a = 1
```

### `+=`

```python
a += 1
```

等於：

```python
a = a + 1
```

---

### `-=`

```python
a -= 1
```

等於：

```python
a = a - 1
```

---

### `*=`

```python
a *= 2
```

等於：

```python
a = a * 2
```

---

### `/=`

```python
a /= 2
```

等於：

```python
a = a / 2
```

---

### `//=`

```python
a //= 2
```

等於：

```python
a = a // 2
```

`//` 是**取商**。

---

### `%=`

```python
a %= 2
```

等於：

```python
a = a % 2
```

`%` 是**取餘數**。

---

### `**=`

```python
a **= 2
```

等於：

```python
a = a ** 2
```

`**` 是**次方**。

---

# 十二、Python 的運算優先順序 ⭐

如果一個算式裡面有很多不同的運算，Python 有自己的「先後順序」。

從先做，到後做：

1. `()` → 括號
2. `**` → 次方
3. `* / // %` → 乘、除、取商、取餘數
4. `+ -` → 加、減
5. `== != > < >= <=` → 比較
6. `not`
7. `and`
8. `or`
9. `= += -= *= /= //= %= **=` → 指定

### 🧠 小提醒

可以把它想成數學考卷：

> **括號最優先！**

例如：

```python
(2 + 3) * 4
```

要先算：

```text
2 + 3 = 5
```

再算：

```text
5 × 4 = 20
```

---

# 十三、`while` 迴圈 🔄

`while` 的意思可以想成：

> **只要條件是 True，就一直做。**

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

執行結果：

```text
0
1
2
3
4
```

運作方式：

```text
i = 0
↓
i < 5？是 → 印出 0
↓
i + 1
↓
i < 5？是 → 印出 1
↓
...
↓
i = 5
↓
5 < 5？不是
↓
停止
```

---

# 十四、`break`：強制停止迴圈 🛑

`break` 的意思是：

> **立刻離開目前的迴圈。**

例如：

```python
for i in range(5):
    print(i)

    if i == 3:
        break
```

結果：

```text
0
1
2
3
```

到了 `3` 就停止了。

---

## ⚠️ 巢狀迴圈中的 `break`

如果迴圈裡面還有另一個迴圈：

```python
while i < 5:

    for j in range(5):
        print(j)

    if i == 3:
        break
```

這裡的 `break` 是屬於外面的 `while`。

所以要特別注意：

> `break` 會跳出它所屬的那一層迴圈。

---

# 十五、`random`：讓電腦抽籤 🎲

如果想讓電腦隨機產生數字，可以使用：

```python
import random
```

這表示：

> 把 `random` 隨機功能載入進來。

---

## `random.randint()`

```python
random.randint(1, 100)
```

代表：

> 隨機產生 **1～100** 的整數。

例如可能得到：

```text
27
```

下一次可能變成：

```text
83
```

---

## `random.randrange()`

例如：

```python
random.randrange(7)
```

會產生：

```text
0～6
```

注意：

> `range()` 和 `randrange()` 的結束數字通常**不包含**。

例如：

```python
random.randrange(1, 6)
```

會產生：

```text
1、2、3、4、5
```

不是 6。

### ⚠️ 筆記中的一個重要修正

你原本的註解寫「1～6」，但實際上：

```python
random.randrange(1, 6)
```

是 **1～5**。

如果真的想產生 **1～6**，可以使用：

```python
random.randint(1, 6)
```

---

# 十六、猜數字遊戲 🎯

今天利用 `random`、`while`、`if`、`break` 做了一個猜數字遊戲。

```python
answer = random.randint(1, 100)
```

電腦先偷偷選一個：

> 1～100 的數字。

玩家開始猜。

如果：

```python
answer > a
```

代表：

> 猜太小了！

如果：

```python
answer < a
```

代表：

> 猜太大了！

最後：

```python
else:
    print("答對了")
    break
```

猜對就離開迴圈。

---

# 十七、讓猜數字遊戲更聰明 🧠

第二個猜數字程式增加了：

```python
min_num = 1
max_num = 100
```

一開始範圍：

```text
1 ～ 100
```

如果猜 30，而且答案比 30 大：

```text
31 ～ 100
```

如果接著猜 80，而答案比 80 小：

```text
31 ～ 79
```

所以電腦會一直縮小範圍。

這樣玩家就更容易知道下一次應該猜哪裡。

---

# 十八、`try` 和 `except`：處理錯誤 ⚠️

如果使用者本來應該輸入數字，卻輸入：

```text
蘋果
```

程式可能會發生錯誤。

所以可以使用：

```python
try:
    num = int(input("請輸入數字"))
except:
    print("請輸入數字")
```

意思是：

> **try：先試著執行。**
> **except：如果出錯，就做這裡的事情。**

可以把它想成：

```text
try
 ↓
試看看
 ↓
成功？ → 繼續
 ↓
失敗？
 ↓
except → 處理錯誤
```

---

# 十九、`continue`：跳過這一次 🔄

```python
continue
```

意思是：

> **這一次不要繼續做了，直接開始下一輪迴圈。**

例如：

```python
except:
    print("請輸入數字")
    continue
```

如果使用者輸入錯誤：

1. 顯示錯誤訊息
2. `continue`
3. 回到下一輪
4. 再讓使用者輸入一次

---

# 二十、字典 `dict` 📖

Python 裡面還有一種很重要的資料工具：

```python
dict
```

中文可以叫：

> **字典**

字典的特色是使用：

```text
key → value
```

也就是：

> **關鍵字 → 資料**

例如：

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

可以想成：

| Key | Value |
| --- | ----: |
| a   |     1 |
| b   |     2 |
| c   |     3 |

---

# 二十一、Key 和 Value

例如：

```python
"a": 1
```

其中：

- `"a"` 是 **key**
- `1` 是 **value**

### 🔑 Key

Key 就像是：

> 一個資料的「名字」。

同一個字典裡，Key 必須是唯一的。

### 📦 Value

Value 是：

> Key 對應的真正資料。

Value 可以重複，也可以放不同種類的資料。

---

# 二十二、取得字典的 Key

```python
d.keys()
```

可以取得所有 Key。

例如：

```python
for key in d.keys():
    print(key)
```

結果：

```text
a
b
c
```

---

# 二十三、取得字典的 Value

```python
d.values()
```

可以取得所有 Value。

例如：

```python
for value in d.values():
    print(value)
```

結果：

```text
1
2
3
```

---

# 二十四、同時取得 Key 和 Value

```python
d.items()
```

可以一次取得：

> Key + Value

例如：

```python
for key, value in d.items():
    print(key, value)
```

結果：

```text
a 1
b 2
c 3
```

---

# 二十五、新增和修改字典資料

### ➕ 新增

```python
d["d"] = 4
```

原本：

```text
a → 1
b → 2
c → 3
```

變成：

```text
a → 1
b → 2
c → 3
d → 4
```

---

### ✏️ 修改

```python
d["a"] = 5
```

原本：

```text
a → 1
```

變成：

```text
a → 5
```

---

# 二十六、`pop()`：刪除字典資料

```python
d.pop("a")
```

意思是：

> 把 Key 是 `"a"` 的資料刪掉。

而且會回傳被刪除的 Value。

---

如果找不到資料：

```python
d.pop("e", "Not found")
```

就會得到：

```text
Not found
```

所以可以記住：

> `pop()` → **拿走資料**

---

# 二十七、`in`：檢查資料有沒有存在 🔍

例如：

```python
"a" in d
```

可以檢查：

> `"a"` 這個 Key 存不存在？

如果存在：

```text
True
```

如果不存在：

```text
False
```

### ⚠️ 注意

對 `dict` 使用 `in` 時，檢查的是：

> **Key，不是 Value。**

例如：

```python
"a" in d
```

是在找 Key `"a"`。

---

# 二十八、字典裡面還可以放 List 和另一個字典

Python 可以建立很複雜的資料。

例如：

```python
d = {
    "a": [1, 2, 3],
    "b": {
        "c": 4,
        "d": 5
    }
}
```

這就像一個大盒子裡面還有小盒子。

---

### 取得 List

```python
d["a"]
```

得到：

```text
[1, 2, 3]
```

### 取得 List 第 1 個資料

```python
d["a"][0]
```

得到：

```text
1
```

### 取得裡面的字典

```python
d["b"]
```

得到：

```text
{"c": 4, "d": 5}
```

### 再取得裡面的 `c`

```python
d["b"]["c"]
```

得到：

```text
4
```

---

# 二十九、成績登記系統 📚

今天用「字典裡面放字典，字典裡面又放 List」的方法，建立了一個成績系統。

例如：

```text
小明
 ├── 國文 → 90、80、70
 ├── 數學 → 85、75、65
 └── 英文 → 95、85、75
```

所以：

```python
grade["小明"]["數學"]
```

就可以找到小明的數學成績：

```text
[85, 75, 65]
```

如果想找小美第一次英文成績：

```python
grade["小美"]["英文"][0]
```

得到：

```text
93
```

---

# 三十、計算平均成績

例如：

```python
chinese = subjects["國文"]
avg = sum(chinese) / len(chinese)
```

這裡有兩個很重要的功能：

### `sum()`

把數字全部加起來。

```python
sum([90, 80, 70])
```

得到：

```text
240
```

### `len()`

計算有幾個資料。

```python
len([90, 80, 70])
```

得到：

```text
3
```

所以：

```python
240 / 3
```

得到：

```text
80
```

就是平均分數。

---

# 三十一、`.2f` 是什麼？

例如：

```python
print(f"平均成績是{avg:.2f}")
```

`.2f` 的意思是：

> 小數點後面顯示 **2 位**。

例如：

```text
80
```

可能顯示成：

```text
80.00
```

又例如：

```text
85.666666
```

會顯示成：

```text
85.67
```

---

# 三十二、計算每個人的總平均

可以用兩層 `for` 迴圈：

```python
for name, subjects in grade.items():
    total = 0

    for scores in subjects.values():
        total += sum(scores)
```

可以想成：

```text
小明
 ↓
國文 → 加起來
數學 → 加起來
英文 → 加起來
 ↓
全部加起來
 ↓
算平均
```

這就是**巢狀迴圈**：

> 迴圈裡面還有另一個迴圈。

---

# 三十三、整理全校各科成績

建立：

```python
avg_grade = {
    "國文": [],
    "數學": [],
    "英文": []
}
```

可以想成有三個資料夾：

📁 國文
📁 數學
📁 英文

接著把每位同學的成績放進正確的資料夾。

最後會得到：

```text
國文 → 所有學生的國文成績
數學 → 所有學生的數學成績
英文 → 所有學生的英文成績
```

這樣就可以進一步計算：

> 全校國文平均
> 全校數學平均
> 全校英文平均

---

# 三十四、`len(dict)`：計算字典有幾個 Key

例如：

```python
len(avg_grade)
```

如果有：

```python
{
    "國文": [],
    "數學": [],
    "英文": []
}
```

就會得到：

```text
3
```

因為有 3 個 Key：

- 國文
- 數學
- 英文

---

# 三十五、圖片元件 `st.image()` 🖼️

Streamlit 也可以在網頁上顯示圖片。

首先：

```python
import streamlit as st
import os
```

接著：

```python
st.image("image/apple.png", width=300)
```

意思是：

> 把 `image` 資料夾裡面的 `apple.png` 顯示在網頁上。

`width=300` 表示：

> 圖片寬度設定成 300。

所以只要把圖片放在正確的位置，就可以讓 Streamlit 顯示圖片。

---

# 🧠 今天最重要的指令總整理

| 指令                 | 簡單意思                 |
| -------------------- | ------------------------ |
| `st.title()`         | 顯示大標題               |
| `st.write()`         | 顯示文字                 |
| `st.button()`        | 建立按鈕                 |
| `st.columns()`       | 把畫面分成幾欄           |
| `with`               | 把內容放進指定欄位       |
| `st.text_input()`    | 建立文字輸入框           |
| `st.session_state`   | 幫程式記住資料           |
| `st.rerun()`         | 重新執行程式             |
| `append()`           | 在 List 後面加入資料     |
| `pop()`              | 刪除資料                 |
| `+=`                 | 加上某個數字             |
| `-=`                 | 減去某個數字             |
| `*=`                 | 乘上某個數字             |
| `/=`                 | 除以某個數字             |
| `//=`                | 取商                     |
| `%=`                 | 取餘數                   |
| `**=`                | 次方                     |
| `while`              | 條件成立就一直做         |
| `for`                | 重複做很多次             |
| `break`              | 離開迴圈                 |
| `continue`           | 跳過這一輪               |
| `import random`      | 載入隨機功能             |
| `random.randint()`   | 隨機產生整數，包含頭尾   |
| `random.randrange()` | 按照範圍規則隨機產生數字 |
| `try`                | 試著執行程式             |
| `except`             | 發生錯誤時處理           |
| `dict`               | 用 Key 和 Value 儲存資料 |
| `.keys()`            | 取得所有 Key             |
| `.values()`          | 取得所有 Value           |
| `.items()`           | 同時取得 Key 和 Value    |
| `in`                 | 檢查是否存在             |
| `sum()`              | 計算總和                 |
| `len()`              | 計算資料數量             |
| `st.image()`         | 顯示圖片                 |

---

# 🌟 今天的 Python 學習地圖

可以把今天學到的東西想成一個小小的工具箱：

```text
🐍 Python
│
├── 🖥️ Streamlit 網頁
│   ├── title
│   ├── write
│   ├── button
│   ├── columns
│   ├── text_input
│   ├── session_state
│   ├── rerun
│   └── image
│
├── 🔄 迴圈
│   ├── for
│   ├── while
│   ├── break
│   └── continue
│
├── 🎲 隨機數
│   ├── random.randint()
│   └── random.randrange()
│
├── ⚠️ 錯誤處理
│   ├── try
│   └── except
│
├── 📖 字典 dict
│   ├── key
│   ├── value
│   ├── keys()
│   ├── values()
│   ├── items()
│   └── pop()
│
└── ➕ 運算
    ├── +=
    ├── -=
    ├── *=
    ├── /=
    ├── //=
    ├── %=
    └── **=
```

## 🎯 今天最值得記住的 5 件事

**① `columns` 是排版工具**
👉 可以讓按鈕、文字等東西左右排列。

**② `session_state` 是記憶盒子**
👉 可以讓 Streamlit 記住分數、購物車等資料。

**③ `while` 是「一直做」**
👉 只要條件是 `True`，就會繼續執行。

**④ `dict` 是「名字對資料」**
👉 用 `key → value` 的方式整理資料，非常適合做成績表、會員資料等。

**⑤ `try / except` 是「出錯不要怕」**
👉 程式遇到錯誤時，可以先處理錯誤，而不是直接停止。

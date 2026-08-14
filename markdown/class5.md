# 🐍 Python＋Streamlit＋AI 聊天機器人課堂筆記

今天學到的內容比較多，主要可以分成 **4 個部分**：

1. 🔑 使用 OpenAI API
2. 💬 製作可以記住對話的 AI
3. 🖥️ 用 Streamlit 做聊天機器人
4. 🛒 用 Streamlit 做購物平台

---

## 一、🔑 使用 OpenAI API

### 1. `import`

```python
import openai
import os
```

`import` 就像是「把工具拿進來使用」。

- `openai`：讓 Python 可以使用 OpenAI 的功能
- `os`：可以幫助 Python 取得電腦上的環境設定

安裝 OpenAI 套件：

```bash
pip install openai
```

---

### 2. `from dotenv import load_dotenv`

```python
from dotenv import load_dotenv
```

這是把 `.env` 裡面的設定載入 Python。

`.env` 可以放一些重要的資料，例如：

```text
OPENAI_API_KEY=你的API金鑰
```

這樣就不用直接把 API 金鑰寫在 Python 程式裡。

---

### 3. `load_dotenv()`

```python
load_dotenv()
```

意思是：

> 「把 `.env` 裡面的資料載入進來。」

---

### 4. `os.getenv()`

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

`os.getenv()` 可以取得環境變數。

這裡就是取得：

```text
OPENAI_API_KEY
```

然後把它設定成 OpenAI 使用的 API 金鑰。

🔐 **API 金鑰很重要，不可以隨便公開給別人！**

---

# 二、💬 製作最基本的 AI 聊天程式

### 1. `input()`

```python
user_input = input("你：")
```

`input()` 可以讓使用者在終端機輸入文字。

例如：

```text
你：你好
```

使用者輸入的內容會存到：

```python
user_input
```

---

### 2. `while True`

```python
while True:
```

意思是：

> 一直重複執行。

所以 AI 就可以一直和我們聊天。

---

### 3. `lower()`

```python
user_input.lower()
```

`lower()` 可以把英文變成小寫。

例如：

```python
"EXIT".lower()
```

會變成：

```text
exit
```

這樣使用者輸入 `EXIT`、`Exit`、`exit` 都可以判斷。

---

### 4. `in`

```python
if user_input.lower() in ["exit", "quit"]:
```

`in` 可以檢查某個東西「有沒有在裡面」。

這裡是在檢查：

> 使用者輸入的是不是 `exit` 或 `quit`。

---

### 5. `break`

```python
break
```

`break` 的意思是：

> 馬上離開迴圈。

所以：

```python
if user_input.lower() in ["exit", "quit"]:
    break
```

就是輸入 `exit` 或 `quit` 後，結束聊天。

---

# 三、🤖 呼叫 AI

### `openai.chat.completions.create()`

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "請用繁體中文進行後續對話"},
        {"role": "user", "content": user_input},
    ],
)
```

這個指令就是：

> 📢 把訊息送給 AI，請 AI 回答。

---

## `model`

```python
model="gpt-4o-mini"
```

`model` 是告訴程式：

> 我要使用哪一個 AI 模型。

例如：

```text
gpt-4o-mini
gpt-4o
```

---

## `messages`

```python
messages=[
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
]
```

`messages` 是「聊天內容」。

可以想像成一本聊天紀錄本 📖。

---

## `role`

`role` 是「這句話是誰說的」。

主要會看到：

| role        | 意思             |
| ----------- | ---------------- |
| `system`    | 告訴 AI 要怎麼做 |
| `user`      | 使用者說的話     |
| `assistant` | AI 說的話        |

例如：

```python
{"role": "user", "content": "你好"}
```

就是：

> 使用者說：「你好」

---

## `content`

```python
"content": "你好"
```

`content` 就是：

> 💬 實際說的內容。

---

# 四、📖 讓 AI 記住之前的聊天

一開始的 AI 可能只知道現在這一句話。

所以我們建立：

```python
messages = [
    {"role": "system", "content": "請用繁體中文進行後續對話"}
]
```

這就是「聊天紀錄」。

---

## `append()`

```python
messages.append(
    {"role": "user", "content": user_input}
)
```

`append()` 是：

> ➕ 把新的東西加到列表最後面。

例如：

```python
messages = ["你好"]
messages.append("今天天氣如何？")
```

就會變成：

```python
["你好", "今天天氣如何？"]
```

---

AI 回答之後也要加入紀錄：

```python
messages.append(
    {"role": "assistant", "content": assistant_message}
)
```

這樣下一次問問題時，AI 就可以看到之前的聊天內容。

---

# 五、📦 `response.choices[0].message.content`

```python
assistant_message = response.choices[0].message.content
```

這一行是在：

> 📩 從 AI 回傳的資料中，把 AI 真正回答的文字拿出來。

可以把它想成：

```text
response
 ↓
choices
 ↓
第 1 個答案 [0]
 ↓
message
 ↓
content
 ↓
AI回答的文字
```

---

# 六、🖨️ `print()` 和 f-string

```python
print(f"AI：{assistant_message}")
```

`print()` 可以在終端機顯示文字。

`f"..."` 可以把變數放進文字裡。

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

# 七、🖥️ Streamlit 聊天泡泡

### `st.chat_message()`

```python
st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的回應")
```

`st.chat_message()` 可以製作像聊天軟體一樣的：

💬 **聊天泡泡**

- `"user"` → 使用者
- `"assistant"` → AI

---

## `write()`

```python
.write("你好")
```

`write()` 可以把文字顯示在網頁上。

---

# 八、🔄 用 `for` 顯示聊天紀錄

我們可以先建立：

```python
history = [
    {"role": "user", "content": "你好，AI！"},
    {"role": "assistant", "content": "哈囉！"},
]
```

這是一個「聊天紀錄列表」。

然後：

```python
for message in history:
```

代表：

> 🔁 一筆一筆讀取聊天紀錄。

---

### `if`

```python
if message["role"] == "user":
```

如果角色是使用者，就顯示使用者的聊天泡泡。

否則：

```python
else:
```

就顯示 AI 的聊天泡泡。

---

# 九、🪄 `avatar`

```python
st.chat_message("user", avatar="🪄")
```

`avatar` 可以設定聊天泡泡旁邊的圖示。

例如：

```text
🪄 使用者
✨ AI
```

---

# 十、💾 `st.session_state`

這是今天非常重要的功能！

```python
st.session_state
```

可以把資料暫時「記住」。

Streamlit 每次更新畫面時，普通的變數可能會重新開始。

所以我們可以使用：

```python
st.session_state.history
```

來保存聊天紀錄。

---

## 初始化

```python
if "history" not in st.session_state:
    st.session_state.history = []
```

意思是：

> 如果還沒有聊天紀錄，就建立一個空列表。

---

也可以保存系統訊息：

```python
if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"
```

還可以保存 AI 模型：

```python
if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"
```

---

# 十一、📐 Streamlit 欄位

```python
col1, col2, col3 = st.columns([4, 2, 1])
```

這可以把網頁分成 3 欄。

寬度比例是：

```text
第1欄：4
第2欄：2
第3欄：1
```

也就是：

```text
┌──────────────┬──────┬───┐
│     col1     │ col2 │c3 │
│      4       │  2   │ 1 │
└──────────────┴──────┴───┘
```

---

# 十二、📝 `st.text_input()`

```python
st.text_input(
    "系統訊息",
    st.session_state.system_message
)
```

可以讓使用者輸入文字。

例如：

```text
系統訊息：[請用繁體中文回答]
```

---

# 十三、🔽 `st.selectbox()`

```python
st.selectbox(
    "AI模型",
    ["gpt-4o-mini", "gpt-4o", "gpt-4o-search-preview"]
)
```

`selectbox()` 可以做一個「下拉式選單」。

例如：

```text
AI模型 ▼
gpt-4o-mini
gpt-4o
gpt-4o-search-preview
```

使用者就可以選擇 AI 模型。

---

# 十四、🗑️ 清除聊天紀錄

```python
if st.button("🗑️"):
    st.session_state.history = []
    st.rerun()
```

按下垃圾桶按鈕後：

### 第一步

```python
st.session_state.history = []
```

把聊天紀錄變成空列表。

### 第二步

```python
st.rerun()
```

重新執行 Streamlit 網頁。

所以畫面就會更新。

---

# 十五、💬 `st.chat_input()`

```python
prompt = st.chat_input("請輸入想要對話的訊息")
```

這可以建立聊天輸入框。

例如：

```text
┌──────────────────────────┐
│ 請輸入想要對話的訊息      │
└──────────────────────────┘
```

---

如果有輸入：

```python
if prompt:
```

就代表：

> 如果使用者真的輸入了文字，就開始處理。

---

# 十六、🛒 購物平台

今天最後還把學到的東西做成一個小型購物平台！

---

## 1. 商品列表

```python
products = ["apple", "banana", "bg", "orange"]
```

這是一個列表，裡面放商品名稱。

---

## 2. 商品名稱

```python
product_names = {
    "apple": "🍎 蘋果",
    "banana": "🍌 香蕉",
    "bg": "🍇 葡萄",
    "orange": "🍊 柳橙"
}
```

這是一個 **字典 dictionary**。

可以利用：

```python
product_names["apple"]
```

找到：

```text
🍎 蘋果
```

---

# 十七、💰 商品價格

```python
prices = {
    "apple": 10,
    "banana": 10,
    "bg": 10,
    "orange": 10
}
```

用字典保存每個商品的價格。

例如：

```python
prices["apple"]
```

結果就是：

```text
10
```

---

# 十八、📦 商品庫存

```python
st.session_state.stock = {
    "apple": 10,
    "banana": 10,
    "bg": 10,
    "orange": 10
}
```

這裡保存每種商品目前有幾個。

例如：

```python
st.session_state.stock["apple"]
```

就是蘋果目前的庫存。

---

# 十九、🔢 `st.number_input()`

```python
column_number = st.number_input(
    "欄位數",
    min_value=1,
    max_value=4,
    value=4,
    step=1
)
```

這可以讓使用者輸入數字。

這裡設定：

| 指令          | 意思       |
| ------------- | ---------- |
| `min_value=1` | 最小值是 1 |
| `max_value=4` | 最大值是 4 |
| `value=4`     | 預設是 4   |
| `step=1`      | 每次增加 1 |

---

# 二十、📐 動態建立欄位

```python
cols = st.columns(column_number)
```

如果使用者選：

```text
4
```

就建立 4 個欄位。

如果選：

```text
2
```

就建立 2 個欄位。

---

# 二十一、🔁 `for` 迴圈

```python
for i in range(column_number):
```

這會重複執行程式。

例如欄位數是 4：

```text
i = 0
i = 1
i = 2
i = 3
```

---

# 二十二、🖼️ `st.image()`

```python
st.image(
    "image/" + product + ".png",
    width=150
)
```

可以顯示圖片。

如果：

```python
product = "apple"
```

程式就會組合成：

```text
image/apple.png
```

所以圖片要放在：

```text
image
├── apple.png
├── banana.png
├── bg.png
└── orange.png
```

---

# 二十三、➕ 字串連接

```python
"image/" + product + ".png"
```

`+` 不只能拿來加數字，也可以把文字接在一起。

例如：

```python
"Hello " + "World"
```

結果：

```text
Hello World
```

---

# 二十四、🛍️ 購買商品

```python
if st.button(
    "購買",
    key="buy_" + product
):
```

建立「購買」按鈕。

`key` 可以幫每個按鈕取一個不同的名字。

例如：

```text
buy_apple
buy_banana
buy_bg
buy_orange
```

這樣每個按鈕才不會搞混。

---

# 二十五、📦 判斷有沒有庫存

```python
if st.session_state.stock[product] > 0:
```

`>` 是「大於」。

所以這句是在問：

> 商品庫存是不是大於 0？

如果大於 0，就可以購買。

---

# 二十六、➖ 庫存減少

```python
st.session_state.stock[product] -= 1
```

這等於：

```python
st.session_state.stock[product] = st.session_state.stock[product] - 1
```

意思是：

> 買一個商品，所以庫存減少 1。

---

# 二十七、✅ `st.success()`

```python
st.success("購買成功")
```

顯示成功訊息。

例如：

🟢 購買成功

---

# 二十八、❌ `st.error()`

```python
st.error("沒有庫存")
```

顯示錯誤訊息。

例如：

🔴 沒有庫存

---

# 二十九、➕ 新增商品庫存

```python
selected_product = st.selectbox(
    "商品",
    products,
    format_func=lambda x: product_names[x]
)
```

這裡可以選擇要增加哪一種商品。

`format_func` 可以把程式裡的名稱換成比較漂亮的名稱。

例如：

```text
apple
```

顯示成：

```text
🍎 蘋果
```

---

# 三十、`lambda`

```python
lambda x: product_names[x]
```

`lambda` 可以快速建立一個小小的函式。

這裡的意思可以簡單理解成：

> 把商品代號 `x` 拿去商品名稱字典查詢。

---

# 三十一、➕ 增加庫存

```python
st.session_state.stock[selected_product] += add_number
```

`+=` 是：

> 原本的數字再加上新的數字。

例如：

```python
stock = 10
stock += 5
```

就會變成：

```text
15
```

所以如果蘋果原本有 10 個，新增 5 個，就會變成 15 個。

---

# 三十二、⭐ 今天最重要的指令整理

| 指令                | 簡單意思         |
| ------------------- | ---------------- |
| `import`            | 把工具拿進來     |
| `load_dotenv()`     | 載入 `.env`      |
| `os.getenv()`       | 取得環境變數     |
| `input()`           | 讓使用者輸入     |
| `while True`        | 一直重複         |
| `break`             | 離開迴圈         |
| `lower()`           | 英文變小寫       |
| `in`                | 檢查有沒有在裡面 |
| `append()`          | 加到列表最後面   |
| `print()`           | 在終端機顯示     |
| `st.write()`        | 在網頁顯示       |
| `st.title()`        | 顯示大標題       |
| `st.columns()`      | 建立欄位         |
| `st.button()`       | 建立按鈕         |
| `st.text_input()`   | 建立文字輸入框   |
| `st.number_input()` | 建立數字輸入框   |
| `st.selectbox()`    | 建立下拉選單     |
| `st.image()`        | 顯示圖片         |
| `st.chat_message()` | 顯示聊天泡泡     |
| `st.chat_input()`   | 建立聊天輸入框   |
| `st.session_state`  | 保存網頁中的資料 |
| `st.rerun()`        | 重新執行網頁     |
| `st.success()`      | 顯示成功訊息     |
| `st.error()`        | 顯示錯誤訊息     |
| `for`               | 重複執行         |
| `if`                | 判斷條件         |
| `else`              | 如果不是         |
| `+=`                | 加上數字         |
| `-=`                | 減掉數字         |
| `>`                 | 大於             |
| `[]`                | 列表             |
| `{}`                | 字典             |
| `lambda`            | 快速建立小函式   |

---

# 🎯 今天學到的重點

今天其實是把之前學過的 Python 基礎，組合成真正的小程式。

可以把今天的學習想成：

```text
Python 基礎
   ↓
列表、字典、if、for、while
   ↓
Streamlit
   ↓
網頁按鈕、輸入框、圖片、欄位
   ↓
session_state
   ↓
保存資料
   ↓
OpenAI API
   ↓
🤖 AI 聊天機器人
   ↓
🛒 購物平台
```

也就是說，你今天已經開始學會把**「一個一個 Python 指令」組合起來，做成真正可以操作的小型網站**了！

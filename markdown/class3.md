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

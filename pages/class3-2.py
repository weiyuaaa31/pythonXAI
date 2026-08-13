import streamlit as st

# 1. 初始化購物籃 (如果 session_state 中沒有 cart，就建立一個空 List)
if "cart" not in st.session_state:
    st.session_state.cart = []

# 2. 最上方的「重新整理」按鈕
if st.button("重新整理"):
    st.rerun()

# 3. 題目：點餐機
st.title("點餐機")

# 4. 小題目：請輸入餐點
st.subheader("請輸入餐點")

# 5. 輸入框與「加入」按鈕 (使用 st.columns 排版在同一行)
col1, col2 = st.columns([3, 1])
with col1:
    meal_input = st.text_input("請輸入餐點名稱", key="meal_input", label_visibility="collapsed")
with col2:
    if st.button("加入"):
        if meal_input:  # 確保輸入框不是空的才加入
            st.session_state.cart.append(meal_input)
            st.rerun()  # 加入後強制更新畫面

st.write("---")

# 6. 題目：購物籃
st.title("購物籃")

    
for idx, item in enumerate(st.session_state.cart):
        col_item, col_del = st.columns([3, 1])
        with col_item:
            st.write(f"{item}")
        with col_del:
            # 每個按鈕都需要唯一的 key，所以使用索引 idx (如：del_0, del_1)
            if st.button("刪除", key=f"del_{idx}"):
                st.session_state.cart.pop(idx)  # 移除指定位置的餐點
                st.rerun()  # 刪除後強制更新畫面
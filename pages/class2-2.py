import streamlit as st #匯入streamlit模組並重新命名為st

#st.number_input()可以讓使用著輸入數字，設定step=1可以讓使用者只能輸入整數
#min_value=0設定最小值0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字:", step=1, min_value=0, max_value=100)
#st.markdown()可以在網頁上使用markdown語法顯示文字
st.markdown(f"你輸入的數字是: {number}")

import streamlit as st
st.markdown("---")
st.markdown("### 練習")
a=st.number_input("請輸入你的分數", step=1, min_value=0, max_value=100)
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

st.markdown("---")
st.markdown("### 按鈕練習") 
#st.button()可以在網頁上顯示一個按鈕，使用者可以點擊按鈕
# key是按鈕的識別名稱，可以用來區分不同的按鈕 
# 如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下",key="button1")
if st.button("按我一下",key="balloons"):
             st.balloons() 
if st.button("按我一下",key="snow"):
             st.snow() 
st.markdown("---")             
                         
                      
















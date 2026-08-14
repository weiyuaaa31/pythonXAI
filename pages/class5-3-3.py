
import streamlit as st
import os

st.title("購物平台")

products = ["apple", "banana", "bg", "orange"]

product_names = {
    "apple": "🍎 蘋果",
    "banana": "🍌 香蕉",
    "bg": "🍇 葡萄",
    "orange": "🍊 柳橙"
}

prices = {
    "apple": 10,
    "banana": 10,
    "bg": 10,
    "orange": 10
}

if "stock" not in st.session_state:
    st.session_state.stock = {
        "apple": 10,
        "banana": 10,
        "bg": 10,
        "orange": 10
    }

st.write("請輸入欄位數")

column_number = st.number_input(
    "欄位數",
    min_value=1,
    max_value=4,
    value=4,
    step=1
)

cols = st.columns(column_number)

for i in range(column_number):

    product = products[i]

    with cols[i]:

        st.image(
            "image/" + product + ".png",
            width=150
        )

        st.write(product_names[product])

        st.write(
            "庫存數量：",
            st.session_state.stock[product]
        )

        st.write(
            "價格：",
            prices[product]
        )

        if st.button(
            "購買",
            key="buy_" + product
        ):

            if st.session_state.stock[product] > 0:

                st.session_state.stock[product] -= 1

                st.success("購買成功")

                st.rerun()

            else:

                st.error("沒有庫存")


st.markdown("---")


st.title("新增商品庫存")

st.write("選擇商品")

selected_product = st.selectbox(
    "商品",
    products,
    format_func=lambda x: product_names[x]
)

st.write("新增庫存數量")

add_number = st.number_input(
    "數量",
    min_value=1,
    value=1,
    step=1
)

if st.button("新增庫存"):

    st.session_state.stock[selected_product] += add_number

    st.success("新增成功")

    st.rerun()


st.markdown("---")


st.write("目前商品庫存")

for product in products:

    st.write(
        product_names[product],
        "：",
        st.session_state.stock[product],
        "個"
    )

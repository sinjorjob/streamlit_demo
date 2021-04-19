import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#    '2列目':[10,20,30,40]
#})

#st.write(df)
#st.dataframe(df, width=100, height=100)
#st.dataframe(df.style.highlight_max(axis=0))  #axis(0:行方向,1:列方向)

#st.table(df.style.highlight_max(axis=0))  #axis(0:行方向,1:列方向)



df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b','c'])

#新宿(35.69, 139.70)付近の座標を生成

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#st.map(df_map)

#画像表示on/off
if st.checkbox("Show Image"):
    img = Image.open("sample.jpg")
    # use_column_width=True アプリの幅に合わせて表示してくれる。
    st.image(img, caption='サンプル画像', use_column_width=True)  


# option = st.selectbox(
#     '好きな数字を選んで下さい',
#     list(range(1,11))
# )


# "選択した数字は", option, "です。"



# st.write('Interactive Widgets')

# text = st.sidebar.text_input("好きな言語を教えてください。")
# "好きな言語は", text, "です。"

# condition = st.sidebar.slider('今の調子は？', 0, 100, 50)   # min, max, default value
# "コンディション", condition

left_column, right_column = st.beta_columns(2)    #2カラムに定義
button = left_column.button('右カラムに文字を表示する。')
if button:
    right_column.write("右カラムに表示します。")


expander1 = st.beta_expander("問合せ1の回答を見る")
expander1.write("問合せ1の回答はAAAです。")
expander2 = st.beta_expander("問合せ2の回答を見る")
expander2.write("問合せ2の回答はBBBです。")
expander3 = st.beta_expander("問合せ3の回答を見る")
expander3.write("問合せ3の回答はCCCです。")


st.write('プログレスバーの表示')
latest_iteration = st.empty() #空のコンテナ要素を追加
bar = st.progress(0)    #バー要素を準備

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
"処理が完了しました。"
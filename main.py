import streamlit as st
import time

st.title('Streamlit 入門')



df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b','c'])

#新宿(35.69, 139.70)付近の座標を生成

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#画像表示on/off
if st.checkbox("Show Image"):
    img = Image.open("sample.jpg")
    # use_column_width=True アプリの幅に合わせて表示してくれる。
    st.image(img, caption='サンプル画像', use_column_width=True)  



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
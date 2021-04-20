import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title('米国株価可視化アプリ')

st.sidebar.write(""" 
# GAFA株価
# こちらは株価可視化ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
## 表示日数選択
 """)

# min, max, default value
# スライドバーで選択した日付をdaysに格納
days = st.sidebar.slider("日数", 1, 50, 20 )


st.write(f"""
### 過去 **{days}日間** のGAFA株価
""")


#データの取得
#キャッシュに保存して高速化（毎回取得しない）
#キャッシュクリアの機能もある
@st.cache   
def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

    
try:    
    st.sidebar.write("""
    ## 株価の範囲指定
    """)
    
    #最小値と最大値の株価が戻り値
    ymin, ymax = st.sidebar.slider(
        "範囲を指定してください",
        0.0, 3500.0, (0.0,3500.0)
    )
    
    tickers = {
            'apple': 'AAPL',
            'facebook': 'FB',
            'google': 'GOOGL',
            'microsoft': 'MSFT',
            'netflix': 'NFLX',
            'amazon': 'AMZN'
    }
    
    #株価データを取得
    df = get_data(days, tickers)
    
    
    
    #社名複数選択機能の実装
    # multiselect(説明、オプション、デフォルト値)
    companies = st.multiselect(
            '会社名を選択してください。',
            list(df.index),
            ['google', 'amazon', 'facebook', 'apple']
    )
    
    if not companies:
        st.error("少なくとも1社は選んでください")
    
    else:
        data = df.loc[companies]
        st.write("### 株価 (USD)", data.sort_index())  #表の表示
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
                columns={'value': 'Stock Prices(USD)'}
            )
        chart = (
                alt.Chart(data)
                .mark_line(opacity=0.8, clip=True)
                .encode(
                    x="Date:T",
                    y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                    color='Name:N'
                )
            )
        #グラフの描画
        # use_container_width　枠に収まるように調整する＝True
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
         "不明なエラーが発生しました"
     )   
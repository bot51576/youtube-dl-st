import time
import streamlit as st
from pytube import YouTube
from moviepy.editor import *


options = ["mp4", "mp3"]

def youtube_dl_with_st():
    yt = YouTube(input_url)
    file_name = decide_file_name()
    with st.spinner('ローディング中...'):
        yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution').desc().first() \
        .download(filename=f'{file_name}.mp4')

    st.success('ダウンロードが準備できました。') 

    if selected_option == 'mp4':
        st.video(f'{file_name}.{selected_option}')
    else:
        audioclip = AudioFileClip(f'{file_name}.mp4')
        audioclip.write_audiofile(f"{file_name}.mp3")

        # 不要なファイル（元の動画）を削除
        audioclip.close()
        os.remove(f'{file_name}.mp4')
        st.audio(f'{file_name}.{selected_option}')
    
    
def decide_file_name():
    file_name  = str(time.time())
    return file_name

st.markdown("# YouTube Downloader")
input_url = st.text_input("リンク/urlを入力してください。")
selected_option = st.selectbox('拡張子(動画・音声)', options)
st.button("スタート", on_click=youtube_dl_with_st)


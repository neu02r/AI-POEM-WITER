# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:13:25 2022

@author: jh
"""

import streamlit as st
from PIL import Image
#from pororo import Pororo 

def main():
    #st.title('AI 시인')
    st.subheader('이미지 캡셔닝')
    '이미지 캡셔닝이란 이미지의 설명문을 만들어 내는 것으로'
    '생성된 결과를 이용해 시를 만들어보세요'
    ' '
    
    

     
    
#이미지    
    #img_upload = st.file_uploader('이미지 찾아보기')
    img_url = st.text_input('이미지 url 붙여넣기')
    
    show_img = st.empty()
     
    #업로드
    
    #if img_upload:
        #bytes_img = img_upload.getvalue()
        #show_img.image(img_upload)
    
    
    #url 
    if img_url != '':
        show_img.image(img_url)    
           
        
    #캡셔닝
    #caption = Pororo(task='caption', lang='ko')
    #st.text_input(caption)
    

    '이미지 캡셔닝을 원하시면 아래 링크를 클릭하세요'
    'https://colab.research.google.com/drive/1cD_hYCFJyFSJfs3BUhceYTgkRQXtu_lF?usp=sharing'
    
        
  
    
  
if __name__ == '__main__':
    main()
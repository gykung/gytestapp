# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:01:22 2024

@author: kgua
"""

import streamlit as st


import base64
import requests

# OpenAI API Key
api_key = "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"

title = st.text_input("Your prompt:","Can you tell the gender, region?")


img_file_buffer  = st.camera_input("Take a picture")


print('here 1')
if img_file_buffer is not None:
# if img_file_buffer:
    print('here')
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer .getvalue()
    
    # Convert bytes data to base64
    base64_encoded = base64.b64encode(bytes_data).decode()

    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }

    payload = {
      "model": "gpt-4-turbo",
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": title
            },
            {
              "type": "image_url",
              "image_url": {
                "url": f"data:image/jpeg;base64,{base64_encoded}"
              }
            }
          ]
        }
      ],
      "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    print(response.json())

    st.text(response.json())

# #  python -m streamlit run "C:\Users\kgua\OneDrive - SINGAPORE REFINING COMPANY\data\openai\camera_test.py"
















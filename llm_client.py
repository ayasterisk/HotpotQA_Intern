import requests
import streamlit as st
import os

def get_api_key():
    # Ưu tiên lấy key từ st.secrets (trên Streamlit Cloud)
    try:
        return st.secrets["OPENROUTER_API_KEY"]
    except Exception:
        # Nếu chạy ở máy tính (Local) mà không có thư mục .streamlit, thì lấy từ biến môi trường
        return os.environ.get("OPENROUTER_API_KEY", "")

def generate(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # BẮT LỖI TẠI ĐÂY: Nếu có chữ "choices" thì trả về kết quả
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    
    # Nếu không có "choices", in thẳng nguyên nhân báo lỗi ra màn hình!
    raise Exception(f"Lỗi từ OpenRouter: {result}")
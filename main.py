import streamlit as st
from qa_service import answer_question

# Cài đặt tiêu đề trang web
st.set_page_config(page_title="Hệ thống Hỏi Đáp", page_icon="🤖")
st.title("Hệ thống Hỏi Đáp với Neo4j & OpenRouter")

# Tạo form nhập câu hỏi
question = st.text_input("Nhập câu hỏi của bạn vào đây:")

# Khi người dùng bấm nút "Gửi"
if st.button("Gửi câu hỏi"):
    if question.strip() == "":
        st.warning("Vui lòng nhập câu hỏi trước khi gửi!")
    else:
        # Hiển thị vòng xoay chờ đợi trong lúc xử lý
        with st.spinner("Hệ thống đang suy nghĩ..."):
            try:
                # Gọi hàm xử lý từ file qa_service của bạn
                answer = answer_question(question)
                
                # In câu trả lời ra màn hình
                st.success("Đã tìm thấy câu trả lời!")
                st.write(answer)
                
            except Exception as e:
                st.error(f"Có lỗi xảy ra trong quá trình xử lý: {e}")
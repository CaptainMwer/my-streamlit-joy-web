# 1. 导入相关包，如streamlit包
import streamlit as st
# from langchain.memory import ConversationBufferMemory
from my_utils import get_response

# 3. 主界面主标题
st.title("T801")

# 5. 会话保持：用于存储会话记录
if "messages" not in st.session_state:# {"memory":缓冲区}
    st.session_state['messages'] = [    # 存了字典列表
        {'role': 'assistant', 'content': '你好，我是神秘人，有什么可以帮助你的么？'},
    ]

# 6. 编写一个循环结构，用于打印会话记录
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 4. 创建一个聊天窗口
prompt = st.chat_input("请输入您要咨询的问题：")   # 最底端
# 7. 如果文本框有数据，继续向下执行
if prompt:
    st.session_state['messages'].append({'role': 'user', 'content': prompt})
    st.chat_message("user").markdown(prompt)    # 消息框+内容
    # 10. 向utils工具箱发起请求，返回响应
    with st.spinner("AI小助手正在思考中..."):
        content = get_response(st.session_state['messages'])
    st.session_state['messages'].append({'role': 'assistant', 'content': content})
    st.chat_message("assistant").markdown(content)
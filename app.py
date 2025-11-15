from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

def call_llm(input_text, expert_choice):
    if expert_choice == "育児":
        system_content = "あなたは育児の専門家です。親切で分かりやすく回答してください。"
    else:
        system_content = "あなたは健康の専門家です。親切で分かりやすく回答してください。"
    
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_text)
    ]
    
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    response = llm.invoke(messages)
    return response.content

st.title("サンプルアプリ: LLM機能を搭載したWebアプリ")
input_message = st.text_input(label="質問を入力してください。")
expert_choice = st.radio(label="専門家を選択してください。", options=["育児", "健康"])

if st.button("実行"):
    if input_message:
        with st.spinner("回答を生成中..."):
            response = call_llm(input_message, expert_choice)
        st.subheader("回答:")
        st.write(response)
    else:
        st.warning("質問を入力してください。")

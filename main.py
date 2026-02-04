import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_classic.agents import AgentExecutor, create_openai_tools_agent
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic import hub 
from langchain_community.tools import DuckDuckGoSearchRun
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="Knowledge Bot", page_icon="🤖")
st.title("Free Conversational Knowledge Bot")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    temperature=0.2,
    google_api_key="AIzaSyAk7cKug7HDSW4KzNYdmNnLKP4O2iF4YEQ",
    max_output_tokens=4096,
    google_thinking_config={"thinking_budget": 0}
    

)
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True
    )
prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=st.session_state.memory, 
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
    
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt_input := st.chat_input("Ask me anything for free..."):
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    with st.chat_message("user"):
        st.markdown(prompt_input)

    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            try:
                response = agent_executor.invoke({"input": prompt_input})
                raw_output = response["output"]

            
                
                if isinstance(raw_output, list):
                    answer = "".join([part.get("text", "") for part in raw_output if isinstance(part, dict)])
                else:
                    answer = raw_output

                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"An error occurred: {e}")
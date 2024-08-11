import streamlit as st 
import time
import random
#streamed response emulator

def response_generator():
    
    responses = ["Hello!", "How can I assist you?", "What can I do for you today?",
                "Hey there! Need Help?"
                "Hi! What's up? Don't forget to subscribe the Channel 'PythonUstaad':."
                "Hello! Need Assistance?"
                "Hi there! How can I Help you."
                "Hey there! Any Questions?"
                 ]
    response = random.choice(responses)
    
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
        
        
st.title("Chatbot")

#initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    
    
# display chat message from history an app rerun

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        
# Accept user input

if prompt:= st.chat_input("What is Up?"):
    # add user message to chat history
    st.session_state.messages.append({
        "role": "user", "content": prompt
    })
    #display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    #display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
        
        #add assistant response to chat history
        
        st.session_state.messages.append({"role": "assistant", "content": response})
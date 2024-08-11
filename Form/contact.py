import streamlit as st 
import re
import requests

WEBHOOK_URL = ""

def is_valid_email(email):
    # Basic regex pattern for email validation
    
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None


def contact_form():
    with st.form("Contact Form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
    
        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again later.", icon='😊')
                st.stop()
            
            if not name:
                st.error(" Please Provide your Beautiful name.", icon='😊')
                st.stop()
                
            if not email:
                st.error(" Please Provide your Email Address.", icon='😊')
                st.stop()
                
            if not is_valid_email(email):
                st.error(" Please Provide a Valid Email Address.", icon='😊')
                st.stop()
                
            if not message:
                st.error(" Please Provide a Message.", icon='😊')
                st.stop()
            
            
            
            #prepare the data payload and send it to the specified webhook url
            
            data = {"email":email,
                    "name": name,
                    "message": message
                }
            
            response = requests.post("WEBHOOK_URL", json=data)
            
            if response.status_code == 200:
                st.success("Your message has been sent Successfully!🥳🎇", icon="🎇")
                
            else:
                st.error("There was an error sending your Message.", icon = "😨")
                
            
    

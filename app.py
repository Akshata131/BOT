import streamlit as st
import openai

openai.api_key = "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"

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image:linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75)),url("https://www.syncfusion.com/blogs/wp-content/uploads/2020/01/tile.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.markdown("<h1 style='text-align: center; color: blue;font-size:80px'>Edtech Chatbot</h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
query  = st.text_area("Enter Your Query")
button = st.button("Your Answer")

def generate_reply(query):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"This following is a conversation between User and Edtech-Bot. \nEdtech-Bot is a highly intelligent question answering bot. If you ask him a question that is rooted in truth, It will give you the answer related to data science field. \n\nUser:{query}\n\nEdtech-Bot:",
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    # st.write(response)
    return response.choices[0].text

if button and query:
    with st.spinner("Generating Answer..."):
        reply = generate_reply(query)
    st.write(reply)
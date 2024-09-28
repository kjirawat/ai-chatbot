import streamlit as st

st.title("🎈 My chatbot app")
# st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

#if user_input := st.text_input("You: ", placeholder="Type your message here..."):
#    st.write(f"User Input: {user_input}")

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)

#st.text_input()
#s1 = st.text_input()
#st.write(s1)
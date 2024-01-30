import streamlit as st
import google.generativeai as genai
# streamlit run app1.py

GOOGLE_API_KEY = "AIzaSyB97JQ-JAt0OOhURhdCbqWHYhrATlAzo4s"

genai.configure(api_key = GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="Friday Query Genrator ", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>SQL Query Generator</h1>
                <h3>I can generate SQL queries for you!</h3>
                <h4>With Explanation as well!!!</h4>
                <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
    text_input = st.text_area("Enter your Query here in English:")

    submit = st.button("Generate SQL Query")
    if submit:
        response = model.generate_content(text_input)
        print(response.text)
        st.write(response.text)




main()
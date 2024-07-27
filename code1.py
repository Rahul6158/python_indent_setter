import streamlit as st
import autopep8

def format_code(code):
    """Format the given code using autopep8."""
    formatted_code = autopep8.fix_code(code, options={'aggressive': 1})
    return formatted_code

def main():
    st.title("Code Indentation Formatter with autopep8")

    st.write("### Enter your code snippet below:")
    code = st.text_area("Code", height=300)

    if st.button("Format Code"):
        if code:
            formatted_code = format_code(code)
            st.write("### Reformatted Code:")
            st.code(formatted_code, language='python')
        else:
            st.warning("Please enter some code.")

if __name__ == "__main__":
    main()

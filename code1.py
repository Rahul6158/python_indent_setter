import streamlit as st
import autopep8

def format_code(code):
    """Format the given code using autopep8."""
    formatted_code = autopep8.fix_code(code, options={'aggressive': 1})
    return formatted_code

def main():
    st.title("Code Indentation Formatter")

    st.write("### Enter your code snippet below:")
    code = st.text_area("Code", height=300)

    st.write("### Set the desired indentation level:")
    indent_level = st.slider("Indentation Level", min_value=0, max_value=10, value=4)

    if st.button("Format Code"):
        if code:
            formatted_code = format_code(code)
            st.write("### Reformatted Code:")
            st.code(formatted_code)
        else:
            st.warning("Please enter some code.")

if __name__ == "__main__":
    main()

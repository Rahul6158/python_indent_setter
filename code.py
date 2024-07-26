import streamlit as st
import textwrap

def adjust_indentation(code, indent_level):
    """Adjust the indentation of the given code snippet."""
    # Calculate the indentation string based on the number of spaces
    indent_string = ' ' * indent_level
    # Split the code into lines and add the indentation to each line
    indented_code = '\n'.join([indent_string + line for line in code.split('\n')])
    return indented_code

def main():
    st.title("Code Indentation Formatter")

    st.write("### Enter your code snippet below:")
    code = st.text_area("Code", height=300)

    st.write("### Set the desired indentation level:")
    indent_level = st.slider("Indentation Level", min_value=0, max_value=10, value=4)

    if st.button("Format Code"):
        if code:
            indented_code = adjust_indentation(code, indent_level)
            st.write("### Reformatted Code:")
            st.code(indented_code)
        else:
            st.warning("Please enter some code.")

if __name__ == "__main__":
    main()

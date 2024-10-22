import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for the two numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number", value=0.0, step=0.1)

    # Operation selection
    operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Perform calculation
    result = None
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")

    # Display the result
    if result is not None:
        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()

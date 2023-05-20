import streamlit as st
st.title('This is first Basic Application')

st.subheader('Sum & Subtract Two Numbers')

operation = st.selectbox('Select Operation', ['Sum', 'Subtract'])

num1 = st.number_input('Enter first Number')
num2 = st.number_input('Enter Second Number')

if operation == "Sum":
    operation_of_two_numbers = num1 + num2
else:
    operation_of_two_numbers = num1 - num2



st.write(operation_of_two_numbers)


st.subheader('Predict salary')
st.subheader('Predict salary based on Experience of Candidate')

#User Input
name = st.text_input('Enter Name')
experience = st.number_input('Enter Experience (in Years)')



# Model
predicted_salary = 1.71 * experience + 1.471

# displaying the Predicted Output
st.write(name + 's Predicted salary (in lakhs)')
st.write(predicted_salary)




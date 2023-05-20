
import pandas as pd
import streamlit as st
import joblib

st.title('Predict Customer Loyality')

st.subheader('Is your customer loyal to you?')

#User Input
Customer_Age = st.number_input('Enter age')
Credit_Limit = st.number_input('Enter Credit Limit [Between 1450 - 13500]')
Total_Trans_Amt = st.number_input('Enter Tital Transaction Amount[Between 500 - 18500]')
Gender_F = st.number_input('1 - if Female/ else 0')
Gender_M = st.number_input('1 - if Male/ else 0')
Income_Category_120K = st.number_input('1 if Income Greater then $120k/ else 0')
Income_Category_40Kto60K=st.number_input('1 if Income Between $40k-$60k/ else 0')
Income_Category_60Kto80K=st.number_input('1 if Income Between $60k-$80k/ else 0')
Income_Category_80Kto120K=st.number_input('1 if Income Between $80k-$120k/ else 0')
Income_Category_Less_than_40K=st.number_input('1 if Income less than $40k/ else 0')
Income_Category_Unknown =st.number_input('1 If no Info about income/ else 0')
Card_Category_Blue=st.number_input('1 If Card is Blue/ else 0')
Card_Category_Gold =st.number_input('1 If Card is gold/ else 0')
Card_Category_Platinum =st.number_input('1 If Card is Platinum/ else 0')
Card_Category_Silver =st.number_input('1 If Card is Silve/ else 0')


#Create Input DataFrame

New = pd.DataFrame({'Customer_Age':[Customer_Age], 'Credit_Limit':[Credit_Limit], 'Total_Trans_Amt':[Total_Trans_Amt], 'Gender_F':[Gender_F],
       'Gender_M':[Gender_M], 'Income_Category_$120K +':[Income_Category_120K], 'Income_Category_$40K - $60K':[Income_Category_40Kto60K],
       'Income_Category_60Kto80K':[Income_Category_60Kto80K], 'Income_Category_$80K - $120K':[Income_Category_80Kto120K],
       'Income_Category_Less than $40K':[Income_Category_Less_than_40K], 'Income_Category_Unknown':[Income_Category_Unknown],
       'Card_Category_Blue':[Card_Category_Blue], 'Card_Category_Gold':[Card_Category_Gold], 'Card_Category_Platinum':[Card_Category_Platinum],
       'Card_Category_Silver':[Card_Category_Silver]
        })


#Import
Prediction = joblib.load('Model/Retention.pkl')

#Model
Customer_Nature = Prediction.predict(New)

# Displaying the Predicted Output
st.write('This is a - ')
st.write(Customer_Nature)



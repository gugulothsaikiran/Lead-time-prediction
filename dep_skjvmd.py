import pickle 
import streamlit as st
import pandas as pd
st.title("Lead time prediction RINL")
catalog_numbers=pd.read_csv("cat_num.csv")
with open('dt_model.pkl', 'rb') as file:
    dt_model = pickle.load(file)




catalog_no_input = st.selectbox("Select Catalog Number", catalog_numbers)
indent_dt_input = st.date_input("Indent Date (YYYY-MM-DD)")
button = st.button("Predict")
if button:
    
    if indent_dt_input and catalog_no_input:
        try:
            indent_dt_input = pd.to_datetime(indent_dt_input)
            cat_input = catalog_numbers[catalog_numbers.iloc[:,0]==catalog_no_input].index[0] 
            prediction = dt_model.predict([[cat_input]])
            reciept_date = indent_dt_input + pd.Timedelta(days=int(prediction))
            st.header("Predicted Material Receipt Date")
            st.write(reciept_date.strftime("%Y-%m-%d"))
    
        except Exception as e:
            st.error("Error occured. Please check the input and try again")
            st.error(str(e))
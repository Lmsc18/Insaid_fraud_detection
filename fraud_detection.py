import streamlit as st
import pickle

st.header("Fraud Prediction Application")



col1, col2,col3= st.columns(3)

with col1:
    types= col1.selectbox(
    'Select the type of transaction',
    ('CASH_OUT', 'PAYMENT', 'CASH_IN', 'TRANSFER', 'DEBIT'))

with col2:
    amount= st.number_input('Enter the amount')

with col3:
    iff=col3.selectbox('Is the amount greater than 200000',
                       ('YES','NO'))
    


col1, col2,col3= st.columns(3)

with col1:
    new_bal = st.number_input('Balance of the sender after transaction')
with col2:
    old_bal = st.number_input('Balance of the reciever before transaction')

encode_dict = {
   'tp':{
    'CASH_OUT':1,
    'PAYMENT':2,
    'CASH_IN':3,
    'TRANSFER':4,
    'DEBIT':5
},
    "iff": {"YES": 1, "NO": 0}
}

def model_pred(types,amount,iff,new_bal,old_bal):

    with open("classifier.pkl", "rb") as file:
        model = pickle.load(file)
    
    input_ftrs = [[293.632,types,amount,0.002044,new_bal,0.05917,old_bal,iff]]
    return model.predict(input_ftrs)

if st.button("Predict"):
    types = encode_dict['tp'][types]
    iff = encode_dict['iff'][iff]

    price = model_pred(types,amount,iff,new_bal,old_bal)
    res=''
    if price ==0:
        res='NOT FRAUD'
    if price==1:
        res='FRAUD'
    st.text("Result of the prediction: "+ res)
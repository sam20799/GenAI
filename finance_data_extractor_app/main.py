import streamlit as st
from data_extractor import extractor
import pandas as pd

st.title("Financial Data Extractor")

article = st.text_area("Enter your article ")

if st.button("Extract"):
    if article:
        extracted_data = extractor((article))
        data = {
            'Measure':['Revenue','EPS'],
            'Estimated':[extracted_data['revenue_expected'],extracted_data['eps_expected']],
            'Actual':[extracted_data['revenue_actual'],extracted_data['eps_actual']]
        }

        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("No article given")


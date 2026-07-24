import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st

st.title(':zap: Pytopia Dashboard')

with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

with st.expander('User Profile:'):
    col1, col2 = st.columns(2)

    col1.text_input('Name:')
    col2.text_input('Age:')

    st.camera_input('Camera Input', key='camera_input')
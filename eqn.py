import st as st
import streamlit
import streamlit as st
import pandas as pd
import streamlit as st
from PIL import Image

st.title("atomic structure of elements")
st.header("python for elements")
df = pd.read_csv('../Periodic Table of Elements.csv')
st.dataframe(df)
atom_name = st.selectbox("Select Name of element : ", (df.iloc[:,1]))
#atom_name = st.selectbox("which property of elementes you want",('Phase','atomic radius','boiling point','melting point','density',(df.iloc[:,1])))
if (st.button('Show')):
    st.write(atom_name)
    # st.dataframe(df[df['Element'] == atom_name])
    dff = st.dataframe(df[df['Element']== atom_name])
    #st.write()
    for i in df[df['Element'] == atom_name].iloc[:, -1]:
        print(i)
    image = Image.open(i)
    st.image(image)

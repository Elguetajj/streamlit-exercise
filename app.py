import streamlit as st
import pandas as pd
import numpy as np


st.title('K onda prro')

x = st.slider('x')
st.write(x, 'square', x*x)


st.write('Dataframe')
st.write(pd.DataFrame({
    'column':[1,2,3,4,5],
    'column2': [10,20,30,40,50]

}))


"""
# Otra manera de escribir titulos

Line Graph

"""
  
df = pd.DataFrame({
    'column':[1,2,3,4,5],
    'column2': [10,20,30,40,50]

})


if st.checkbox('Show dataframe'):
  
    df



"""
# Graphs

Line Graph
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)







chart_data = pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.76,-122.4],
    columns=["lat","lon"]
)

st.map(chart_data)


option = st.selectbox(
    'Which number do you like best?',
     df['column'])

'You selected: ', option


option_side = st.sidebar.selectbox(
    'Which number do you like best?',
     ["hello", "world", "!"])

'You selected:', option_side

import time
'Starting a long computation...'

# Initializing the variables
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}%')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
# https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import graphviz
import random
import numpy as np

#Title
st.title("Hello World!")

#Header
st.header("This is a header")

#subheader
st.subheader("This is a subheader")

#success, info & warning
st.success("Executed successfully")
st.info("Informational")
st.warning("Warning!")
st.error("Error message")

#write
st.write("See code below")
st.write(range(20))

#code
code = '''
            for 1 in range(10):
                print(i)
'''

st.code(code, language='python')

#checkbox
if(st.checkbox("Pick me")):
    st.text("Selected!")

#radio button
val = st.radio("Choose one: ", ('yes','no'))
st.write("You selected: ", val)

#dropdown
option = st.selectbox("Select an option", ['','option 1','option 2','option 3'])
st.write("You selected: ", option)

options = st.multiselect("Select multiple options", ['option 1','option 2','option 3'])
st.write("You selected: ")
for o in options:
    st.write(o)

name = st.text_input("What is your name? ", "[enter your name]")
st.write("Your name is: ", name)

if(st.button("Click me!")):
    st.write("Thank you for clicking me!")

n = st.slider("How much did you like this tutorial?", 1, 5)
st.write(n)

# cookies
st.context.cookies
#st.context.cookies["_ga"]
sessioncookie = st.context.cookies["session_"]

# help with a python function
# st.help(pd.DataFrame)

# from PIL import Image                          
#image
# img = Image.open("image.jpg")
# st.image(img)


# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge("node 1", "node 2")
graph.edge("node 2", "node 3")
graph.edge("node 3", "node 1")
graph.edge("node 4", "node 2")

st.graphviz_chart(graph)

# displaying data
df = pd.DataFrame(
    {
        "name": ["S&P500", "Nasdaq", "Oil"],
        "url": ["url1.com", "url2.com", "url3.com"],
        "stars": [random.randint(0, 100) for _ in range(3)],
        "views_history": [[random.randint(0, 100) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "ETF",
        "stars": st.column_config.NumberColumn(
            "Buy Rating",
            help="Buy Rating based on stars",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("Fund URL"),
        "views_history": st.column_config.LineChartColumn(
            "Prices (past 30 days)", y_min=0, y_max=100
        ),
    },
    hide_index=True,
)

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))
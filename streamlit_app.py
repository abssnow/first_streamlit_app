import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry oatmeal')
streamlit.text('🥗 Kale Spinach and Rocket muesli')
streamlit.text('🐔 Hard Boiled free range egg')
streamlit.text('🍞 Avocado toast')
 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') 

#lets put a pick list so they can pick the fruit they want to list
streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])

# display the data on the page
streamlit.dataframe(my_fruit_list)


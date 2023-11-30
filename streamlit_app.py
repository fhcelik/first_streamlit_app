#created the main python file.
import streamlit
import pandas

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read.csv("https://uni-lab-files.s3.ca-central-1.amazonaws.com//dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

import jokeapi
from jokeapi import Jokes
import streamlite as st

j = Jokes()  # Initialise the class

categories=["programming","dark","spooky","misc","pun","christmas"] #variable with all joke categories
flags=['nsfw', 'religious', 'political', 'racist', 'sexist', 'explicit'] #variable with all joke flags 
selectedCat=[] #empty list for the categories
selectedBlack=[] #empty list for flags

for i in categories: #loop to let the user choose between each categories
        print("Do you want this kind of jokes: ",i,"? [y/n]") 
        if input() == 'y':
            selectedCat.append(i) #return the selected categories



for i in flags: #loop to let the user select the flags
        print("Do you want this kind of jokes: ",i,"? [y/n]")
        if input() == 'n':
            selectedBlack.append(i) #return the selected flags



print("Select a joke type (single,twopart):")
jokeType=input() #let the user select the type of joke
joke = j.get_joke(category=selectedCat,blacklist=selectedBlack,joke_type=jokeType)  # Retrieve a dark programming joke
#joke = j.get_joke()  # Retrieve a random joke

if joke["type"] == "single": #Check if the joke is a one-liner
    print(joke["joke"]) # Print the joke
else: # if the joke is in the format setup/delivery:
    print(joke["setup"]) # Print the jokes' setup
    print(joke["delivery"]) # Print the jokes' delivery
    
#streamlite GUI to select a joke
st.title("Some jokes")
title = st.text_input('Enter the category of the joke you want, if do not want a specific type leave it blank', '')

if st.button('Say hello to google'):
    st.write('Request sent')
else:
    st.write('Request not sent')
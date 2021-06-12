# DUBOIS_LORRAIN_Joke

Authors: DUBOIS Hadrien
         LORRAIN Yvan

======================================================================================
                             |      Requirements      |
======================================================================================

Install pip: python -m pip --version
Install jokeapi: pip install jokeapi

======================================================================================
                             |      The app      |
======================================================================================

The app is based on jokeapi, the api allows us to get jokes according to certain 
criterias.

This app allows the user to send a request to get jokes. The user can select the type,
the format and blacklist certain kinds of jokes.

======================================================================================
                             |      How to use it?      |

When launching the application you will be asked a set of questions to define the type
of jokes you will be sent. THose are claused question to whiwh you will answer "yes"
by typing "y" or "n" to answer "no".

Once you answered all the questions you will be served a very fine joke! To send it
to your friends you just need to copy the joke and paste it in your favourite chating
app and that's it!

======================================================================================
                             |      How it works?      |
======================================================================================

Jokeapi provides a set functions that allows us to retrieve joke directly from the 
api. 

We manly used the get_joke() function. The function performes a GET request to the 
database containing the jokes and then retrieves the content which comes in a json
format. As get_joke() only returns the joke it means the function then "looks" into
the content of the GET response and only retrieves the part labeled "joke".

To look for specific types of jokes we make use of the certain caracteristics that 
are arguments of get_joke(). We let you check the code to see that.

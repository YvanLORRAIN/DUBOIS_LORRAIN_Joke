import streamlit as st
import logging
import requests
from html import unescape
import streamlit.components.v1 as components
import pytrends
from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt
import timecounter
from timecounter import generateDictionnary, counting


logging.warning("It's a trap!")

st.title("Hello world")
title = st.text_input('A meme', 'Hello there')

if st.button('Say hello to google'):
	st.write('Request to google sent')
	req=requests.get("https://www.google.com/")
	req2 =requests.get("https://analytics.google.com/analytics/web/?pli=1#/report-home/a197552790w273202703p243378564")
	st.markdown(req.cookies._cookies)
	st.text(req2.status_code)
	st.markdown(req2.text)
	components.html(unescape(req.text))
else:
	st.write('Request not sent')
	

df=pandas.DataFrame() 
pytrend = TrendReq()

pytrend = TrendReq(hl='en-US', tz=360)

kw = ["Obi-Wan Kenobi","Star Wars"]
df=pytrend.build_payload(kw, timeframe='today 3-m', geo='FR', gprop='')

df=pytrend.interest_over_time()
st.line_chart(df)

nb_diction = []
nb_counting = []
text=open('shakespeare.txt','r')
for i in range(100):
	nb_diction.append(generateDictionnary(text))
	nb_counting.append(counting(text))



import os
import re
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-197552790-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-197552790-1');
</script>"""
a=os.path.dirname(st.__file__) + '/static/index.html'
with open(a, 'r') as f:
	data=f.read()
	if len(re.findall('UA-', data)) == 0:
		with open(a, 'w') as f:
			newdata=re.sub('<head>','<head>' + code, data)
			f.write(newdata)


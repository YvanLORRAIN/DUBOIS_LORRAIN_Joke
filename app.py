import streamlit as st
import logging
import requests
from pytrends.request import TrendReq


pytrends = TrendReq(hl='en-US', tz=360)
pytrends.trending_searches(pn='Obi-Wan Kenobi')

logging.warning("It's a trap!")

st.title("Hello world")
title = st.text_input('A meme', 'Hello there')

if st.button('Say hello to google'):
	st.write('Request to google sent')
	req=requests.get("https://www.google.com/")
	req2 =requests.get("https://analytics.google.com/analytics/web/?pli=1#/report-home/a197552790w273202703p243378564")
else:
	st.write('Request not sent')
	
st.markdown(req.cookies._cookies)
st.text(req2.status_code)
st.markdown(req2.text)

from html import unescape
import streamlit.components.v1 as components
components.html(unescape(req.text))

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


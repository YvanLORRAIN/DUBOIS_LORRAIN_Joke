import streamlit as st
import logging

logging.warning("It's a trap!")

st.title("Hello world")
title = st.text_input('A meme', 'Hello there')

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


import streamlit as st

# Import google analytics
import os
import re
code = """<!-- Global site tag (gtag.js) - Google Analytics -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXXXX-4"></scrip
t>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-197462138-1');
</script>"""
a=os.path.dirname(st.__file__) + '/static/index.html'
with open(a, 'r') as f:
	data=f.read()
	if len(re.findall('UA-', data)) == 0:
		with open(a, 'w') as f:
			newdata=re.sub('<head>','<head>' + code, data)
			f.write(newdata)

			st.title("Hello world")

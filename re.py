
#爬虫
#1. get html Text

# 2 <span class="top_score">7315</span>

import re
import urllib.request

# 1 get html Text
r = urllib.request.urlopen("http://118.31.19.120:3000/")
#html = str(html)
# html =  """<span class="top_score">7315</span>
#         <span class="top_score">7316</span>
#         <span class="top_score">73</span>
#         <span class="top_score">715</span>
#         <span class="top_score">15</span>"""

# 2 <span class="top_score">7315</span>
html = r.read().decode('utf-8')



res = re.findall('<span class="top_score">(.*?)</span>',html)
print(res)
import requests


PAGE_URL = 'http://google.com'


resp =  requests.get(PAGE_URL)
html_str = resp.content.decode()
print(html_str)
print(resp.status_code)
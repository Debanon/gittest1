import requests
r = requests.get('http://www.tomsguide.com/')

header_list = ['Server', 'Date', 'X-Country-Code', 'Connection', 'Content-Length']

for header in header_list:
   try:
      result = r.headers[header]
      print ('%s: %s' % (header, result))
   except Exception as err:
      print ('%s: No Details Found' % header)


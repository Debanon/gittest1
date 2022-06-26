# Task 2: Footprinting HTTP Headers
#Name: Debanon Datta

import requests #making http request
r = requests.get('http://www.tomsguide.com/')

#generate a list of headers about which we need the information
header_list = ['Server', 'Date', 'X-Country-Code', 'Connection', 'Content-Length']

#try and except block
for header in header_list:
   try:
      result = r.headers[header]
      print ('%s: %s' % (header, result))
   except Exception as err:
      print ('%s: No Details Found' % header)

#End
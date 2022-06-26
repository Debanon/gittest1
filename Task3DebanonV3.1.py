#Step1:
#Task 3: Test security of Web Server Configurations
#Name: Debanon Datta
#Version: 1.0

import requests #making http request

fname1 = 'ServerList.txt'

#try and except block nested
try:
    f1 = open(fname1, 'r') #Open file and returns the content in the form of a string.
    for line in f1.readlines(): #line gets an iten from a list
        line = line.strip() #
        req = requests.get(line) #request the resource
        print(line, 'report:')

        # 01: check sequrity heade for Content-Security-Policy
        try:
            content_security = req.headers['Content-Security-Policy']
            print('Content-Security-Policy set:', content_security)
        except KeyError:
            print('Content-Security-Policy missing')

            # 02: check sequrity heade for Strict-Transport-Security
        try:
            transport_security = req.headers['Strict-Transport-Security']
            print('Strict-Transport-Security set:', transport_security)
        except KeyError:
            print('HTTPS header not set properly, Man-in-the-middle attacks and cookie hijacking is possible')

            # 03 check sequrity heade for X-Content-Type-Options
        try:
            options_content_type = req.headers['X-Content-Type-Options']
            if options_content_type != 'nosniff':
                print('X-Content-Type-Options not set properly:', options_content_type)
        except KeyError:
            print('X-Content-Type-Options not set')

except FileNotFoundError:
    print('There is no such file:', fname1)

#End
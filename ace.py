#!/usr/bin/env python
import sys,requests,json

COMPILE_URL = 'http://api.hackerearth.com/code/compile/'
RUN_URL = 'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '080b41aef659ecc3bbd90e8d0804d40c9c437ab2'

languages={'c':"C",'cc':"CPP",'cpp':"CPP11",'clj':"CLOJURE",'cs':"CSHARP",'java':"JAVA",'js':"JAVASCRIPT",'hs':"HASKELL",'pl':"PERL",'php':"PHP",'py':"PYTHON",'rb':"RUBY"}



filename = str(sys.argv[1])          #filename
ftemp=filename.strip('\n')
refilename=ftemp[::-1]
temp=refilename.split('.',1)

extension=temp[0][::-1]             #file extension

source=open(filename,'r+').read()


#print source
data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source,
    'lang':languages[extension],
    'time_limit': 5,
    'memory_limit': 262144,
}

response = requests.post(RUN_URL, data=data)
data=json.loads(response.text)
#print data
run_status = data.get('run_status')
#print run_status
o=run_status['output']
print o                      #output


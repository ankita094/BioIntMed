##REST API of Kegg from http://exploringlifedata.blogspot.com/
#Python 3.6.5 |Anaconda, Inc.

import collections
from restful_lib import Connection

kegg_url = "http://rest.kegg.jp"
conn = Connection(kegg_url)

data = conn.request_get('list/ko', headers={'Accept':'text/json'})
print(data['headers'])
print(type(data['body']))


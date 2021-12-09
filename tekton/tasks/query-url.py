#from urllib.parse import parse_qs

import urllib.parse as urlparse
import sys

extra_data = {}

#q = '/?TYPE=microservice&APP=demo-webserver'
q = '/?TYPE=microservice'

# Extract params from webhook
parsed = urlparse.urlparse(q)
p      = parsed.query.split('&')

for i in p:
   d = i.split("=")
   extra_data[d[0]] = d[1]

print(extra_data)
sys.exit(0)

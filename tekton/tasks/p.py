from urllib.parse import parse_qs

import urllib.parse as urlparse
import requests
import json
import os
import sys
import yaml

token = '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'
#token     = os.environ.get('GITHUB_TOKEN')
headers   = {"Authorization": "token {}".format(token)}
#file_payload = "$(workspaces.github.path)/$(params.GITHUB_FILE_PAYLOAD)"
file_payload = "github-payload.conf"
file_params = "github-webhook-params.conf"
payload   = None
hooks     = []
params    = []

if token == None:
   print("[ERROR] Unable to find GitHub token")
   sys.exit(1)

try:
   f = open(file_payload, "r")
   payload = yaml.load(f)
   f.close()

   #payload = json.loads(github_payload)
except Exception as e:
   print("[ERROR] {}".format(e))
   sys.exit(1)

if not 'repository' in payload:
   print("[ERROR] Unable to find 'repository' in payload")
   sys.exit(1)

if not 'hooks_url' in payload['repository']:
   print("[ERROR] Unable to find 'hooks_url' in payload")
   sys.exit(1)

hooks_url = "{}".format(payload['repository']['hooks_url'])

try:
   r    = requests.get(hooks_url, headers=headers)
   data = json.loads(r.content.decode("UTF-8"))

   for h in data:
      if 'config' in h and 'url' in h['config']:
         hooks.append(h['config']['url'])
except Exception as e:
   print("[ERROR] {}".format(e))
   sys.exit(1)

# Extract params from webhooks
for u in hooks:
   parsed = urlparse.urlparse(u)
   p      = parsed.query.split('&')

   for d in p:
      params.append(d)

try:
   f = open(file_params,"w")

   for p in params:
      f.write("{}\n".format(p))

   f.close()
except Exception as e:
   print("[ERROR] {}".format(e))
   sys.exit(1)

sys.exit(0)

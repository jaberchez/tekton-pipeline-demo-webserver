#! /usr/bin/env python3

from urllib.parse import parse_qs

import urllib.parse as urlparse
import requests
import json
import os
import sys
import yaml
import re

payload_str = '''
{  "ref": "refs/heads/test-webhook",  "before": "49b50e0b72dc6c292c9c1b1f4e80e39280a28a94",  "after": "018b8a6f978affda063b7ba857ea4d66cd34a20a",  "repository": {    "id": 336481268,    "node_id": "MDEwOlJlcG9zaXRvcnkzMzY0ODEyNjg=",    "name": "demo-webserver",    "full_name": "jaberchez/demo-webserver",    "private": false,    "owner": {      "name": "jaberchez",      "email": "44943862+jaberchez@users.noreply.github.com",      "login": "jaberchez",      "id": 44943862,      "node_id": "MDQ6VXNlcjQ0OTQzODYy",      "avatar_url": "https://avatars.githubusercontent.com/u/44943862?v=4",      "gravatar_id": "",      "url": "https://api.github.com/users/jaberchez",      "html_url": "https://github.com/jaberchez",      "followers_url": "https://api.github.com/users/jaberchez/followers",      "following_url": "https://api.github.com/users/jaberchez/following{/other_user}",      "gists_url": "https://api.github.com/users/jaberchez/gists{/gist_id}",      "starred_url": "https://api.github.com/users/jaberchez/starred{/owner}{/repo}",      "subscriptions_url": "https://api.github.com/users/jaberchez/subscriptions",      "organizations_url": "https://api.github.com/users/jaberchez/orgs",      "repos_url": "https://api.github.com/users/jaberchez/repos",      "events_url": "https://api.github.com/users/jaberchez/events{/privacy}",      "received_events_url": "https://api.github.com/users/jaberchez/received_events",      "type": "User",      "site_admin": false    },    "html_url": "https://github.com/jaberchez/demo-webserver",    "description": "Web server example written in Go",    "fork": false,    "url": "https://github.com/jaberchez/demo-webserver",    "forks_url": "https://api.github.com/repos/jaberchez/demo-webserver/forks",    "keys_url": "https://api.github.com/repos/jaberchez/demo-webserver/keys{/key_id}",    "collaborators_url": "https://api.github.com/repos/jaberchez/demo-webserver/collaborators{/collaborator}",    "teams_url": "https://api.github.com/repos/jaberchez/demo-webserver/teams",    "hooks_url": "https://api.github.com/repos/jaberchez/demo-webserver/hooks",    "issue_events_url": "https://api.github.com/repos/jaberchez/demo-webserver/issues/events{/number}",    "events_url": "https://api.github.com/repos/jaberchez/demo-webserver/events",    "assignees_url": "https://api.github.com/repos/jaberchez/demo-webserver/assignees{/user}",    "branches_url": "https://api.github.com/repos/jaberchez/demo-webserver/branches{/branch}",    "tags_url": "https://api.github.com/repos/jaberchez/demo-webserver/tags",    "blobs_url": "https://api.github.com/repos/jaberchez/demo-webserver/git/blobs{/sha}",    "git_tags_url": "https://api.github.com/repos/jaberchez/demo-webserver/git/tags{/sha}",    "git_refs_url": "https://api.github.com/repos/jaberchez/demo-webserver/git/refs{/sha}",    "trees_url": "https://api.github.com/repos/jaberchez/demo-webserver/git/trees{/sha}",    "statuses_url": "https://api.github.com/repos/jaberchez/demo-webserver/statuses/{sha}",    "languages_url": "https://api.github.com/repos/jaberchez/demo-webserver/languages",    "stargazers_url": "https://api.github.com/repos/jaberchez/demo-webserver/stargazers",    "contributors_url": "https://api.github.com/repos/jaberchez/demo-webserver/contributors",    "subscribers_url": "https://api.github.com/repos/jaberchez/demo-webserver/subscribers",    "subscription_url": "https://api.github.com/repos/jaberchez/demo-webserver/subscription",    "commits_url": "https://api.github.com/repos/jaberchez/demo-webserver/commits{/sha}",    "git_commits_url": "https://api.github.com/repos/jaberchez/demo-webserver/git/commits{/sha}",    "comments_url": "https://api.github.com/repos/jaberchez/demo-webserver/comments{/number}",    "issue_comment_url": "https://api.github.com/repos/jaberchez/demo-webserver/issues/comments{/number}",    "contents_url": "https://api.github.com/repos/jaberchez/demo-webserver/contents/{+path}",    "compare_url": "https://api.github.com/repos/jaberchez/demo-webserver/compare/{base}...{head}",    "merges_url": "https://api.github.com/repos/jaberchez/demo-webserver/merges",    "archive_url": "https://api.github.com/repos/jaberchez/demo-webserver/{archive_format}{/ref}",    "downloads_url": "https://api.github.com/repos/jaberchez/demo-webserver/downloads",    "issues_url": "https://api.github.com/repos/jaberchez/demo-webserver/issues{/number}",    "pulls_url": "https://api.github.com/repos/jaberchez/demo-webserver/pulls{/number}",    "milestones_url": "https://api.github.com/repos/jaberchez/demo-webserver/milestones{/number}",    "notifications_url": "https://api.github.com/repos/jaberchez/demo-webserver/notifications{?since,all,participating}",    "labels_url": "https://api.github.com/repos/jaberchez/demo-webserver/labels{/name}",    "releases_url": "https://api.github.com/repos/jaberchez/demo-webserver/releases{/id}",    "deployments_url": "https://api.github.com/repos/jaberchez/demo-webserver/deployments",    "created_at": 1612596575,    "updated_at": "2021-03-26T16:17:54Z",    "pushed_at": 1617282874,    "git_url": "git://github.com/jaberchez/demo-webserver.git",    "ssh_url": "git@github.com:jaberchez/demo-webserver.git",    "clone_url": "https://github.com/jaberchez/demo-webserver.git",    "svn_url": "https://github.com/jaberchez/demo-webserver",    "homepage": null,    "size": 3,    "stargazers_count": 0,    "watchers_count": 0,    "language": "Go",    "has_issues": true,    "has_projects": true,    "has_downloads": true,    "has_wiki": true,    "has_pages": false,    "forks_count": 0,    "mirror_url": null,    "archived": false,    "disabled": false,    "open_issues_count": 0,    "license": null,    "forks": 0,    "open_issues": 0,    "watchers": 0,    "default_branch": "master",    "stargazers": 0,    "master_branch": "master"  },  "pusher": {    "name": "jaberchez",    "email": "44943862+jaberchez@users.noreply.github.com"  },  "sender": {    "login": "jaberchez",    "id": 44943862,    "node_id": "MDQ6VXNlcjQ0OTQzODYy",    "avatar_url": "https://avatars.githubusercontent.com/u/44943862?v=4",    "gravatar_id": "",    "url": "https://api.github.com/users/jaberchez",    "html_url": "https://github.com/jaberchez",    "followers_url": "https://api.github.com/users/jaberchez/followers",    "following_url": "https://api.github.com/users/jaberchez/following{/other_user}",    "gists_url": "https://api.github.com/users/jaberchez/gists{/gist_id}",    "starred_url": "https://api.github.com/users/jaberchez/starred{/owner}{/repo}",    "subscriptions_url": "https://api.github.com/users/jaberchez/subscriptions",    "organizations_url": "https://api.github.com/users/jaberchez/orgs",    "repos_url": "https://api.github.com/users/jaberchez/repos",    "events_url": "https://api.github.com/users/jaberchez/events{/privacy}",    "received_events_url": "https://api.github.com/users/jaberchez/received_events",    "type": "User",    "site_admin": false  },  "created": false,  "deleted": false,  "forced": false,  "base_ref": null,  "compare": "https://github.com/jaberchez/demo-webserver/compare/49b50e0b72dc...018b8a6f978a",  "commits": [    {      "id": "018b8a6f978affda063b7ba857ea4d66cd34a20a",      "tree_id": "b2ee6574535b87d1771b3120347ffa57b889813a",      "distinct": true,      "message": "Testing",      "timestamp": "2021-04-01T15:14:34+02:00",      "url": "https://github.com/jaberchez/demo-webserver/commit/018b8a6f978affda063b7ba857ea4d66cd34a20a",      "author": {        "name": "jaberchez",        "email": "44943862+jaberchez@users.noreply.github.com",        "username": "jaberchez"      },      "committer": {        "name": "GitHub",        "email": "noreply@github.com",        "username": "web-flow"      },      "added": [      ],      "removed": [      ],      "modified": [        "README.md"      ]    }  ],  "head_commit": {    "id": "018b8a6f978affda063b7ba857ea4d66cd34a20a",    "tree_id": "b2ee6574535b87d1771b3120347ffa57b889813a",    "distinct": true,    "message": "Testing",    "timestamp": "2021-04-01T15:14:34+02:00",    "url": "https://github.com/jaberchez/demo-webserver/commit/018b8a6f978affda063b7ba857ea4d66cd34a20a",    "author": {      "name": "jaberchez",      "email": "44943862+jaberchez@users.noreply.github.com",      "username": "jaberchez"    },    "committer": {      "name": "GitHub",      "email": "noreply@github.com",      "username": "web-flow"    },    "added": [    ],    "removed": [    ],    "modified": [      "README.md"    ]  }}
'''

token = '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'
#token        = os.environ.get('GITHUB_TOKEN')
headers      = {"Authorization": "token {}".format(token)}
file_payload = "/tmp/payload.conf"
#payload_str  = "{}".format('$(params.gitHubPayload)')
payload      = {}
hook         = ""
params       = []
#github_request_url = 'https://el-github-event-listener-tekton.apps.cluster01.sandbox1789.opentlc.com:'
github_request_url = 'https://el-github-event-listener-tekton.apps.cluster01.sandbox1789.opentlc.com'
x_forwarded_host   = 'el-github-event-listener-test-tekton.apps.cluster01.sandbox1789.opentlc.com'

# Data from webhook request url
custom_data  = {}

#if re.match(r':$', github_request_url):
#m = re.match(r':$', github_request_url)
#if re.match(r':$', github_request_url) != None:
#if re.match(r':$', github_request_url):
#   github_request_url = re.sub(r':$', "", github_request_url)
github_request_url = re.sub(r':$', "", github_request_url)

if token == None:
   print("[ERROR] Unable to find GitHub token")
   sys.exit(1)

if len(payload_str) == 0:
  print("[ERROR]: GitHub payload empty")
  sys.exit(1)

payload = json.loads(payload_str)

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
         hook_tmp = h['config']['url']
         hook_tmp = re.sub(r'^https?://', "", hook_tmp)

         if hook_tmp.startswith(x_forwarded_host):
            hook = "{}".format(h['config']['url'])
            break
except Exception as e:
   print("[ERROR] {}".format(e))
   sys.exit(1)

if len(hook) == 0:
   print("[ERROR] WebHook not found")
   sys.exit(1)

# Extract params from webhook
parsed = urlparse.urlparse(hook)
p      = parsed.query.split('&')

for i in p:
   i = i.replace(" ", "")
   d = i.split("=")

   key = "{}".format(d[0])
   val = "{}".format(d[1])

   if len(key) == 0:
     print("[ERROR] Unable to find a key in webhook URL parameters")
     sys.exit(1)
   elif len(val) == 0:
     print("[ERROR] Unable to find a value in key \"{}\" in webhook URL parameters".format(key))
     sys.exit(1)

   key = key.upper()
   val = val.lower()

   custom_data[key] = val

if len(custom_data) == 0:
   print("[ERROR] Unable to find data in webhook URL parameters")
   sys.exit(1)

# Check if "TYPE" key exists
# Note: TYPE is the key to know the pipeline to run
if not 'TYPE' in custom_data:
  print("[ERROR] Unable to find key 'TYPE' in Webhook URL")
  sys.exit(1)

# Add custom_data to payload
payload['custom_data'] = custom_data

# Add github_event_got key with the github event we got
payload['github_event_got'] = "{}".format('$(params.gitHubEvent)')

# Create the file with the new payload
try:
   f = open(file_payload,"w")
   f.write(json.dumps(payload))
   f.close()
except Exception as e:
   print("[ERROR] {}".format(e))
   sys.exit(1)

sys.exit(0)

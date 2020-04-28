#!/usr/bin/python3
import requests

iq_session = requests.Session()
iq_session.auth = requests.auth.HTTPBasicAuth("admin", "admin123")
iq_url = "http://localhost:8070"
orgs = {}

url = f'{iq_url}/api/v2/organizations'
organizations = iq_session.get(url).json()["organizations"]
for org in organizations:
	orgs.update({
		org["id"]: {
			"name": org["name"], 
			"count": 0, 
			"apps": []
		} 
	})


url = f'{iq_url}/api/v2/applications'
apps = iq_session.get(url).json()["applications"]

for app in apps:
	org_id = app["organizationId"]
	orgs[org_id]["apps"].append(app["publicId"])

for org in orgs.values():
	org["count"] = len( org["apps"] )

for org in orgs.values():
	print (f'{org["name"]} : {org["count"]}')

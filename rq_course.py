import requests
import json

sess = requests.session()
# response = sess.get('http://api.github.com/', auth=('robober', 'MySuperSecurePassword'))

# print(response.status_code)
# print(response.headers)

response = sess.get('http://api.github.com/user/repos', auth=('robober', 'MySuperSecurePassword'))

print("\nREPOSITORIES-------->\n")

for index, repo in enumerate(json.loads(response.text)):
	print(str(index) + " " + repo['full_name'])

print("\n<--------REPOSITORIES")
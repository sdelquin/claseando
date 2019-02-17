import sys
import re
import os

url = sys.argv[1]
r = re.search('github.com/([^\/]+)/', url)
username = r.groups()[0]
r = re.search('tree/([^\/]+)/', url)
commit = r.groups()[0]

repo_url = f'git@github.com:{username}/imw.git'
repo_path = 'imw'

os.system(f'git clone {repo_url} {repo_path}')
os.system(f'cd {repo_path} && git checkout {commit}')

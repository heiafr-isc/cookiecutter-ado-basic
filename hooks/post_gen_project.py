from subprocess import call
import sys

gitlab_url = "{{ cookiecutter.gitlab_url }}"

retcode = call("git init --initial-branch=main", shell=True)
if retcode != 0:
    print("Failed to initialize git")
    sys.exit(1)

if len(gitlab_url) == 0:
    print("No gitlab URL given, skipping adding remote")
    sys.exit(0)

retcode = call(f"git remote add origin {gitlab_url}", shell=True)
if retcode != 0:
    print("Failed to add remote")
    sys.exit(1)

from subprocess import call
import sys

retcode = call("git init --initial-branch=main", shell=True)
if retcode != 0:
    print("Failed to initialize git")
    sys.exit(1)

retcode = call("git remote add origin {{ cookiecutter.gitlab_url }}", shell=True)
if retcode != 0:
    print("Failed to add remote")
    sys.exit(1)

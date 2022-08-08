from cookiecutter.utils import simple_filter
import re

@simple_filter
def extractslug(gitlab_url):
    m = re.search(r"(\w+?)(-\w*)?\.git$", gitlab_url)
    if m:
        return m.group(1)
    else:
        return "tpxx"

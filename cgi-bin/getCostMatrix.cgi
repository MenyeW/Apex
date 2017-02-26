#!/Python27/python
import memcache
import json
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
value = mc.get("costMatrix")
json = json.JSONEncoder().encode(value)
print json

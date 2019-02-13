import sys
import json

data = json.loads(sys.argv[1])

# print(str(data))
print(data.name)
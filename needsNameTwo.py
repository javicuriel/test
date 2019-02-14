import sys
import json
data = json.loads(sys.argv[1])
print("The name is: "+str(data['name']))

import json
import random

nbs = [2,3,5,7,11,13]

fn = "nb.json"
with open(fn,'w') as f :
    json.dump(nbs,f)

nfn = 'nb.json'
with open(nfn) as a :
    nnbs =json.load(a)

print(nnbs)
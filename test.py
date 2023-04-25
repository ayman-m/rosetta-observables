import json

# Load the JSON file
with open('nvdcve.json', 'r') as f:
    data = json.load(f)['CVE_Items']
for data in data[:1000]:
    print (data['cve']['CVE_data_meta']['ID'])


# Use the data as a Python object

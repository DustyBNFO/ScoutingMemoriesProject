
''' Generate Council Links from councils_us table data

    Format : https://dev.boyscoutimages.org/portal?portal=council_4thcongressionaldistrict_va&council-id=4thCongressionalDistrict-VA&council-name=4th%20Congressional%20District

'''

import re

council_portals = [] # takes in council short names (ID's) and replaces "-" with "_"
                     # then sets all chars to lowercase to match MySQL table names                  

council_ids = [] # takes in council short names (ID's) ex. "Robert-E-Lee-VA", "Riverside-NJ"

council_names = [] # all HTML special characters manually replaced in source file
                   # Ex. whitespace replaced with %20, etc. See HTML special chars
                   # Note : Be sure to do a quick visual check for character wierdness
                   # prior to reading in council names


# Format council_names.csv to replace special chars with HTML encoding (%20, %3A etc.)
html_encodings = {

    "!" : "%21",
    "*" : "%2A",
    "@" : "%40",
    '"' : "%22",
    "#" : "%23",
    "+" : "%2B",
    "[" : "%5B",
    "$" : "%24",
    "," : "%2C",
    "%" : "%25",
    "/" : "%2F",     
    "]" : "%5D",
    "&" : "%26",
    "'" : "%27",
    ":" : "%3A",
    "(" : "%28",
    ";" : "%3B",
    ")" : "%29",     
    "=" : "%3D",
    "?" : "%3F",
    " " : "%20"

}

# Replace special chars in Council names with html url encodings
with open('council_names.csv', 'r') as f:
    for council_name in f:
        for char, encoding in html_encodings.items():
            council_name = re.sub(re.escape(char), encoding, council_name)

        council_names.append(council_name.rstrip())


# Use Councils ID's to generate the portal/table names
with open('council_ids.csv', 'r') as f:
    for portal in f:
        council_portals.append(portal.replace("-", "_").lower().rstrip())


with open('council_ids.csv', 'r') as f:
    for council_id in f:
        council_ids.append(council_id.rstrip())


zipped_list = zip(council_portals, council_ids, council_names)


with open('council_links.csv', 'w') as f:
    for portal, id, name in zipped_list:
        f.write(f"https://dev.boyscoutimages.org/portal?portal=council_{portal}&council-id={id}&council-name={name}\n")
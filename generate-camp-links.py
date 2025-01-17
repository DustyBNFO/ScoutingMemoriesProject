
''' Generate Camp Links

    Format : https://dev.boyscoutimages.org/portal?portal=camps&camp-id=Shawondasee-VA&camp-name=Camp%20Shawondasee

'''

import re


camp_ids = [] # takes in council short names (ID's) ex. "Shawondasee-VA", etc.

camp_names = [] # all HTML special characters manually replaced in source file
                   # Ex. whitespace replaced with %20, etc. See HTML special chars
                   # Note : Be sure to do a quick visual check for character wierdness
                   # prior to reading in camp names


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
with open('camp_names.csv', 'r') as f:
    for camp_name in f:
        for char, encoding in html_encodings.items():
            camp_name = re.sub(re.escape(char), encoding, camp_name)

        camp_names.append(camp_name.rstrip())


with open('camp_ids.csv', 'r') as f:
    for camp_id in f:
        camp_ids.append(camp_id.rstrip())


zipped_list = zip(camp_ids, camp_names)


with open('camp_links.csv', 'w') as f:
    for id, name in zipped_list:
        f.write(f"https://dev.boyscoutimages.org/portal?portal=camps&camp-id={id}&camp-name={name}\n")
import json

with open('sessionstore.js', encoding='utf-8') as f:
    content = json.load(f)

# The loaded content is a dictionary. List the keys first (console).
for k in content:
    print(k)

# Now list the content bound to the keys. As the console may not be capable
# to display all characters, write it to the file.
with open('out.txt', 'w', encoding='utf-8') as f:

    # Write the overview of the content.
    for k, v in content.items():
        # Write the key and the type of the value.
        f.write('\n\n{}:  {}\n'.format(k, type(v)))

        # The value could be of a list type, or just one item.
        if isinstance(v, list):
            for e in v:
                f.write('\t{}\n'.format(e))
        else:
            f.write('\t{}\n'.format(v))

    # Write the content of the tabs in each windows.
    f.write('\n\n=======================================================\n\n')
    windows = content['windows']
    for n, w in enumerate(windows, 1):  # the enumerate is used just for numbering the windows
        f.write('\n\tWindow {}:\n'.format(n))
        tabs = w['tabs']
        for tab in tabs:
            # The tab is a dictionary. Display only 'title' and 'url' from
            # 'entries' subdictionary.
            e = tab['entries'][0]
            f.write('\t\t{}\n\t\t{}\n\n'.format(e['url'], e['title']))

import pyperclip

content = pyperclip.paste()

lines = content.split('\n')

# tab size of the source code you are copying from
tabSize = 4
tabIdentifier = tabSize * ' '

snippetLines = []
for line in lines:
	snippetLines.append('"' + line.replace(tabIdentifier, '\\t') + '"')

separator = ',\n\t\t\t'

body = separator.join(snippetLines)

template = '''"KEY": {
		"prefix": "",
		"body": [
			#TOKEN#
		],
		"description": ""
	},'''

snippet = template.replace('#TOKEN#', body)

pyperclip.copy(snippet)
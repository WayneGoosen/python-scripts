import pyperclip

content = pyperclip.paste()

lines = content.split('\n')

snippetLines = []
for line in lines:
    snippetLines.append('"' + line + '"')

separator = ',\n'

body = separator.join(snippetLines)

template = '''"": {
	 	"prefix": "",
	 	"body": [
	 		#TOKEN#
	 	],
	 	"description": ""
	 },'''

snippet = template.replace('#TOKEN#', body)

pyperclip.copy(snippet)



import pyperclip

content = pyperclip.paste()

cr = '\r'
lf = '\n'
crlf = cr + lf

endOfLineSequence = crlf

lines = content.split(endOfLineSequence)

escapeDoubleQuotes = '\\"'

# tab size of the source code you are copying from
tabSize = 4
tabIdentifier = tabSize * ' '

snippetLines = []
for line in lines:
	line = line.replace('"', escapeDoubleQuotes)
	snippetLines.append('"' + line.replace(tabIdentifier, '\\t') + '"')

bodyLineseparator = ',\n\t\t\t'

body = bodyLineseparator.join(snippetLines)

template = '''"KEY": {
		"prefix": "",
		"description": "",
		"body": [
			#TOKEN#
		]
	},'''

snippet = template.replace('#TOKEN#', body)

pyperclip.copy(snippet)
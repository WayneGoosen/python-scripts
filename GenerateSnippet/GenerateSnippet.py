import pyperclip
import unittest

def SplitContentIntoLines(content, endOfLineSequence):
	endOfLineSequences = {"cr" : "\r", "lf": "\n", "crlf" : "\r\n"}
	endOfLineChar = endOfLineSequences[endOfLineSequence]
	return content.split(endOfLineChar)

def EscapeDoubleQuotes(content):
	escapeStr = '\\"'
	return content.replace('"', escapeStr)

def ReplaceSpacesWithTabDelimiter(content, tabSize):
	tabIdentifier = tabSize * ' '
	tabDelimiter = '\\t'
	return content.replace(tabIdentifier, tabDelimiter)

def AddDoubleQuotes(content):
	return '"' + str(content) + '"'

def GenerateSnippetLines(lines, tabSize):
	snippetLines = []
	for line in lines:
		line = ReplaceSpacesWithTabDelimiter(line, tabSize)
		line = EscapeDoubleQuotes(line)
		line = AddDoubleQuotes(line)
		snippetLines.append(line)
	return snippetLines

def BuildSnippetBody(snippetLines):
	bodyLineseparator = ',\n\t\t\t'
	return bodyLineseparator.join(snippetLines)

def GenerateSnippetJson(snippetBody):
	template = '''"KEY": {
	"prefix": "",
	"description": "",
	"body": [
		#TOKEN#
	]
},'''
	return template.replace('#TOKEN#', snippetBody)

def GetClipBoardContent():
	return pyperclip.paste()

def PasteContentOntoClipBoard(content):
	pyperclip.copy(content)

def GenerateSnippetAndPasteOntoClipBoard(endOfLineSequence, tabSize):
	content = GetClipBoardContent()

	lines = SplitContentIntoLines(content, endOfLineSequence)

	snippetLines = GenerateSnippetLines(lines, tabSize)

	body = BuildSnippetBody(snippetLines)

	snippetJson = GenerateSnippetJson(body)

	PasteContentOntoClipBoard(snippetJson)



GenerateSnippetAndPasteOntoClipBoard("cr", 4)
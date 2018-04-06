from GenerateSnippet import SplitContentIntoLines,EscapeDoubleQuotes,ReplaceSpacesWithTabDelimiter,AddDoubleQuotes,GenerateSnippetLines
import unittest

class TestLineSplit(unittest.TestCase):
	def setUp(self):
		self.endOfLineSequences = {"cr" : "\r", "lf": "\n", "crlf" : "\r\n"}	

	def coreTest(self, endOfLineSequence):
		endOfLineChar = self.endOfLineSequences[endOfLineSequence]
		content = "firstline" + str(endOfLineChar) + "secondline"
		lines = SplitContentIntoLines(content, endOfLineSequence)
		self.assertEquals(len(lines),2)
		self.assertEquals("firstline",lines[0])
		self.assertEquals("secondline",lines[1])

	def test_SplitContentIntoLines_cr(self):
		self.coreTest("cr")
	
	def test_SplitContentIntoLines_lf(self):
		self.coreTest("lf")
	
	def test_SplitContentIntoLines_crlf(self):
		self.coreTest("crlf")

class TestEscapeQuotes(unittest.TestCase):
	def test_EscapeDoubleQuotes_single(self):
		quotes = '"'
		self.assertEqual(EscapeDoubleQuotes(quotes),'\\"')
	
	def test_EscapeDoubleQuotes_double(self):
		quotes = '""'
		self.assertEqual(EscapeDoubleQuotes(quotes),'\\"\\"')

class TestReplaceSpacesWithTabDelimiter(unittest.TestCase):
	def test_ReplaceSpacesWithTabDelimiter_two(self):
		content = '  '
		self.assertEqual(ReplaceSpacesWithTabDelimiter(content, 2),'\\t')

	def test_ReplaceSpacesWithTabDelimiter_four(self):
		content = '    '
		self.assertEqual(ReplaceSpacesWithTabDelimiter(content, 4),'\\t')

class TestAddDoubleQuotes(unittest.TestCase):
	def test_AddDoubleQuotes(self):
		content = 'hello'
		self.assertEqual(AddDoubleQuotes(content),'"hello"')

class TestGenerateSnippetLines(unittest.TestCase):
    	def test_GenerateSnippetLines_singleCodeLine(self):
		content = 'public class Hello {'
		lines = SplitContentIntoLines(content, "cr")
		snippetLines = GenerateSnippetLines(lines, 2)
		self.assertEqual(len(snippetLines), 1)
		self.assertEqual(snippetLines[0],'"public class Hello {"')


if __name__ == '__main__':
	unittest.main()
		

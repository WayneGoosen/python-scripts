''' Used to generate a SQL in statement from line separated values on clipboard & pastes completed in statement onto clipboard '''
import pyperclip

clipBoardContent = pyperclip.paste()

endOfLineSequences = {"cr" : "\r", "lf": "\n", "crlf" : "\r\n"}

values = clipBoardContent.split(endOfLineSequences["crlf"])

separator = ","
inStatement = "in (" + separator.join(values) + ")"

pyperclip.copy(inStatement)
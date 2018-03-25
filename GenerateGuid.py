import pyperclip, uuid

# Create a new Guid
newGuid = str(uuid.uuid4())

# Copy the new Guid to the clip board
pyperclip.copy(newGuid)

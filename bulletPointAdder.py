import pyperclip

# Get text from the clipboard
text = pyperclip.paste()

# Split text into separate lines
lines = text.split('\n')

# Add a bullet point to each line
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join the lines back together
text = '\n'.join(lines)

# Copy the new text back to the clipboard
pyperclip.copy(text)

print("Bullet points added! Paste your text anywhere.")
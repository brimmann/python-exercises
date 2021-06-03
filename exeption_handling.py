result = "Not found"
text = "Helllo Rashid I don't know!"
i = text.find("<")
if i > -1:
	j = text.find(">")
	if j > -1:
		result = text[i:j+1]
print(result)

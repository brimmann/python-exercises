text = "<Hello my bro!>"
result = ""
i = text.find("<")
if i > -1:
    j = text.find(">", i+1)
    if j > -1:
        result = text[i:j + 1]
print(result)

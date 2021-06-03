text = "He<ll>o Bro"
try:
    i = text.index("<")
    j = text.index(">", i+1)
    result = text[i:j + 1]
except ValueError:
    result = ""
print(result)

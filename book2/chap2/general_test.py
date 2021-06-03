def simplify(text, space = "\t\r\n\f", delete = ""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in space:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        reslut.append(word)
        return " ".join(result)

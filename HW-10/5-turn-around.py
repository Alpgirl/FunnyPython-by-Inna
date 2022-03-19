text = input("Введите текст, в котором буква 'h' встречается минимум 2 раза: ")

indices = [key for key, value in enumerate(text) if value == "h"]
text = text[:min(indices)] + text[max(indices):min(indices):-1] + text[max(indices):]
print("Результат разворота:", text)

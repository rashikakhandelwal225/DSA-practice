def defangIPaddr(address):
    new_char = "[.]"
    resultant_string = address.replace(".", new_char)
    return resultant_string

address = "1.1.1.1"
print(defangIPaddr(address))
address = "255.100.50.0"
print(defangIPaddr(address))
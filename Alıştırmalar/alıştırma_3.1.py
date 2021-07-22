text = "X-DSPAM-Confidence:    0.8475"
num_index = text.find(".")
new_num = float(text[num_index-1:])
print(type(new_num))
print(new_num)
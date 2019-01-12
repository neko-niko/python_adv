import array

test = bytes('◐test', encoding='utf-8')
test_arr = bytearray(test)
print(test_arr[:1])
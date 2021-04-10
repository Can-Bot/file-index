binF = open("duck.bin", "wb")

test = "this is a test"

testBytes = bytearray(test.encode('utf-8'))

binF.write(testBytes)
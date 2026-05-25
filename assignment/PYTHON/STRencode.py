print("STRING\t\"ENCODING\"")
#Encoding means converting human-readable text (string) into machine-readable bytes.
#Computers store data in binary form (0s and 1s).
TXT="PYTHON"
a="VAIShu"
print(TXT.encode("utf-8"))
result=a.encode()
print(result)
print(a.encode("utf-8"))
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print("Type of encode")
print(type(a.encode("utf-8")))

#👉 Special characters are converted into byte format.
#b inculdes byte code.
#✅ UTF-8 is the most commonly used encoding.
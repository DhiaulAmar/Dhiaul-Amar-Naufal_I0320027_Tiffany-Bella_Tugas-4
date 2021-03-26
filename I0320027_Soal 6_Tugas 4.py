a = 4
b = 11
print("Nilai a =", a, ", dalam biner :", format(a, "08b"))
print("Nilai b =", b, ", dalam biner :", format(b, "08b"))

c = a | b;
print("Nilai a | b = ", c, ", dalam biner :" ,format(c, "08b"))

c = a >> b;
print("Nilai a >> b = ", c, ", dalam biner :" ,format(c, "08b"))

c = a ^ b
print("Nilai a ^ b = ", c, ", dalam biner :" ,format(c, "08b"))

c = ~a;
print("Nilai ~a= ", c, ", dalam biner :" ,format(c, "08b"))

c = b & a
print("Nilai b & a = ", c, ", dalam biner :" ,format(c, "08b"))
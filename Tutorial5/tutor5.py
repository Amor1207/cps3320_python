import re
string1 = "Aabb29ABCLK%1CnerDBCabbbb"
#we should use {4} to limit the number of occurrences of b
m = re.search(r"ab{4}",string1)
print(m)
#"[A-Z][a-z]+" means that the first matched string of one uppercase letter + multiple lowercase letters
n = re.search("[A-Z][a-z]+",string1)
print(n)
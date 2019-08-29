import re

print(re.sub("a","*","abc adc afg"))
print(re.sub("[ab]","*","abc adc afg b"))
print(re.sub("abc","*","abc adc afg"))
print(re.sub('A.B',"*","A2B, AxB, AxxB,ABx"))
print(re.sub('A..B',"*","A2B, AxxB,ABx"))
print(re.sub('AB+',"*","ABC ABBBBBBBC ab cd"))


#search : used to find pattern anywhere
# str = "The rain in Spain"
# print(re.search("rain",str))

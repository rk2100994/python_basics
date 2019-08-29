list_authors = ["Coremn","KL Kapoor","RK Sharma"]
enu = enumerate(list_authors)

enu_list = list(enu)
for i in enu_list:
	print(i)

for k in enumerate(list_authors):
	print(k)
	print(k[0])
	print(k[1])
	print(type(k))
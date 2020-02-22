import re
Message="ffm/8"
VersionNumber=[]
x=re.split("/",Message)
vn=x[::-1]
smi=re.findall("[a-z0-9A-z]+", Message)
smi.remove(vn[0])
print(smi,"- Standard Message Identifier")
print(vn[0],"- Version-Number")
if re.findall("/",Message):
	print("/ - Slant")




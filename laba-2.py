import re
file = open ("nums.txt" , 'r')
text = file.read()
re_text = re.sub(r'[^\w\s]','', text)
num = len(re_text.split())
print (re_text )
print (num)

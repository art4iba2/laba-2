import re
file = open ("nums.txt" , 'r')
text = file.read()
re_text = re.sub(r'[^\w\s]','', text)
num = len(re_text.split())
print ("последовательность чисел : " , re_text )
print ("количество чисел в последовательности :" , num)

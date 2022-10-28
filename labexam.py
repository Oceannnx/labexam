# namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
# namelengthlist = (list((i,int(j)) for i in namelist for j in str(len(i))))

# Dr_set = {'Jeffy', 'David', 'Ted'} 
# namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
# # print(list("Dr. " + i if i in Dr_set else i for i in namelist))
# titlednamelist = list("Dr. " + i if i in Dr_set else i for i in namelist)

# student_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# scores = [9, 22, 60, 58, 70, 12, 33, 99, 57, 82]
# print(list((i,j) for i,j in zip(student_names,scores) if j >= 80))


ddict = {'Amanda': 'Doctor', 
        'knew': 'now', 
        'how': 'in', 
        'joyous': 'great', 
        'could': 'threatening', 
        'be': 'danger,',
        'until': 'please', 
        'saw': 'need', 
        'face': 'help', 
        'leaps': 'beats', 
        'hummingbird': 'machine ', 
        'in': 'very', 
        'flight': 'alarmingly', 
        'time': 'hour,', 
        'see': 'need', 
        'you': 'the drug', 
        'inspires': 'causes', 
        "haven't": 'am'}

letter="Dear Amanda I haven't knew how joyous life could be until I saw your face My heart leaps like a hummingbird in flight every time I see your face This is something I have never felt before and it is you that inspires it"
list_letter = letter.split()
decoded_list =  list(ddict.get(i) if i in ddict.keys() else i for i in list_letter)
decoded_letter = ' '.join(decoded_list)
print(decoded_letter)
# Expected ans-> decoded_letter = 'Dear Doctor I am now in great life threatening danger, please I need your help My heart beats like a machine  very alarmingly every hour, I need your help This is something I have never felt before and it is the drug that causes it'

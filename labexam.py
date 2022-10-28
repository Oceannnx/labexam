namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
namelengthlist = (list((i,int(j)) for i in namelist for j in str(len(i))))


Dr_set = {'Jeffy', 'David', 'Ted'} 
namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
# print(list("Dr. " + i if i in Dr_set else i for i in namelist))
titlednamelist = list("Dr. " + i if i in Dr_set else i for i in namelist)

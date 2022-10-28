def p11():
    namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
    # Expeced Ans -> namelengthlist = [('kitty', 5), ('Hinton', 6), ('Jack', 4), ('Ted', 3), ('Bahab', 5), ('Cebul', 5), ('David', 5), ('Koller', 6)]
    namelengthlist = (list((i,int(j)) for i in namelist for j in str(len(i))))
    return namelengthlist
    
def p12():
  Dr_set = {'Jeffy', 'David', 'Ted'} 
  namelist = ['kitty' , 'Hinton', 'Jack', 'Ted', 'Bahab', 'Cebul', 'David', 'Koller']
  titlednamelist = list("Dr. " + i if i in Dr_set else i for i in namelist)
  #Expected Ans -> titlednamelist = ['kitty', 'Hinton', 'Jack', 'Dr. Ted', 'Bahab', 'Cebul', 'Dr. David', 'Koller']
  return titlednamelist

def p13():
    student_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    scores = [9, 22, 60, 58, 70, 12, 33, 99, 57, 82]
    grade_a_student_with_score = (list((i,j) for i,j in zip(student_names,scores) if j >= 80))
    #Expected Ans -> grade_a_student_with_score = [('h', 99), ('j', 82)]
    return  grade_a_student_with_score

def p14():
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
    list_letter = letter.split(" ")
    decoded_list = list(ddict.get(i) if i in ddict.keys() else i for i in list_letter)
    decoded_letter = ' '.join(decoded_list)
    # Expected ans-> decoded_letter = 'Dear Doctor I am now in great life threatening danger, please I need your help My heart beats like a machine  very alarmingly every hour, I need your help This is something I have never felt before and it is the drug that causes it'
    return decoded_letter

def p2():
    icecream_msg = 'I like to buy ice cream: choco or may be cone otherwise sherbet'
    icecream_price = {'cone':'300', 'sherbet':'200', 'choco': '100'}
    #ExpectedAns = 'I like to buy ice cream: choco for 100 or may be cone for 300 otherwise sherbet for 200'
    decoded_icecream_list = (list(i +" "+ "for" + " " +icecream_price.get(i) if i in icecream_price else i for i in icecream_msg.split()))
    Ans = ' '.join(decoded_icecream_list)
    return Ans

def p3(x,y):
    gcd_1 = list(i for i in range(1,x+1) if x%i ==0)
    gcd_2 = list(i for i in range(1,y+1) if y%i ==0)
    gcd_all = max(list(i for i in gcd_1 if i in gcd_2))
    return gcd_all

from functools import reduce
def p4():
  list_x = [1.5,2,0.5,4,5]
  return (reduce(lambda x1, x2: (x2-x1)/(x2+x1), list_x))

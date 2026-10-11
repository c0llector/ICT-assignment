import random

Tandau = ['қайшы', 'құдық', 'қағаз']

oiynshy_utusy = 0
computer_utusy = 0
ten_zhagdai = 0

while True:
    oiynshy = input('Ойынды бастау үшін таңдаңыз: || Қағаз / Қайшы / Құдық || Аяқтау үшін: exit/quit ||\nСіздің таңдауыңыз: ')
    oiynshy = oiynshy.lower()
    
    if oiynshy == 'exit' or oiynshy == 'quit':
        print('                         Ойын Аяқталды!                         ')
        break
    
    #Ойыншы таңдауды дұрыс жазып тұрма соны тексеру ережесі:
    if oiynshy not in Tandau:
        print('Қате таңдау!')
        continue
    
    computer = random.choice(Tandau) #.choise() әдісі тізімнен кездейсоқ мәнді алады, біздің жағдайымызда бұл әдіс компьютердің таңдауы үшін қолданылды.
    
    print('Компьютердің таңдауы:', computer)
    
    if oiynshy == computer:
        ten_zhagdai += 1
        print('Тең!')
    
    #Ойыншы ұтатын барлық жағдай ережемен жазылып шықты, осылайша компьютерді келесіде ереже арқылы тексерудің қажеті жоқ, 
    #себебі ойыншы ұтылса, демек компьютер ұтады.
    elif (oiynshy == 'қағаз' and computer == 'құдық' or (oiynshy == 'құдық' and computer == 'қайшы') or (oiynshy == 'қайшы' and computer == 'қағаз')): 
        oiynshy_utusy += 1
        print('Сіз ұттыңыз!')
    
    else:
        computer_utusy += 1
        print('Ұтылдыңыз!')
        
print('                         | Қорытынды: |                    ')
print(f"| Сіз {oiynshy_utusy} рет ұттыңыз | Компьютердің {computer_utusy} рет ұтты | Тең жағдай: {ten_zhagdai} |")
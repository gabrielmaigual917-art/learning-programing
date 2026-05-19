import os 

client_ident = []
client_fullname = []
client_address = []
client_mobile = []
client_email = []
client_gender = []
client_age = []

product_code = []
product_name = []
product_quantity = []
product_unit_val = []

def mainmenu():
    os.system('clear')
    print(":::MARKET MAIN MENU:::")
    print(
        "[1]. Register client \n"\
        "[2]. Register product \n"\
        "[3]. list clients \n"\
        "[4]. list products \n"\
        "[5]. search client by ident \n"\
        "[6]. search product by code \n"\
        "[7]. update client \n"\
        "[8]. update product \n"\
        "[9]. delete client \n"\
        "[10]. delete productt \n"\
        "[11]. exit \n"\
        ".:: press any option: ")

#main
menu_status = True
while menu_status:
    mainmenu()
    opt = int(input ())
    
    if == 1:
        os.system('clear')
        print('...........................')
        print('........NEW CLIENTS........')
        print('...........................')
        
        ident = input('client identification:')
        client_ident.append(ident)
        fullname = input('client fullname: ')
        client_fullname. oppend(fullname)
        print('client has been registered successfully !!!')
        key = input(' press any option to back main menu')
    elif == 3:
        os.system('clear')
        print('...........................')
        print('........LIST CLIENTS........')
        print('...........................')

        i = 0
        while i < len(client_fullname):
            print('Identification      fullname')
            print(f'{client_ident[i]}')            {client_fullname[i]}   
            i+=1     
        
        key = input(' press any option to back main menu')
    
    if opt == '11':
        print(':::Bye Bye:::')
        break
    if opt < 1 or opt > 11:
        key = input(':: Ivalid option. Try again.\n' \
        'press any key to continue.')
        

num : int = int( input("> ") )

num_dictionary : dict = {
    1 : "один",
    2 : "два",
    3 : "три",
    4 : "четыре",
    5 : "пять",
    6 : "шесть",
    7 : "семь",
    8 : "восемь",
    9 : "девять"
    }

num10_dictionary : dict = {
    1 : "десять",
    2 : "двадцать",
    3 : "тридцать",
    4 : "сорок",
    5 : "пятьдесят",
    6 : "шестьдесят",
    7 : "семьдесят",
    8 : "восемьдесят",
    9 : "девяносто"
    }

num10_special : dict = {
    1 : "одиннадцать",
    2 : "двенадцать",
    3 : "тринадцать",
    4 : "четырнадцать",
    5 : "пятнадцать",
    6 : "шестьнадцать",
    7 : "семнадцать",
    8 : "восемнадцать",
    9 : "девятнадцать"
}

num100_dictionary : dict = {
    1 : "сто",
    2 : "двести",
    3 : "трсита",
    4 : "четыреста",
    5 : "пятьсот",
    6 : "шестьсот",
    7 : "семьсот",
    8 : "восемьсот",
    9 : "девятьсот"
    }

num1000_dictionary : dict = {
    0 : "тысяч",
    1 : "тысяча",
    2 : "тысячи",
    3 : "тысячи",
    4 : "тысячи",
    5 : "тысяч",
    6 : "тысяч",
    7 : "тысяч",
    8 : "тысяч",
    9 : "тысяч"
    }


ed : int = num % 10
ed_special : int = num % 100
dec : int = num % 100 // 10
hundred : int = num % 1000 // 100

thousands : int = num % 1000000 // 1000

ed_special_mapped = (ed_special - 20) + 10

if thousands != 0:
    first_digit : int = thousands % 10
    dec_t : int = thousands % 100 // 10

    t_special = thousands % 100
    t_special_mapped = (t_special - 20) + 10

    if t_special_mapped > 0 and t_special_mapped < 9:
       print( num10_special[t_special_mapped], end = " " )
        
    print( num1000_dictionary[thousand], end = "" )
    
if hundred != 0:
    print( num100_dictionary[hundred], end = " " )

if ed_special_mapped > 0 and ed_special_mapped < 9:
    print(num10_special[ed_special_mapped], end = " ")
else:
    if dec != 0:
        print( num10_dictionary[dec], end = " " )
    if ed != 0:
        print( num_dictionary[ed], end = " " )


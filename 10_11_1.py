num : int = int( input("> ") )

num_list : list[str] = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]

num10_list : list[str] = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят" , "восемьдесят", "девяносто"]

num1x_list : list[str] = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестьнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

num100_list : list[str]  = ["сто", "двести", "трсита", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

num1000_list : list[str] = [ "одна тысяча", "две тысячи", "три тысячи", "четыре тысяч", "пять тысяч", "шесть тысяч", "семь тысяч", "восемь тысяч", "девять тысяч" ]

digit = num % 10

digit_10 = num // 10 % 10
digit_1x = (num % 100) - 20 + 10

digit_100 = (num % 1000) // 100

digit_1000 = (num // 1000) % 1000


if digit_1000 != 0:
    
    th_digit = digit_1000 % 10
    
    th_digit_10 = digit_1000 // 10 % 10
    th_digit_1x = (digit_1000 % 100) - 20 + 10

    th_digit_100 = (digit_1000 % 1000) // 100

    if th_digit_100 != 0:
       print( num100_list[ th_digit_100 - 1], end = " " )

       if th_digit == 0 and th_digit == 0:
           print("тысяч", end = " ")

    if th_digit_1x > 0 and th_digit_1x < 10:
        print( num1x_list[ th_digit_1x - 1 ], end = " " )

        print("тысяч", end = " ")
    else:
        if th_digit_10 != 0:
            print( num10_list[ th_digit_10 - 1 ], end = " ")

            if th_digit == 0:
                print("тысяч", end = " ")
            
        if th_digit != 0:
            print( num1000_list[th_digit - 1], end = " " )
 
if digit_100 != 0:
    print( num100_list[ digit_100 - 1], end = " " ) 

if digit_1x > 0 and digit_1x < 10:

    print( num1x_list[ digit_1x - 1 ], end = " " )
else:
    if digit_10 != 0:
        print( num10_list[ digit_10 - 1 ], end = " " )
    if digit != 0:
        print( num_list[ digit - 1 ] )

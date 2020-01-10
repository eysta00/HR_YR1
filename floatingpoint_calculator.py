#Made by Ægir
""" This program lets you calculate/convert, single precision floating point binary numbers of imaginary sizes, to decimal or decimal fraction and the other way around"""

from fractions import Fraction

def getexponentsize():
    expo = input("Enter exponent size: ")
    while True:
        try:
            expo = int(expo)
            break
        except ValueError:
            print("Exponent size must be an integer")
            expo = getexponentsize()

    return expo

def getmantissasize():
    mantissa = input("Enter mantissa size: ")
    while True:
        try:
            mantissa = int(mantissa)
            break
        except ValueError:
            print("Mantissa size must be an integer")
            mantissa = input("Enter mantissa size: ")

    return mantissa

def getbinarynumber():
    binary_string = input("Enter binary number without a dot on fraction: ")
    while True:
        is_binary = True
        for i in range(len(binary_string)):
            if binary_string[i]!="0" or  binary_string[i]!="1":
                is_binary = False
        if is_binary:
            break
        else:
            print("Binary strings only contain 0 and 1")
            binary_string = input("Enter binary number without a dot on fraction: ")
    return binary_string

def getdecimalnumber():
    decimal_value = input("Enter decimal value with (f.ex 63.43 or -453): ")
    while True:
        if "." not in decimal_value and decimal_value[0]=="0":
            print("You are in (Decimal to float) conversion. Enter a decimal number or type (quit) to stop program")
            decimal_value = input("Enter decimal value with (f.ex 63.43 or -453): ")
            if decimal_value == "quit".lower():
                quit()
        else:
            break

    while True:
        try:
            test = float(decimal_value)
            break
        except ValueError:
            print("You entered an invalid float try again")
            decimal_value = input("Enter decimal value with (f.ex 63.43 or -453): ")

    return decimal_value

def binary_to_decimal_conversion(binary_string):
    len_string = len(binary_string)
    reverse_string = binary_string[::-1]
    decimal_value = 0
    for i in range(len_string):
        if reverse_string[i]=="1":
            decimal_value += 2**i

    return decimal_value

def getexponent_value(expo_size, binary_string): #e
    exponent = binary_string[1:expo_size+1]
    exponent_value = binary_to_decimal_conversion(exponent)
    return exponent_value

def getBias(expo_size): #bias
    bias = (2**(expo_size-1))-1
    return bias

def get_big_E(expo_size, binary_string): #E
    bias = getBias(expo_size)
    exponent_value = getexponent_value(expo_size, binary_string)
    if not exponent_all_zeros(expo_size, binary_string):
        big_E = exponent_value-bias
        return big_E
    else:
        big_E = 1 - bias
        return big_E

def max_exponent(expo_size):
    power = expo_size-1
    max_exponent = 0
    while power > 1:
        max_exponent +=2**power
        power -= 1
    return max_exponent

def exponent_all_ones(expo_size, binary_string):
    exponent_value = getexponent_value(expo_size, binary_string)
    max_expo = max_exponent(expo_size)

    if exponent_value > max_expo:
        return True #True if expo is all ones

def exponent_all_zeros(expo_size, binary_string):
    exponent = binary_string[1:expo_size+1:]
    initiate = "0"
    compare = initiate*expo_size
    if exponent == compare:
        return True #True if exponent is all zero

def mantissa_all_zeros(expo_size, mantissa_size, binary_string):
    mantissa = binary_string[expo_size+1:]
    initiate = "0"
    compare = initiate*(mantissa_size+1)
    if mantissa == compare:
        return True

def max_min_decimal(expo_size, mantissa_size, binary_string): #Get largest/smallest number possible with given float settings
    #largest fraction possible * 2^E
    big_E = 0
    expomax_string = "0"
    for i in range(expo_size):
        if i!=expo_size-1:
            expomax_string +="1"
        elif i==expo_size-1:
            expomax_string+="0"
    initiate = "0"
    add_temp = initiate*(mantissa_size+1)
    expomax_string +=add_temp

    big_E = get_big_E(expo_size, expomax_string)
    largest_fraction = 0
    power = 2
    for i in range(mantissa_size):
        largest_fraction += 2/(2**power)
        power+=1

    range_value = largest_fraction * (2**big_E)
    return range_value

def get_fraction(expo_size, mantissa_size, binary_string): #M
    mantissa = binary_string[expo_size+1:]

    """Decimal representation"""
    fraction = 0
    power = 2
    for i in range(mantissa_size):
        if(mantissa[i]=="1"):
            fraction += 2/(2**power)
        power+=1

    if not exponent_all_zeros(expo_size, binary_string):
        fraction += 1

    """Fraction representation"""
    fraction_repr = Fraction(fraction)

    return fraction, fraction_repr



def get_float_value(expo_size, mantissa_size, binary_string): #Decimal representation of binary float
    fraction, fraction_representation = get_fraction(expo_size, mantissa_size, binary_string)
    bigE = get_big_E(expo_size, binary_string)
    if binary_string[0] == "1":
        sign = -1
    else:
        sign = 1
    
    float_value = sign * fraction* (2**bigE)
    return float_value

    

def check_string_legality(expo_size, mantissa_size, binary_string):
    required_size = expo_size+mantissa_size+1
    actualy_size = len(binary_string)
    not_zero_one = False
    for i in range(len(binary_string)):
        if binary_string[i]!="0" or binary_string[i]!="1":
            not_zero_one==True

    while expo_size + mantissa_size+1 < len(binary_string) or expo_size + mantissa_size+1 > len(binary_string) or not_zero_one:
        was = ""
        if expo_size + mantissa_size+1 < len(binary_string):
            was = "larger"
        if expo_size + mantissa_size+1 > len(binary_string):
            was = "shorter"

        if expo_size + mantissa_size+1 < len(binary_string) or expo_size + mantissa_size+1 > len(binary_string):
            print("!!Binary string was %s than given size!!"%(was))
            print("Last input: %s"%(binary_string))
            print("Given exponent size: %d"%(expo_size))
            print("Given mantissa size: %d"%(mantissa_size))
            print("Exact size required accordin to given format: %d \nInput binary string size: %d"%(required_size, actualy_size ))
        if not_zero_one:
            print("Binary strings only contain the numbers 0 and 1")
            print("Your binary string input: %s"%(binary_string))
        to_do = input("Type (s) to enter a new binary string, (e) to change exponent value, (m) to change mantissa value. Type (q) to quit: ")
        if to_do == "s".lower():
            binary_string = getbinarynumber()
        if to_do == "e".lower():
            expo_size = getexponentsize()
        if to_do == "m".lower():
            mantissa_size = getmantissasize()
        if to_do == "q".lower():
            exit()

    return expo_size, mantissa_size, binary_string

def getfloat_output(expo_size, mantissa_size, binary_string):
    expo_size, mantissa_size, binary_string = check_string_legality(expo_size, mantissa_size, binary_string)
    if binary_string[0]=="1":
        sign = "-1"
    else:
        sign = "1"

    if exponent_all_ones(expo_size, binary_string) and mantissa_all_zeros(expo_size, mantissa_size, binary_string):
        print("you entered an Infinite number (Inf)")
    elif exponent_all_ones(expo_size, binary_string) and not mantissa_all_zeros(expo_size, mantissa_size, binary_string):
        print("the binary float number you entered does not exist (NaN)")
    else: 
        bias = getBias(expo_size)
        e = getexponent_value(expo_size, binary_string)
        big_E = get_big_E(expo_size, binary_string)
        max_nums = max_min_decimal(expo_size, mantissa_size, binary_string)
        big_M, big_M_Fractional = get_fraction(expo_size, mantissa_size, binary_string)
        float_value_decimal = get_float_value(expo_size, mantissa_size, binary_string)
        
        float_fraction = Fraction(float(sign))*Fraction(float(big_M))*Fraction(float(2**big_E))

        print("Binary float number in decimal: %s"%(float_value_decimal))
        print("Binary float number as decimal fraction: %s"%(float_fraction))
        print("Bias: %d"%(bias), end = " /// ")
        print("e: %d"%(e), end = " /// ")
        print("E: %d"%(big_E), end = " /// ")
        print("M as decimal: %s /// M as decimal fraction %s"%(big_M, big_M_Fractional))
        print("Highest/Lowest representable number with given float settins: (+/-)%s (%s)"%(max_nums, Fraction(float(max_nums))))

        print("Formula representation: %s * %s * 2^%d"%(sign, big_M_Fractional, big_E))


def create_decimal_binary(decimal_value):
    rev_decimal_string = ""
    if "." in decimal_value:
        dotindex = decimal_value.index(".")
        decimal = int(decimal_value[:dotindex])
    else:
        decimal = int(decimal_value)

    while decimal > 0:
        remainder = decimal%2
        if remainder == 1:
            rev_decimal_string+="1"
        elif remainder ==0:
            rev_decimal_string+="0"

        div2 = decimal//2
        decimal = div2
        
    decimal_string = rev_decimal_string[::-1]
    return decimal_string

def create_fraction_binary(mantissa_size, decimal_value, decimal_string):
    fraction_string = ""
    if "." in decimal_value:
        dot_index = decimal_value.index(".")
        temp_fraction = "0"+decimal_value[dot_index:]
        fraction = float(temp_fraction)

        while fraction > 0:
            fraction = fraction*2
            if fraction >=1:
                fraction_string+="1"
                fraction = fraction - 1
            else:
                fraction_string+="0"
            try:
                first_signed_bit = fraction_string.index("1")
            except:
                first_signed_bit = 0
            if (len(fraction_string)-(first_signed_bit+1))==(len(decimal_string)+mantissa_size):
                break
    return fraction_string


def create_normalized_float(expo_size, mantissa_size, decimal_value):
    decimal_string = create_decimal_binary(decimal_value)
    sign = "0"
    if "-" in decimal_value:
        sign = "1"
        decimal_value = decimal_value[1:]

    fraction_string = create_fraction_binary(mantissa_size, decimal_value, decimal_string)
    big_E = len(decimal_string)-1 #Færsla
    preset_mantissa = decimal_string[1:]

    if big_E<mantissa_size:
        fraction_string +="0"*(mantissa_size-(len(preset_mantissa)))
    
    preset_mantissa = preset_mantissa+fraction_string
    mantissa = preset_mantissa[:mantissa_size]

    bias = getBias(expo_size)
    decimal_small_e = bias+big_E 
    exponent = create_decimal_binary(str(decimal_small_e))

    binary_string = sign+exponent+mantissa
    
    return sign, exponent, mantissa, binary_string

def create_denormalized_float(expo_size, mantissa_size, decimal_value):
    sign = "0"
    if "-" in decimal_value:
        sign = "1"
        decimal_value = decimal_value[1:]

    fraction_string = create_fraction_binary(mantissa_size, decimal_value, "")

    if len(fraction_string)>mantissa_size:
        fraction_string +="0"*(mantissa_size-(len(fraction_string)))
    

    temp_mantissa = fraction_string
    add_mantissa = ""
    if len(temp_mantissa)<mantissa_size:
        add_mantissa = "0"*(mantissa_size-len(temp_mantissa))

    mantissa = temp_mantissa+add_mantissa
    exponent = expo_size*"0"
    binary_string = sign+exponent+mantissa

    return sign, exponent, mantissa, binary_string
        

def create_float_number(expo_size, mantissa_size, decimal_value):
    if "." in decimal_value:
        dot_index = decimal_value.index(".")
        dec = int(decimal_value[:dot_index])
        if dec > 1:
            sign, exponent, mantissa, binary_string = create_normalized_float(expo_size, mantissa_size, decimal_value)
        elif dec < 1:
            sign, exponent, mantissa, binary_string = create_denormalized_float(expo_size, mantissa_size, decimal_value)
    else:
        sign, exponent, mantissa, binary_string = create_normalized_float(expo_size, mantissa_size, decimal_value)

    return sign, exponent, mantissa, binary_string


def getdecimal_output(expo_size, mantissa_size, decimal_value):
    sign, exponent, mantissa, binary_string = create_float_number(expo_size, mantissa_size, decimal_value)
    print("Sign: %s"%(sign))
    print("Exponent: %s"%(exponent))
    print("Mantissa: %s"%(mantissa))
    print("Binary string with given settings: %s"%(binary_string))

            
def main():
    op_storage = ["getf", "getd", "quit"]
    operation = input("Type (getf), to convert decimal to float. Type (getd) to convert float to decimal: ")
    while operation.lower() not in op_storage:
        print("(%s) is not a valid operation, type (quit) to stop the program"%(operation.lower()))
        operation = input("Type (getf), to convert decimal to float. Type (getd) to convert float to decimal: ")
    
    expo_size = getexponentsize()
    mantissa_size = getmantissasize()

    if operation == "getd".lower():
        binary_string = getbinarynumber()
        getfloat_output(expo_size, mantissa_size, binary_string)

    elif operation == "getf".lower():
        repr_string = "0"*(expo_size+mantissa_size+1)
        largest_nums = max_min_decimal(expo_size, mantissa_size, repr_string)
        print("Highest/Lowest representable number with given float settins: (+/-)%s (%s)"%(largest_nums, Fraction(float(largest_nums))))

        decimal_value = getdecimalnumber()
        if float(decimal_value)>float(largest_nums) or float(decimal_value)<float(-largest_nums):
            print("The number you entered is either too large or too small for given float format")
            quit()
    
        binary_string = getdecimal_output(expo_size, mantissa_size, decimal_value)



        

    

main()


        


# Forrit tekur inntak sem eru rauntölur í einu inputi
# Forrit finnur út hvaða tvær rauntölur eru minnstar og fjarlægir þær
# Forritið skilar summu af rauntölunum sem verða eftir

def main ():
    user_input = input("Enter scores separated by space: ")
    score_float_list = []
    score_str_list = user_input.split(' ')

    for num in score_str_list:
        score_float_list.append(float(num))

    if len(score_float_list) < 2:
        print ("At least two scores needed!")
    else:
        score_float_list = sorted(score_float_list)
        adjusted_score_list = score_float_list[2:]
        print ("Sum of scores (two lowest removed):", sum(adjusted_score_list))

main()
from mymath import myArithmetic,myCalcArea,myStatistics
the_first_number=float(input("輸入第一個值:"))
the_second_number=float(input("輸入第二個值:"))
the_third_number=float(input("輸入第三個值:"))
the_fourth_number=float(input("輸入第四個值:"))
the_fifth_number=float(input("輸入第五個值:"))
list_of_number=[the_first_number,the_second_number,the_third_number,the_fourth_number,the_fifth_number]
print(myStatistics.myMean(list_of_number))

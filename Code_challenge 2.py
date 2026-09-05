#Peso Denominator
# Money = 4572
# 1000,500,200,100,50,20,10,5,1
#what operator/symbol did you we to solve ttgahe problem
# floor division, % mudulos
money = 4572
libo = money//1000  
libo_sukli = money % 1000  #572
# libo_sukli = money - (libo + 1000)

five_h = libo_sukli//500 # 5
five_sukli = libo_sukli % 500  #72 

two_h = five_sukli // 200
two_sukli = five_sukli % 200

one_h = two_sukli // 100
one_sukli = two_sukli %100


fifty = one_sukli // 50
fifty_sukli = one_sukli % 50

twenty = fifty_sukli // 20
twenty_sukli = fifty_sukli % 20

ten = twenty_sukli // 10
twenty_sukli = fifty_sukli % 20

ten = twenty_sukli // 10
ten_sukli = twenty_sukli % 10

five = ten_sukli // 5
five_sukli = ten_sukli % 5

one = five_sukli  // 1
one_sukli = five_sukli % 1
print("1000 -",libo)
print("500 -",five_h)
print("200 -",two_h) 
print("100 -", one_h)
print("50 -", fifty)
print("20 -", twenty)
print("10 -", ten)
print("5 -", five)
print("1 -",one)

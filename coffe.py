coffee=10

while True:
    money = int(input("돈을 넣으세요. : "))
        
    if money >= 300:
        print("커피를 줍니다.")
        coffee = coffee-1
        print(f"남은 커피의 양은 {coffee}개 입니다.")
            
    else:
        print("돈을 다시 돌려줍니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
            
    if coffee == 0 :
        print("커피가 다 떨어졌습니다.")
        break
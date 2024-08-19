#사용자로부터 숫자입력 받아서 구구단

gugu = int(input("구구구9999999999"))
for i in range(10):
    ans=gugu*i
    print(f"{gugu}*{i}={ans}")

for i in range(gugu+1):
    star = "*"
    print(star*i)
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
num = 0
result = 0
gugu = 3
dan = 6
data_list = list(range(1, gugu * dan + 1))

for i in data_list:
    if i % gugu == 0:
        num += 1
        result += i

print('주어진 리스트에서 ' + str(gugu) + '의 배수의 개수 => ' + str(num))
print('주어진 리스트에서 ' + str(gugu) + '의 배수의 합 => ' + str(result))


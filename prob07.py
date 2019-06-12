# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
import sys
repeat_num = 5
num_list = []
result = 0

for i in range(0, repeat_num):
    value = input('정수를 입력하세요 : ')
    if not value.isdigit():
        sys.exit(0)
    result += int(value)
    num_list.append(value)

result = result / repeat_num
print('평균' + str(result))


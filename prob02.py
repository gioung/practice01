# 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요
import sys
number = input('수를 입력하세요 : ')

if number.isdigit():
    number = int(number)
    if number <= 0:
        sys.exit(0)
    elif number % 2 == 0:
        print('짝수')
    else:
        print('홀수')



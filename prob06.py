# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.

import sys
money_unit_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

value = input('금액을 입력하세요 : ')

if not value.isdigit():
    sys.exit(0)

value = int(value)


def sep_money(money):
    for money_unit in money_unit_list:
        if money >= money_unit:
            quantity = money // money_unit
            print(str(money_unit)+'원 : ' + str(quantity) + '개')
            money -= money_unit * quantity


sep_money(value)




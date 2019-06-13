# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

# while True:
#     num = input('숫자를 입력하세요 : ')
#     if not num.isdigit():
#         break
#     num = int(num)
#     if num <= 0:
#         break
#
#     total = 0
#
#     for i in range(num % 2, num + 1, 2):
#         total += i
#
#     print('결과 값: {}'.format(total))

while True:
    number = input('숫자를 입력하세요:')
    if number.isdigit() is False:
        break

    number = int(number)

    s = 0
    for n in range(number+1):
        if number & 0x0001 ^ n & 0x0001 == 0:
            s += n

    print('결과 값: {0}'.format(s))

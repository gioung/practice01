# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요

string = input('입력> ')


def reverses(string):
    size = len(string)
    for i in range(size, 0, -1):
        print(string[i-1], end='')


len(string) != 0 and reverses(string)

# 주어진 if 문을 dict를 사용해서 수정하세요.
menus = {'오뎅': 300, '순대': 400, '만두': 500}
menu = input('메뉴 : ')

if menus.get(menu) is not None:
        print('가격: {}'.format(menus.get(menu)))






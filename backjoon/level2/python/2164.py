from collections import deque

card_num = int(input())
card_list = deque([card for card in range(1, card_num + 1)])

while len(card_list) > 1:
    card_list.popleft()
    card_list.append(card_list.popleft())

print(card_list.pop())









#
#
# card_list = [card for card in range(1, card_num + 1)]
# while (card_len := len(card_list)) > 1:
#     if card_len % 2 == 0:
#         card_list = card_list[1::2]
#     else:
#         new_list = [card_list[-1]]
#         card_list = card_list[1::2]
#         new_list.extend(card_list)
#         card_list = new_list
#
# print(card_list[0])




# 1 2 3 4 5 6 7 8 9 10
# 3 4 5 6 7 8 9 10 2
# 5 6 7 8 9 10 2 4
# 7 8 9 10 2 4 6
# 9 10 2 4 6 8
# 2 4 6 8 10
# 6 8 10 4
# 10 4 8
# 8 4
# 4


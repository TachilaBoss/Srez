# 1) Фильтр
# def de_none(lst):
#     return [x for x in lst if x is not None]
#
# my_list = [1, None, 2, None, 3, 4, None]
# result = de_none(my_list)
# print(result)

# 2) Добавление
# def list_insert(ref_list, start, num, rep):
#      return ref_list[:start] + [num] * rep + ref_list[start:] if len(ref_list) >= start else -1
#
# my_list = [1, 2, 3, 4, 5]
# result = list_insert(my_list, 2, 9, 2)
# print(result)

# 3)
# def get_elem(d, k):
#     if k in d:
#         return d[k]
#     else:
#         return None
#
#
# my_dict = {"apple": 5, "banana": 3, "cherry": 8}
# result1 = get_elem(my_dict, "banana")
# print(result1)
# result2 = get_elem(my_dict, "grape")
# print(result2)
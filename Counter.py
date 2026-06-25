from collections import Counter
_dict0={"a":10,"b":4,"c":12}
_dict1={"a":3,"c":1}

_dict2=Counter(_dict0)
_dict3=Counter(_dict1)
_dict4=dict(_dict2 + _dict3)
print(_dict4)
# print(_dict2)
# print(_dict3)

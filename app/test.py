s = {1: 2}
for key, value in s.items():
    print(key, value)

def compress_sequence(s):
    c = 0
    x = 0
    dic = {}
    new_list = []
    for i in s:
        if i not in dic:
            dic = {}
            new_list.append((tuple(s.items())[0]))
        else:
            dic[i] = x + 1
        new_list.append(())
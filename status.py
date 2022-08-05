

with open("/Users/mattsunkun/experiment/python/twitter/nigiri_status.txt", "r") as fp:
    level = fp.readline().strip()
    item = fp.readline().strip().rstrip(',')
    name = fp.readline().strip().rstrip(',')
    
# level
level = int(level)
# item
target_item = item.split(',')
target_item.append("壺")
# name
target_name = name.split(',')
target_name.append("@mattsunkun1221")

with open("/Users/mattsunkun/experiment/python/twitter/nigiri_status.txt", "w") as fp:
    # level
    print(f"{level}", file=fp)
    # item
    for item in target_item:
        print(f"{item}", end=",", file=fp)
    
    print("", file=fp)
    
    # name
    for name in target_name:
        print(f"{name}", end=",", file=fp)



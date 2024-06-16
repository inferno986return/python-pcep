train_speed = {"FlyingScotsman":201, "TGV":320, "Shinkansen":320}

for train in train_speed:
    print(train[0], end="")

print()

for train in train_speed.values():
    print(str(train)[0], end="") # 233

print()

for train in train_speed.items():
    print(train[0], end="") # 233
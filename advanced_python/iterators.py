days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
hari = ["isnin", "selasa", "rabu", "khamis", "jumaat", "sabtu", "ahad"]

i = iter(days)
print(next(i))
next(i)
print(next(i))
print(next(i))

for i,m in enumerate(days, start = 1):
    print(i, m)

for i,m in enumerate(hari, start = 1):
    print(i, m)

for i,m in enumerate(zip(days, hari), start = 1):
    print(i, m[0], "in malay = ", m[1])
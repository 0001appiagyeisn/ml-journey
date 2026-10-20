#Ask for number of seconds
tseconds = int(input("Enter number of seconds: "))

hours = tseconds // 3600

remain_seconds = tseconds % 3600

minutes = remain_seconds // 60

seconds = remain_seconds % 60

print(f"{tseconds}s = {hours}h,{minutes}m,{seconds}s")
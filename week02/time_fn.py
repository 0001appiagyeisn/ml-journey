def main():
    total_seconds = int(input("Enter total seconds: "))
    hours = get_hours(total_seconds)
    minutes = get_minutes(total_seconds)
    seconds = get_seconds(total_seconds)
    print(f"{hours} h {minutes} min {seconds} s")

def get_hours(seconds):
    return seconds // 3600

def get_minutes(seconds):
    return (seconds % 3600)// 60

def get_seconds(seconds):
    return seconds % 60

main()
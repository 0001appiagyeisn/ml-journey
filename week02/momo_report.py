from stats import mean, median, data_range, mode, variance, std_dev

momo = [23, 31, 27, 45, 29, 33, 26, 30, 28, 35, 31, 27, 32]

print(f"Days: {len(momo)}")
print(f"Mean: {mean(momo):.2f}")
print(f"Median: {median(momo):.2f}")
print(f"Mode: {mode(momo)}")
print(f"Range: {data_range(momo)}")
print(f"SD: {std_dev(momo):.2f}")

from stats import mean, median, data_range, mode, variance, std_dev

momo = [23, 31, 27, 45, 29, 33, 26, 120, 30, 28, 35, 31, 27, 32]

print(f"Days: {len(momo)}")
print(f"Mean: {mean(momo):.2f}")
print(f"Median: {median(momo):.2f}")
print(f"Mode: {mode(momo)}")
print(f"Range: {data_range(momo)}")
print(f"SD: {std_dev(momo):.2f}")

m = mean(momo)
sd = std_dev(momo)
print("Mean:", round(m, 2))
print("z of 120:", round((120 - m) / sd, 2))
print("z of 45:", round((45 - m) / sd, 2))
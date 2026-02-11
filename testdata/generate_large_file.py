with open("testdata/large_file.txt", "w") as f:
    for _ in range(100):
        f.write("Hello\n")

print("Large file generated successfully!")

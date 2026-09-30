with open("access.log", "r") as f:
    counts = {}
    for line in f:

        parts = line.split()
        if len(parts) >= 8 and parts[7].isdigit():
            code = parts[7]

            if code in counts:
                counts[code] += 1;
            else:
                counts[code] = 1
       
    for code, count in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
        print(code, count)
        
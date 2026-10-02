with open("auth.log", "r") as f:
    attempts = {}

    for line in f:

        if "Failed password" in line:
            log_list = line.split()
            ip = log_list[log_list.index("from") + 1]

            if ip in attempts:
                attempts[ip] += 1;
            else:
                attempts[ip] = 1;

    for ip, count in attempts.items():
        if count >= 5:
            print("WARNING: " + ip + " has " + str(count) + " failed attempts")

print(attempts)
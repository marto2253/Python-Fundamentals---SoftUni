def miner_task(seq):
    findings = {}
    # counter = 0
    while seq != "stop":
        quantity = int(input())
        if seq not in findings:
            findings[seq] = quantity
        else:
            findings[seq] += quantity

        seq = input()

    for k, v in findings.items():
        print(f'{k} -> {v}')


sequence = input()
miner_task(sequence)

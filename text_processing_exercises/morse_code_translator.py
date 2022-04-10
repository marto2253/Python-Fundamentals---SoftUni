morse = {
    'A': ' .- ' ,
    'B': ' -... ' ,
    'C': ' .. . ' ,
    'D': ' -.. ' ,
    'E': ' . ',
    'F': ' .-. ' ,
    'G': ' --. ' ,
    'H': ' .... ' ,
    'I': '.. ' ,
    'J': ' -.-. ' ,
    'K': ' -.- ' ,
    'L': ' ⸺ ' ,
    'M': ' -- ' ,
    'N': ' -. ' ,
    'O': ' . . ' ,
    'P': ' ..... ' ,
    'Q': ' ..-. ' ,
    'R': ' . .. ' ,
    'S': ' ... ' ,
    'T': ' - ' ,
    'U': ' ..- ' ,
    'V': ' ...- ' ,
    'W': ' .-- ' ,
    'X': ' .-.. ' ,
    'Y': ' .. .. ' ,
    'Z': ' ... . ' ,
}

morse_message = input().split('|')
split1 = morse_message.split(' ')
for i in morse_message:
    for k, v in morse.items():
        if i == v:
            print(k)
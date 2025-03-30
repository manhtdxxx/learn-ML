sentences = []


while True:
    try:
        input_text = input().strip()
        input_text = input_text.lower()
        current_text = ''
        for i in input_text:
            if i in '.!?':
                current_text = current_text.strip()
                if len(current_text) > 0:  # TH: them vao toan blank space xong strip di thi len = 0
                    current_text += i
                    sentences.append(current_text)
                current_text = ''
            elif i == '\n':
                current_text = current_text.strip()
                if len(current_text) > 0:
                    sentences.append(current_text)
                current_text = ''
            else:
                current_text += i

        # ADD VAO TEXT CUOI NEU i khong thoa man DK dau
        current_text = current_text.strip()
        if len(current_text) > 0:
            sentences.append(current_text)

    except Exception:
        break

for i in sentences:
    x = i.split()
    x = ' '.join(x)
    if x[-1] not in '.!?':
        x = x + '.'
    x = x.capitalize()
    print(x)

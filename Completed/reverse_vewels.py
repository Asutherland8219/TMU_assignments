def reverse_vowels(text):
    vowels = "aeiouAEIOU"
    v_text = ""
    res = ''
    for i in text:
        if i in vowels:
            v_text = i + v_text
            count = 0
            res = ''
    for i in text:
        if i in vowels:
            if i.isupper():
                res += v_text[count].upper()
            else:
                res += v_text[count].lower()
            count += 1
        else:
            res += i
    return res
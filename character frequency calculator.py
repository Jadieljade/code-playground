sentence = 'videl is my small brother and he has healed up'
char_frequency = {}
for char in sentence:
    char_frequency[char] = char_frequency.get(char, 0)+1

char_frequency.pop(' ')
ans = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
final_ans = dict(ans)
print(final_ans)

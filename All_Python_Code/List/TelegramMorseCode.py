# codes having values :- a - z
codes = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
         '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
         '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
         '-.--', '--..']
text = 'deface'
# Get The starting Value Of 'a' in Ascii Code.
start = ord('a')
result = ''
for i in text:
    diff = abs(start - ord(i))
    result += codes[diff] + " "
print(result, end=" ")




from typing import List
 
 
def stat(words: List[str]):
    for w in words:
        if not w.isalnum():
            words.remove(w)
    if not words:
        return print(-1)
    dct = {}
    pal = 0
    for word in words:
        dct[word] = dct.get(word, 0) + 1
        if word == word[::-1]:
            pal += 1
    most = ''
    least = ''
    for k in sorted(dct):
        print(f'{k}: {dct[k]}')
        if dct[k] == max(dct.values()):
            most = k
        if dct[k] == min(dct.values()):
            least = k
    print(f'Most common: {most}')
    print(f'Least common: {least}')
    print(f'Palindromes: {pal}')
    return None
    

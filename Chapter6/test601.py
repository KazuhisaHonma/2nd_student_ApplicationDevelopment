import random
kuji = ['大吉', '中吉', '小吉', '凶']
kekka = random.choice(kuji)
txt = f'結果は、{kekka}でした〜。'
print(txt)

# for _ in range(10):
#     kuji = ['大吉', '中吉', '小吉', '凶']
#     kekka = random.choice(kuji)
#     txt = f'結果は、{kekka}でした〜。'
#     print(txt)
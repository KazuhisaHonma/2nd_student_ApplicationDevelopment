def getnextnum(n):
    nextnum = list(range(n+1, min(32, n+4)))
    choicemsg = f'{nextnum}から入力してください。'
    print(choicemsg)

getnextnum(5)
getnextnum(18)
getnextnum(29)
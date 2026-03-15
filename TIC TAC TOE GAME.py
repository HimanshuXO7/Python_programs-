
"TIC_TAC_TOE game"

li = [1,2,3,4,5,6,7,8,9]
player = 'X'
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
flag = 0
selected = []

while True:
    print("\n\t\t    TIC_TAC_TOE")
    print(f"\n\t\t    {li[0]} | {li[1]} | {li[2]}")
    print("\t\t    ----------")
    print(f"\t\t    {li[3]} | {li[4]} | {li[5]}")
    print("\t\t    ----------")
    print(f"\t\t    {li[6]} | {li[7]} | {li[8]}")

    if flag == 1:
        break

    if len(selected) == 9:
        print("\n\t\t  match tie!!")
        break

    print(f"\n\t\t player {player} turn:", end='')
    ch = int(input())

    if ch not in selected:
        selected.append(ch)
        li[ch-1] = player
    else:
        print("\n\t\t  already selected area\n\t\t try another !!")
        continue

    for a,b,c in wins:
        if li[a]==li[b] and li[b]==li[c]:
            print("\n\t\t player", player, "WIN!")
            flag = 1

    if player == 'X':
        player = 'O'
    else:
        player = 'X'


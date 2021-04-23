"""
ループの中でじゃんけんを何度もする処理を作成します。
相手は必ずグー、チョキ、パーの順で手を出し、こちらは入力を受け付けます。
入力すると：あなたの出した手：○○、相手の出した手：✖️✖️と表示され
相手に勝った場合：「あなたは勝ちました」と表示されループを抜け出せる
負けた場合は：「あなたの負け、再チャレンジ」と表示され3回負けると「あなたは負けました」と表示されループの外に出る
あいこの場合は：「あいこ」と表示される
誤った入力をした場合：再入力してくださいと表示します。
"""


def paper():
    yield 'パー'


def scissors():
    yield 'チョキ'
    yield from paper()


def rock():
    yield 'グー'
    yield from scissors()


def rock_paper_scissors_game(me, opponent):
    if me == opponent:
        return 'あいこ'
    elif me == 'グー':
        if opponent == 'チョキ':
            return '勝ち'
        elif opponent == 'パー':
            return '負け'
    elif me == 'チョキ':
        if opponent == 'グー':
            return '負け'
        elif opponent == 'パー':
            return '勝ち'
    elif me == 'パー':
        if opponent == 'グー':
            return '勝ち'
        elif opponent == 'チョキ':
            return '負け'


opponent = ''
loss_count = 0
gen = rock()

while True:
    me = input('じゃんけんしましょう！グー・チョキ・パーのいずれかを入力してください\n')
    if me not in ['グー', 'チョキ', 'パー']:
        print('再入力してください')
        continue
    try:
        opponent = next(gen)
    except Exception:
        gen = rock()
        opponent = next(gen)
    print(f'あなたの出した手：{me}、相手の出した手：{opponent}')
    result = rock_paper_scissors_game(me, opponent)
    if result == '勝ち':
        print('あなたは勝ちました')
        break
    elif result == '負け':
        loss_count += 1
        if loss_count == 3:
            print('あなたは負けました')
            break
        else:
            print('あなたの負け、再チャレンジ')
    elif result == 'あいこ':
        print('あいこ')

scores = input()
scores = [int(x) for x in scores.split()] # превращаю строку в список чисел
student_score = int(input())

def check_winners(scores, student_score):
    sorted_scores = sorted(scores, reverse=True) # сортировка по убыванию
    if student_score in sorted_scores[:3]:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')

check_winners(scores, student_score)


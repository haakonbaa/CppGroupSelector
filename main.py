from os import name as OS_NAME, system as execute

NUMHOURS = 58
DAYS = ('mandag','tirsdag','onsdag','torsdag','fredag')

def main():
    index = 0
    selection = [' -']*NUMHOURS
    # index = 58
    # selection = list(range(NUMHOURS))
    while index < NUMHOURS:
        print_calendar(selection)
        print('skriv hvor godt den gitte datoen passer')
        print('på en skala fra 0-3. skriv "p","n" for ')
        print('hennholdsvis forrige og neste.')
        day, kl = index_to_daykl(index)
        day = DAYS[day - 1]
        ans = input(f'{day} {kl:02}-{kl+1:02} : ')
        if ans in ('0','1','2','3'):
            selection[index] = int(ans)
            index += 1
        elif ans == 'p' and index > 0:
            index -= 1
        elif ans == 'n' and index < NUMHOURS - 2 and selection[index] != ' -':
            index += 1
    print_calendar(selection)
    print('\nResultat:\n')

    scores = []
    for line in DATA:
        score = 0
        group = line[0]
        text = line[1]
        daykls = line[2:]
        for day, hours in daykls:
            for hour in hours:
                score += selection[daykl_to_index(day,hour)]
        scores.append([group,score,text])
    scores.sort(key=lambda x: -x[1])
    print('gruppe | poeng | tider')
    for group, score, text in scores:
        print(f'   {group:2}  :  {str(score).ljust(4)} : {text}')
    print('ferdig :)')

# ugly hack to check if in Jupyter
try:
    from IPython import get_ipython
    from IPython.display import clear_output
    if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            raise Exception()
    clear = clear_output
except:
    if OS_NAME == 'posix':
        clear = lambda: execute('clear') # clear works, probably
    else:
        clear = lambda: execute('cls') # Windows, probably :)

def print_calendar(selection):
    clear()
    print(calendar.format(*selection))

def index_to_daykl(i):
    if i >= 54:
        i += 1
    day = i % 5
    kl = int( (i - day) // 5 )
    return day + 1, kl + 8

def daykl_to_index(day, kl):
    kl = kl - 8
    day = day - 1
    i = 5 * kl + day
    if i >= 54:
        i -= 1
    return i

DATA = (
    (1, 'Torsdag 12:00 - 14:00  Fredag 12:00 - 16:00', (4, (12, 13)), (5, (12, 13, 14, 15))),
    (2, 'Tirsdag 14:00 - 16:00  Fredag 10:00 - 12:00  Fredag 14:00 - 16:00', (2, (14, 15)), (5, (10, 11)), (5, (14, 15))),
    (3, 'Onsdag 08:00 - 10:00  Onsdag 14:00 - 16:00  Torsdag 10:00 - 12:00', (3, (8, 9)), (3, (14, 15)), (4, (10, 11))),
    (4, 'Mandag 12:00 - 14:00  Onsdag 10:00 - 14:00', (1, (12, 13)), (3, (10, 11, 12, 13))),
    (5, 'Tirsdag 10:00 - 12:00  Onsdag 12:00 - 14:00  Torsdag 10:00 - 12:00', (2, (10, 11)), (3, (12, 13)), (4, (10, 11))),
    (6, 'Tirsdag 10:00 - 12:00  Onsdag 10:00 - 12:00  Torsdag 16:00 - 18:00', (2, (10, 11)), (3, (10, 11)), (4, (16, 17))),
    (7, 'Onsdag 14:00 - 16:00  Torsdag 08:00 - 10:00  Fredag 08:00 - 10:00', (3, (14, 15)), (4, (8, 9)), (5, (8, 9))),
    (8, 'Onsdag 14:00 - 18:00  Torsdag 08:00 - 10:00', (3, (14, 15, 16, 17)), (4, (8, 9))),
    (9, 'Tirsdag 10:00 - 12:00  Torsdag 10:00 - 12:00  Fredag 08:00 - 10:00', (2, (10, 11)), (4, (10, 11)), (5, (8, 9))),
    (10, 'Tirsdag 08:00 - 10:00  Onsdag 08:00 - 10:00  Fredag 14:00 - 16:00', (2, (8, 9)), (3, (8, 9)), (5, (14, 15))),
    (11, 'Tirsdag 12:00 - 14:00  Torsdag 14:00 - 16:00  Fredag 10:00 - 12:00', (2, (12, 13)), (4, (14, 15)), (5, (10, 11))),
    (12, 'Tirsdag 10:00 - 14:00  Torsdag 12:00 - 14:00', (2, (10, 11, 12, 13)), (4, (12, 13))),
    (13, 'Tirsdag 12:00 - 16:00  Torsdag 12:00 - 14:00', (2, (12, 13, 14, 15)), (4, (12, 13))),
    (14, 'Tirsdag 14:00 - 16:00  Fredag 10:00 - 14:00', (2, (14, 15)), (5, (10, 11, 12, 13))),
    (15, 'Tirsdag 14:00 - 16:00  Torsdag 12:00 - 14:00  Fredag 14:00 - 16:00', (2, (14, 15)), (4, (12, 13)), (5, (14, 15))),
    (16, 'Onsdag 18:00 - 20:00  Torsdag 16:00 - 20:00', (3, (18, 19)), (4, (16, 17, 18, 19))),
    (17, 'Onsdag 12:00 - 16:00  Torsdag 16:00 - 18:00', (3, (12, 13, 14, 15)), (4, (16, 17))),
    (18, 'Torsdag 08:00 - 10:00  Torsdag 14:00 - 16:00  Fredag 10:00 - 12:00', (4, (8, 9)), (4, (14, 15)), (5, (10, 11))),
    (19, 'Torsdag 12:00 - 16:00  Fredag 10:00 - 12:00', (4, (12, 13, 14, 15)), (5, (10, 11))),
    (20, 'Mandag 16:00 - 18:00  Onsdag 12:00 - 14:00  Fredag 10:00 - 12:00', (1, (16, 17)), (3, (12, 13)), (5, (10, 11))),
    (21, 'Onsdag 12:00 - 16:00  Fredag 14:00 - 16:00', (3, (12, 13, 14, 15)), (5, (14, 15))),
    (22, 'Onsdag 12:00 - 14:00  Onsdag 18:00 - 20:00  Fredag 12:00 - 14:00', (3, (12, 13)), (3, (18, 19)), (5, (12, 13))),
    (23, 'Tirsdag 08:00 - 12:00  Fredag 12:00 - 14:00', (2, (8, 9, 10, 11)), (5, (12, 13))),
    (24, 'Torsdag 12:00 - 14:00  Fredag 08:00 - 10:00  Fredag 12:00 - 14:00', (4, (12, 13)), (5, (8, 9)), (5, (12, 13))),
    (25, 'Mandag 12:00 - 14:00  Fredag 12:00 - 16:00', (1, (12, 13)), (5, (12, 13, 14, 15))),
    (26, 'Mandag 12:00 - 14:00  Onsdag 16:00 - 18:00  Fredag 10:00 - 12:00', (1, (12, 13)), (3, (16, 17)), (5, (10, 11))),
    (27, 'Tirsdag 12:00 - 16:00  Fredag 08:00 - 10:00', (2, (12, 13, 14, 15)), (5, (8, 9))),
    (28, 'Tirsdag 14:00 - 16:00  Torsdag 10:00 - 12:00  Fredag 08:00 - 10:00', (2, (14, 15)), (4, (10, 11)), (5, (8, 9))),
    (29, 'Mandag 14:00 - 16:00  Onsdag 14:00 - 18:00', (1, (14, 15)), (3, (14, 15, 16, 17))),
    (30, 'Mandag 16:00 - 18:00  Tirsdag 08:00 - 10:00  Torsdag 18:00 - 20:00', (1, (16, 17)), (2, (8, 9)), (4, (18, 19))),
    (31, 'Mandag 12:00 - 14:00  Tirsdag 12:00 - 16:00', (1, (12, 13)), (2, (12, 13, 14, 15))),
    (32, 'Mandag 10:00 - 12:00  Tirsdag 18:00 - 20:00  Onsdag 08:00 - 10:00', (1, (10, 11)), (2, (18, 19)), (3, (8, 9))),
    (33, 'Mandag 10:00 - 12:00  Torsdag 10:00 - 12:00  Fredag 10:00 - 12:00', (1, (10, 11)), (4, (10, 11)), (5, (10, 11))),
    (34, 'Onsdag 12:00 - 16:00  Torsdag 14:00 - 16:00', (3, (12, 13, 14, 15)), (4, (14, 15))),
    (35, 'Onsdag 10:00 - 12:00  Fredag 12:00 - 16:00', (3, (10, 11)), (5, (12, 13, 14, 15))),
    (36, 'Mandag 14:00 - 16:00  Onsdag 10:00 - 12:00  Fredag 14:00 - 16:00', (1, (14, 15)), (3, (10, 11)), (5, (14, 15))),
    (37, 'Mandag 08:00 - 10:00  Onsdag 16:00 - 18:00  Fredag 08:00 - 10:00', (1, (8, 9)), (3, (16, 17)), (5, (8, 9))),
    (38, 'Mandag 14:00 - 16:00  Tirsdag 12:00 - 14:00  Fredag 08:00 - 10:00', (1, (14, 15)), (2, (12, 13)), (5, (8, 9))),
    (39, 'Mandag 08:00 - 10:00  Onsdag 14:00 - 16:00  Torsdag 10:00 - 12:00', (1, (8, 9)), (3, (14, 15)), (4, (10, 11))),
    (40, 'Onsdag 12:00 - 14:00  Torsdag 08:00 - 12:00', (3, (12, 13)), (4, (8, 9, 10, 11))),
    (41, 'Onsdag 14:00 - 16:00  Torsdag 10:00 - 12:00  Fredag 12:00 - 14:00', (3, (14, 15)), (4, (10, 11)), (5, (12, 13))),
    (42, 'Onsdag 10:00 - 12:00  Fredag 10:00 - 14:00', (3, (10, 11)), (5, (10, 11, 12, 13))),
    (43, 'Mandag 10:00 - 12:00  Onsdag 12:00 - 14:00  Torsdag 12:00 - 14:00', (1, (10, 11)), (3, (12, 13)), (4, (12, 13))),
    (44, 'Tirsdag 16:00 - 18:00  Torsdag 12:00 - 16:00', (2, (16, 17)), (4, (12, 13, 14, 15))),
    (45, 'Mandag 14:00 - 16:00  Torsdag 12:00 - 16:00', (1, (14, 15)), (4, (12, 13, 14, 15))),
    (46, 'Tirsdag 12:00 - 14:00  Onsdag 10:00 - 12:00  Fredag 12:00 - 14:00', (2, (12, 13)), (3, (10, 11)), (5, (12, 13))),
    (47, 'Tirsdag 14:00 - 16:00  Torsdag 08:00 - 12:00', (2, (14, 15)), (4, (8, 9, 10, 11))),
    (48, 'Mandag 12:00 - 16:00  Onsdag 10:00 - 12:00', (1, (12, 13, 14, 15)), (3, (10, 11))),
    (49, 'Tirsdag 16:00 - 20:00  Torsdag 18:00 - 20:00', (2, (16, 17, 18, 19)), (4, (18, 19))),
    (50, 'Tirsdag 16:00 - 18:00  Onsdag 18:00 - 20:00  Torsdag 18:00 - 20:00', (2, (16, 17)), (3, (18, 19)), (4, (18, 19))),
    (51, 'Mandag 18:00 - 20:00  Torsdag 16:00 - 20:00', (1, (18, 19)), (4, (16, 17, 18, 19))),
    (52, 'Mandag 14:00 - 16:00  Torsdag 12:00 - 16:00', (1, (14, 15)), (4, (12, 13, 14, 15))),
    (53, 'Mandag 12:00 - 16:00  Torsdag 08:00 - 10:00', (1, (12, 13, 14, 15)), (4, (8, 9))),
    (54, 'Onsdag 14:00 - 18:00  Torsdag 16:00 - 18:00', (3, (14, 15, 16, 17)), (4, (16, 17))),
    (55, 'Onsdag 08:00 - 10:00  Fredag 10:00 - 14:00', (3, (8, 9)), (5, (10, 11, 12, 13))),
    (56, 'Mandag 14:00 - 16:00  Torsdag 14:00 - 18:00', (1, (14, 15)), (4, (14, 15, 16, 17))),
    (57, 'Onsdag 10:00 - 12:00  Torsdag 14:00 - 16:00  Fredag 10:00 - 12:00', (3, (10, 11)), (4, (14, 15)), (5, (10, 11))),
    (58, 'Tirsdag 12:00 - 16:00  Torsdag 10:00 - 12:00', (2, (12, 13, 14, 15)), (4, (10, 11))),
    (59, 'Mandag 12:00 - 14:00  Onsdag 18:00 - 20:00  Torsdag 12:00 - 14:00', (1, (12, 13)), (3, (18, 19)), (4, (12, 13))),
    (60, 'Mandag 14:00 - 16:00  Onsdag 14:00 - 16:00  Torsdag 16:00 - 18:00', (1, (14, 15)), (3, (14, 15)), (4, (16, 17))),
    (61, 'Tirsdag 14:00 - 16:00  Onsdag 14:00 - 16:00  Fredag 10:00 - 12:00', (2, (14, 15)), (3, (14, 15)), (5, (10, 11))),
    (62, 'Onsdag 16:00 - 18:00  Torsdag 12:00 - 16:00', (3, (16, 17)), (4, (12, 13, 14, 15))),
    (63, 'Onsdag 10:00 - 14:00  Fredag 14:00 - 16:00', (3, (10, 11, 12, 13)), (5, (14, 15))),
    (64, 'Tirsdag 08:00 - 10:00  Fredag 10:00 - 12:00  Fredag 14:00 - 16:00', (2, (8, 9)), (5, (10, 11)), (5, (14, 15))),
    (65, 'Mandag 14:00 - 16:00  Torsdag 14:00 - 18:00', (1, (14, 15)), (4, (14, 15, 16, 17))),
    (66, 'Tirsdag 16:00 - 18:00  Torsdag 08:00 - 10:00  Fredag 12:00 - 14:00', (2, (16, 17)), (4, (8, 9)), (5, (12, 13))),
    (67, 'Onsdag 14:00 - 16:00  Torsdag 12:00 - 16:00', (3, (14, 15)), (4, (12, 13, 14, 15))),
    (68, 'Mandag 16:00 - 18:00  Torsdag 16:00 - 20:00', (1, (16, 17)), (4, (16, 17, 18, 19))),
    (69, 'Mandag 08:00 - 10:00  Fredag 08:00 - 10:00  Fredag 12:00 - 14:00', (1, (8, 9)), (5, (8, 9)), (5, (12, 13))),
    (70, 'Tirsdag 14:00 - 16:00  Torsdag 18:00 - 20:00  Fredag 14:00 - 16:00', (2, (14, 15)), (4, (18, 19)), (5, (14, 15)))
)

possible_hours = (
    (1, tuple(range(8,16-1))),
    (2, tuple(range(8,16-1))),
    (3, tuple(range(8,16-1))),
    (4, tuple(range(8,16-1))),
    (5, tuple(range(8,14-1)))
)

# not an elegant solution, but maybe a fast one?
calendar = """klokka   man   tir    ons   tor   fre  
08-09    {:2}    {:2}     {:2}    {:2}    {:2}   
09-10    {:2}    {:2}     {:2}    {:2}    {:2}   
10-11    {:2}    {:2}     {:2}    {:2}    {:2}   
11-12    {:2}    {:2}     {:2}    {:2}    {:2}   
12-13    {:2}    {:2}     {:2}    {:2}    {:2}   
13-14    {:2}    {:2}     {:2}    {:2}    {:2}   
14-15    {:2}    {:2}     {:2}    {:2}    {:2}   
15-16    {:2}    {:2}     {:2}    {:2}    {:2}   
16-17    {:2}    {:2}     {:2}    {:2}    {:2}   
17-18    {:2}    {:2}     {:2}    {:2}    {:2}   
18-19    {:2}    {:2}     {:2}    {:2}
19-20    {:2}    {:2}     {:2}    {:2} """

if __name__ == '__main__':
    main()
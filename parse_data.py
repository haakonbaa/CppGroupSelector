day_num = {
    'Mandag'    : 1,
    'Tirsdag'   : 2,
    'Onsdag'    : 3,
    'Torsdag'   : 4,
    'Fredag'    : 5
}

def main():
    with open('./data.txt','r') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            line[0] = int(line[0])
            del line[1]
            for i in range(1,len(line)):
                first_space = line[i].find(' ')
                day = line[i][:first_space]
                kl = line[i][first_space+1:]
                start = int(kl[:2])
                stop = int(kl[8:10])
                line[i] = [day_num[day],list(range(start,stop))]
            print(line)

if __name__ == '__main__':
    main()
import codecs

subj = {}
with codecs.open('test_6.txt', 'r', "utf_8_sig") as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = sum([int(s) for s in line.split() if s.isdigit()])

    print(f'Total hours for each subject - \n {subj}')
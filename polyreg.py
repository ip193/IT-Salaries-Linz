import csv

import numpy as np

import matplotlib.pyplot as plt


def findmax(a, num):  # return a list of the num highest values (by index)

    ret = []

    for j in range(num):

        current_best = 0

        highest = 0

        for i in range(len(a)):

            if (a[i] >= highest) and (i not in ret):
                current_best = i

                highest = a[i]

        ret.append(current_best)

    return ret


def higher(a, exp):  # find all members of _a_ with values > exp

    ret = []

    for i in range(len(a)):

        if a[i] > exp:
            ret.append(i)

    return ret


# Get the data

filename = 'responses_clean.csv'

salaries = []

y_o_e = []

gender = []

with open(filename, 'r') as f:  # extract the data

    reader = csv.reader(f)

    for line in reader:

        try:

            if line[3]:

                y_o_e.append(float(line[3]))

            else:

                continue

            word = line[7]  # store gender as a letter

            if word:

                word = word[0]

                if word == 'W':
                    word = 'F'

                gender.append(word)
            else:

                gender.append('N')

            salaries.append(int(line[1]))  # all entries have salaries

        except:

            print("Error Found!")

            print(line)

            pass

# print(len(salaries) , len(gender) , len(y_o_e))

assert (len(salaries) == len(gender) == len(y_o_e))

males = []

females = []

all_list = []  # will be replaced later

for i in range(len(salaries)):

    tuple = (salaries[i], y_o_e[i])

    if gender[i] == 'M':

        males.append(tuple)

    elif gender[i] == 'F':

        females.append(tuple)

    else:  # other/no gender

        all_list.append(tuple)

# Set up arrays

males_x = np.array([males[i][1] for i in range(len(males))])

males_y = np.array([males[i][0] for i in range(len(males))])

all_x = np.array([all_list[i][1] for i in range(len(all_list))])  # unspecified gender goes here

all_y = np.array([all_list[i][0] for i in range(len(all_list))])

females_x = np.array([females[i][1] for i in range(len(females))])

females_y = np.array([females[i][0] for i in range(len(females))])

all_x = np.concatenate((all_x, males_x, females_x))

all_y = np.concatenate((all_y, males_y, females_y))

removed_size = 3

removed_size_low_exp = 3

removed = findmax(males_y, removed_size)

truncated_males_x = males_x
truncated_males_y = males_y

truncated_males_x = np.delete(truncated_males_x, removed)  # take out the outliers
truncated_males_y = np.delete(truncated_males_y, removed)

highest_female_exp = findmax(females_x, 1)

experienced_males = higher(males_x, females_x[
    highest_female_exp[0]])  # find the set of men who are more experienced than all women

exp_pay_truncated_males_x = males_x
exp_pay_truncated_males_y = males_y

exp_pay_truncated_males_x = np.delete(exp_pay_truncated_males_x,
                                      experienced_males)  # remove very experienced men from the set
exp_pay_truncated_males_y = np.delete(exp_pay_truncated_males_y, experienced_males)

high_paid_low_exp = findmax(exp_pay_truncated_males_y, removed_size_low_exp)

exp_pay_truncated_males_x = np.delete(exp_pay_truncated_males_x, high_paid_low_exp)  # remove the top paid men
exp_pay_truncated_males_y = np.delete(exp_pay_truncated_males_y, high_paid_low_exp)

assert (truncated_males_y.size == truncated_males_x.size == (len(males_y) - removed_size))

assert (males_y[findmax(males_y, 1)[0]] > truncated_males_y[findmax(truncated_males_y, 1)[0]])

assert (exp_pay_truncated_males_y.size == exp_pay_truncated_males_x.size)

assert (len(exp_pay_truncated_males_x) < len(truncated_males_x))

assert (exp_pay_truncated_males_x.max() <= females_x.max())

truncated_all_x = np.concatenate(
    (np.array([all_list[i][1] for i in range(len(all_list))]), truncated_males_x, females_x))

truncated_all_y = np.concatenate(
    ((np.array([all_list[i][0] for i in range(len(all_list))]), truncated_males_y, females_y)))

assert (truncated_all_x != all_x and truncated_males_y != males_y)

#  Do the regression analysis

truncated_males_p1 = np.poly1d(np.polyfit(truncated_males_x, truncated_males_y, 1))

truncated_all_p1 = np.poly1d(np.polyfit(truncated_all_x, truncated_all_y, 1))

exp_pay_truncated_males_p1 = np.poly1d(np.polyfit(exp_pay_truncated_males_x, exp_pay_truncated_males_y, 1))

females_p1 = np.poly1d(np.polyfit(females_x, females_y, 1))

males_p1 = np.poly1d(np.polyfit(males_x, males_y, 1))

all_p1 = np.poly1d(np.polyfit(all_x, all_y, 1))

males_p3 = np.poly1d(np.polyfit(males_x, males_y, 3))

females_p3 = np.poly1d(np.polyfit(females_x, females_y, 3))

all_p3 = np.poly1d(np.polyfit(all_x, all_y, 3))

#  Plot the results

xp = np.linspace(0, 25, 100)

plt.title('IT-Gehälter in Linz (ohne ' + str(removed_size) + ' Ausreißer)')

plt.plot(truncated_all_x, truncated_all_y, 'c.')

plt.plot(xp, truncated_all_p1(xp), 'k--',
         label='Erwartetes Gehalt, r = ' + str(int(np.corrcoef(truncated_all_x, truncated_all_y)[0, 1] * 100) / 100))

plt.ylabel('Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.legend()

plt.show()

plt.title('Jahresverdienst IT-Branchen in Linz')

plt.xlabel('Jahre der Berufserfahrung')

plt.subplot(2, 2, 1)

plt.plot(all_x, all_y, 'c.', xp, all_p1(xp), 'k-')  # xp , all_p3(xp), '-',

plt.ylabel('Alle - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.subplot(2, 2, 2)

plt.plot(males_x, males_y, 'r.', xp, males_p1(xp), 'r--')  # xp, 'males_p3(xp), '-',

plt.ylabel('Nur Männer - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.subplot(2, 2, 3)

plt.plot(females_x, females_y, 'b.', xp, females_p1(xp), 'b--')

plt.ylabel('Nur Frauen - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.subplot(2, 2, 4)

plt.plot(females_x, females_y, 'b.')

plt.plot(males_x, males_y, 'r.')

plt.plot(xp, females_p1(xp), 'b--', label='Frauen')

plt.plot(xp, males_p1(xp), 'r--', label='Männer', )  # xp, all_p1(xp), '-.'

plt.ylabel('Vergleich Männer, Frauen - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.legend()

plt.show()

plt.title('Ohne' + str(removed_size) + ' Ausreißer - Jahresgehalt')

plt.subplot(2, 1, 1)

plt.plot(truncated_males_x, truncated_males_y, 'r.', xp, truncated_males_p1(xp), 'r--')

plt.ylabel('Männer ohne Ausreißer - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.subplot(2, 1, 2)

plt.plot(truncated_all_x, truncated_all_y, 'c.', xp, truncated_all_p1(xp), 'k-')

plt.ylabel('Alle ohne Ausreißer - Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.ylim(20000, 160000)

plt.legend()

plt.show()

plt.title('Vergleich Männer und Frauen ohne ' + str(removed_size) + ' Ausreißer')

plt.ylabel('Jahresgehalt')

plt.xlabel('Jahre der Berufserfahrung')

plt.plot(truncated_males_x, truncated_males_y, 'r.')

plt.plot(females_x, females_y, 'b.')

plt.plot(xp, females_p1(xp), 'b--', label='Frauen')

plt.plot(xp, truncated_males_p1(xp), 'r--', label='Männer', )  # xp, all_p1(xp), '-.'

plt.ylim(20000, 160000)

plt.legend()
plt.show()

plt.title('Männer und Frauen mit Erfahrung <= 12 Jahre, ohne ' + str(removed_size_low_exp) + ' Ausreißer')

plt.plot(females_x, females_y, 'b.')

plt.plot(exp_pay_truncated_males_x, exp_pay_truncated_males_y, 'r.')

plt.plot(xp, females_p1(xp), 'b--', label='Frauen')

plt.plot(xp, exp_pay_truncated_males_p1(xp), 'r--', label='Männer', )  # xp, all_p1(xp), '-.'

plt.ylabel('Jahresgehalt')
plt.xlabel('Jahre der Berufserfahrung')

plt.legend()

plt.show()

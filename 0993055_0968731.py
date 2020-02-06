# student_number1: 0993055 first_name1: Danny last_name1: Kariman
# student_number2: 0968731 first_name2: Ali last_name2: Sahar



import random
import matplotlib.pyplot as plt

#Players rolling per strat
def strat1():
    totalScore = 0
    while totalScore < 12:
        i = random.randint(0,6)
        if i == 1:
            return 0
        totalScore += i
    return totalScore

def strat2():
    totalScore = 0
    while totalScore < 33:
        i = random.randint(0,6)
        if i == 1:
            return 0
        totalScore += i
    return totalScore

def strat3(x):
    totalScore = 0
    while totalScore < x:
        i = random.randint(0,6)
        if i == 1:
            return 0
        totalScore += i
    return totalScore


#This function helps run the simulation of the Greedy Pig Game
def GameSim(x):
    total = [0,0,0]

    while total[0] < 100 and total[1] < 100 and total[2] < 100:
        total[0] += strat1()
        total[1] += strat2()
        total[2] += strat3(x)

    return total.index(max(total)) + 1

#Runs the sim with strats calculated
def RunSim(rolls, s, showgraph = False):
    strat1 = 0
    strat2 = 0
    strat3 = 0

    for _ in range(rolls):
        winner = GameSim(s)
        if winner == 1:
            strat1 += 1
        elif winner == 2:
            strat2 += 1
        elif winner == 3:
            strat3 += 1
    res = [strat1 / rolls * 100 , strat2 / rolls * 100 , strat3 / rolls * 100]
    res1 = strat1 / rolls * 100
    res2 = strat2 / rolls * 100
    res3 = strat3 / rolls * 100
    if showgraph:
        x = ['Strategy 1', 'Strategy 2', 'Strategy 3']
        bar1 = plt.bar(x[0], res1, color = 'red')
        bar2 = plt.bar(x[1], res2, color = 'grey')
        bar3 = plt.bar(x[2], res3, color = 'blue')
        plt.ylabel('Probability of winning')
        plt.legend([bar1, bar2, bar3], ['Strategy 1 (' + str(int(res1)) + '%)', 'Strategy 2 (' + str(int(res2)) + '%)' , 'Strategy 3 (' + str(int(res3)) + '%)' ])
        plt.axis([-1,3,0,100])
                                
        plt.show()
    return res

#Calculating strat3 chances
def calc3():
    probability = []
    print('Calculating the ideal strategy..')
    
    for i in range(1, 151):
        strat3win = RunSim(1000, i)[2]
        probability.append(strat3win)

    return probability.index(max(probability)) + 1


s = calc3()
print('Strategy 3 = ' + str(s))
print(RunSim(10000, s, showgraph=True))

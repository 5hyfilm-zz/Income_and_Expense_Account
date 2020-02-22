import matplotlib.pyplot as plt
import seaborn as sns

def instruction():
    print('')
    print('\tHow to use this program')
    print('')
    print('Please fill out information in baht')
    print('')
    print('Continue filling To calculate the next month')
    print('')
    print('Enter 0 in the Income or Expense box to stop.')

def information():
    print('')
    print('If you want to see information about income and expense accounts, press 1. If not, press 0.')
    print('')
    press = int(input('Choose number: '))
    if press == 1:
        f = open('information.txt')
        reader = f.read()
        print('')
        print(reader)
        #print('-'*117)
        f.close()
    elif press == 0:
        print('')

def data_visualization(x_list, y_list):
    sns.set(style="white", rc={"lines.linewidth": 3})
    fig, ax1 = plt.subplots(figsize=(10,10))
    ax2 = ax1.twinx()
    sns.barplot(x=x_list,
                y=y_list, 
                color='#004488',
                ax=ax1)
    sns.lineplot(x=x_list, 
                 y=y_list,
                 color='r',
                 marker="o",
                 ax=ax2)
    plt.xlabel('Total [Baht]')
    plt.ylabel('Month')
    plt.title('Total Graph')
    plt.show()
    sns.set()
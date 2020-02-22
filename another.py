import matplotlib.pyplot as plt
import seaborn as sns

def instruction():
    print('')
    print('\tHow to use this program')
    print('')
    print('Please fill out information in baht')
    print('')

def information():
    print('')
    print('ถ้าต้องการดูข้อมููลเกี่ยวกับบัญชีรายรับ-รายจ่าย กด 1 ถ้าไม่ต้องการกด 0')
    print('')
    press = int(input('เลืือกหมายเลข: '))
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
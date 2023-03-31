import pandas as pd
import numpy as np
import pendulum
from pathlib import Path

result_file = ('phone_random/result')

def split_last_two(e):
    
    e = str(e)
    last_two = e[-2:]
    
    return last_two

def create_random_array_2():

    '''create random array and check distribution'''
    df = pd.DataFrame(columns = ['random_num', 'distribution_checking', 'num_with_0'])
    df['distribution_checking'] = np.zeros((1000,), dtype=int)
    while df['distribution_checking'][499] != 50:
        df['random_num'] = np.random.randint(100, size = 1000)
        df['distribution_checking'] = df['random_num'].apply(split_last_two).astype(int)
        df = df.sort_values(by = 'distribution_checking')
        df = df.reset_index(drop = True)
        
    return df

def create_random_array_4():

    '''create random array and check distribution'''
    df = pd.DataFrame(columns = ['random_num', 'distribution_checking', 'num_with_0'])
    df['distribution_checking'] = np.zeros((1000,), dtype=int)
    while df['distribution_checking'][499] != 50:
        df['random_num'] = np.random.randint(10000, size = 1000)
        df['distribution_checking'] = df['random_num'].apply(split_last_two).astype(int)
        df = df.sort_values(by = 'distribution_checking')
        df = df.reset_index(drop = True)
    
    return df


def transform_array_2(df):

    '''transform array to special format'''
    num_check_list = []
    for num in df['random_num']:
        if len(str(num)) == 2:
            num_check_list.append(' ' + str(num) + ' ') 
        elif len(str(num)) == 1:
            num_check_list.append(' 0' + str(num) + ' ') 
        else:
            print('Error')   
    df['num_with_0'] = num_check_list

    return df

def transform_array_4(df):

    '''transform array to special format'''
    num_check_list = []
    for num in df['random_num']:
        if len(str(num)) == 4:
            num_check_list.append(' ' + str(num) + ' ') 
        elif len(str(num)) == 3:
            num_check_list.append(' 0' + str(num) + ' ') 
        elif len(str(num)) == 2:
            num_check_list.append(' 00' + str(num) + ' ')
        elif len(str(num)) == 1:
            num_check_list.append(' 000' + str(num) + ' ')
        else:
            print('Error')   
    df['num_with_0'] = num_check_list

    return df

def main():
    num_type = input('請輸入 2 或 4：')
    if num_type == '2':
        print('開始產生末兩碼隨機')
        df = create_random_array_2()
        df = transform_array_2(df)
        datetime_str = pendulum.now().format('YYYYMMDDHHmmss')
        df.to_excel((f'result/two_num_random_{datetime_str}.xlsx'), index=False)
       

    elif num_type == '4':
        print('開始產生末四碼隨機')
        df = create_random_array_4()
        df = transform_array_4(df)
        datetime_str = pendulum.now().format('YYYYMMDDHHmmss')
        df.to_excel((f'result/four_num_random_{datetime_str}.xlsx'), index=False)

    else:
        print('錯誤')
        pass

if __name__ == "__main__":
    main()

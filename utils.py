import queue
import os
import struct
import pandas as pd
import matplotlib.pyplot as plt


def read_tdx_day_file(file_path):
    data_set = []
    with open(file_path, 'rb') as fl:
        buffer = fl.read()
        size = len(buffer)
        row_size = 32
        code = os.path.basename(file_path).replace('.day', '')
        for i in range(0, size, row_size):
            row = list(struct.unpack('IIIIIfII', buffer[i:i + row_size]))
            row[1] = row[1] / 100
            row[2] = row[2] / 100
            row[3] = row[3] / 100
            row[4] = row[4] / 100
            row.pop()
            row.insert(0, code)
            data_set.append(row)

    df = pd.DataFrame(data=data_set, columns=['code', 'tradeDate', 'open', 'high', 'low', 'close', 'amount', 'vol'])
    return df


def gen_model_datum_from_file(step, feature_num, file_path):
    feature_q = queue.Queue(maxsize=step)
    feature_qb = queue.Queue(maxsize=step)
    df = read_tdx_day_file(file_path)
    df["nextCLose"] = df["close"].shift(axis=0, periods=-1, fill_value=0)
    df = df[:-1]
    f_list = []
    for index, row in df.iterrows():
        feature_q.put(row[1:-1])
        # print("index:{}".format(index))
        if index >= step - 1:
            row_list = []
            for i in range(step):
                if i == 0:
                    row_ = feature_q.get()
                else:
                    row_ = feature_q.get()
                    feature_qb.put(row_)
                row_list.extend(row_.values.tolist())
                # for j in range(row.size):
                #     col_name=row.keys()[j]+"_"+str(i)
                #     df_c.loc[index-step+1:col_name]=row.values[j]
            row_list.append(row[-1])
            row_list.insert(0, row[0])
            f_list.append(row_list)
            feature_q = feature_qb
            # print("qsize:{}".format(feature_q.qsize()))
            # print(row)
    # print(f_list)
    columns_name = gen_columns_name(df.columns,step)
    df = pd.DataFrame(f_list,columns=columns_name)
    df.to_csv(file_path.split(".")[0]+"_"+str(step)+".csv",index=False)
    return df

def gen_model_datum(step, feature_num,file_path="data/sh000001.day"):
    df = gen_model_datum_from_file(step, feature_num,file_path)
    columns = df.columns.tolist()[1:]
    columns_drop = []
    for column in columns:
        if "tradeDate" in column:
            columns_drop.append(column)
    columns_drop.append("code")
    print(columns_drop)

    X = df.drop(columns=columns_drop)
    y = df['predict']
    return X,y


def plot_y(y,file,file_path):
    plt.plot(y)
    plt.savefig(file_path.split(".")[0] + ".png")
    plt.show()


def gen_columns_name(columns,step):
    columns_name = []
    columns_l = columns[1:-1]
    for i in range(step):
        for j in range(len(columns_l)):
            columns_name.append(columns_l[j]+"_"+str(i))
    columns_name.append("predict")
    columns_name.insert(0,columns[0])
    return columns_name


if __name__ == '__main__':
    X,y=gen_model_datum(step=3,feature_num=20)
    print(X)
    print(y)

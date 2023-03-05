import json
import os
import chardet
from collections import OrderedDict


def get_encoding(file):
    #二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']

def make_unique(key, dct):
    counter = 0
    unique_key = key
    while unique_key in dct:
        counter += 1
        unique_key = '{}_{}'.format(key, counter)
    return unique_key

def parse_object_pairs(pairs):
    dct = OrderedDict()
    for key, value in pairs:
        if key in dct:
            key = make_unique(key, dct)
        dct[key] = value
    return dct


def JsonOperation(jsonRoot):
    print(jsonRoot)

def FileRead():
    floderPath = "D:\\software\\pythonCommunity\\project\\git\\pythonLearning\\data"
    for root, dirs, files in os.walk(floderPath):
        for file in files:
            filePath = root + '\\' + file
            if "testcase" not in file:
                continue
            print(filePath)
            try:
                jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5, "a":3}'
                text = json.loads(jsonData, object_pairs_hook=parse_object_pairs)
                print(text)
                with open(filePath, "r", object_pairs_hook=parse_object_pairs, encoding=get_encoding(filePath)) as fp:
                    jsonRoot = json.loads(fp)
                    jsonRoot = JsonOperation(jsonRoot)

                with open(filePath, "wb", encoding='utf-8') as f:

                    # json.dump(dict_var, f)  # 写为一行
                    json.dump(jsonRoot, f, indent=2, sort_keys=True, ensure_ascii=True)  # 写为多行
            except:
                print(filePath)

def main():
    print("Begin")
    FileRead()
    print("End")


if __name__=="__main__":
    main()
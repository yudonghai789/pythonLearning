import json
import os








def JsonOperation(jsonRoot):
    print(jsonRoot)

def FileRead():
    floderPath = "D:\\software\\pythonCommunity\\project\\数据"
    for root, dirs, files in os.walk(floderPath):
        for file in files:
            filePath = root + '\\' + file
            print(filePath)
            try:
                with open(filePath, "r", encoding='utf-8') as f:
                    jsonRoot = json.load(f)
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
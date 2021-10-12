def format(data):
    for i in data:
        print('--------------------------------')
        for k, v in i.items():
            print(k, ':', v)

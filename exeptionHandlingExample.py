try:
    a = int(input())
    b = 1
    print(b/a)
except Exception as e:
    print('Failed, because of this error: '+ str(e))
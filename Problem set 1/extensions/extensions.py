file = input('File name: ').strip().split('.')
dic = {'txt':'text/plain',
       'jpg':'image/jpeg',
       'jpeg':'image/jpeg',
       'png':'image/png',
       'gif':'image/gif',
       'pdf':'application/pdf',
       'zip':'application/zip',
       }
temp = file[-1].lower()
if(temp in dic.keys()):
    print(dic[temp])
else:
    print('application/octet-stream')
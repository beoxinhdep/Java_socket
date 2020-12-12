from pytrends.request import TrendReq
import pandas as pd
import time
import jpysocket
import json 


host="localhost" #Host Name
port=12345    #Port Number
s=jpysocket.jpysocket() #Create Socket
s.bind((host,port)) #Bind Port And Host
s.listen(5) #Socket is Listening
test = "Socket Is Listening...."

pytrend = TrendReq(hl='vi_VN', tz=420)
dataset = []
key_word = []
time_frame = '2020-11-09 2020-11-22'
geo = 'VN'
cat = 0
gprop = ''

print(test)


while True:
    connection,address=s.accept() #Accept the Connection
    print("Connected To ",address)
    while 1:
        
        data1 = connection.recv(1024)
        if not data1:
            break
        print("RECIEVED FROM JAVA SERVER:" , jpysocket.jpydecode(data1))
        key_word = []
        key_word.append(jpysocket.jpydecode(data1))
        pytrend.build_payload(key_word, geo = geo, timeframe = time_frame, cat = cat, gprop = gprop)

        data = pytrend.interest_over_time()

        if not data.empty:
                 data = data.drop(labels=['isPartial'],axis='columns')
#                 data['Date'] = pd.to_datetime(data.index, format="%m/%d/%Y").astype(str)
#                 data['Date'] = data.index.values.astype(str)
#                 data = data[['Date']]
                 dataset = []
                 dataset.append(data)
                 
        result = pd.concat(dataset, axis=1)
        result.to_csv(r"C:\Users\Admin\Desktop\Java_socket\Trend\src\search_trends.csv")
        dataa = "Send success!!!"
#        dataa = jpysocket.jpyencode(dataa)
#        dataset1 =json.dumps(data.to_dict(orient='list'))
        data1 = jpysocket.jpyencode(dataa)
        connection.send(data1) #Send Msg
        print("SEND TO JAVA SERVER:" , dataset)
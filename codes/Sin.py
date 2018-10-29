import csv

ID=input('Enter the user ID:')
with open('1-edges.csv') as csvfile:
    readCSV=csv.reader(csvfile, delimiter=',')
    Connected_users=[]
    

    for row in readCSV:
        if(row[0]==ID):
            Connected_users.append(row[1])

print('Connected_users:',Connected_users)

with open('ratings1.csv') as rating:
    readCSV2=csv.reader(rating,delimiter=',')
    subscriptions=[]

    for row in readCSV2:
        if((row[2]=='5' or '4') and (row[0] in Connected_users)):
            if(row[1] not in subscriptions):
                subscriptions.append(row[1])
    if not subscriptions:               
        print ('No recommendations')
    else:
        print('Recommended subscriptions:',subscriptions)
        
    
        

    

#vehicle_count = 15 
#green_time = 10 + vehicle_count * 2 
#print('Green time:', green_time)



#signal_state = 'GREEN'

#if signal_state == 'GREEN':
   # print('Gaadiyaan chal sakti hain!')
#else:
    #print('Ruko!')




#lanes = ['North', 'South', 'East', 'West']

#for lane in lanes:
   # print('Lane:', lane)



import cv2
img = cv2.imread('traffic.jpg')
cv2.imshow('Traffic', img) 
cv2.destroyAllWindows()

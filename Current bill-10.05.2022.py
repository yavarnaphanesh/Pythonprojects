print("T S S P D C L".center(30))
print("ELECTRICITY".center(30))
print("BILL-CUM NOTICE".center(30))
print("-"*30)
import datetime # copied from online need to explain
current_time = datetime.datetime.now() 
print(current_time)
sno = int(input("S.No: "))
name= input("Consumer name :")
addr= input("Address :")
print("-"*30)

curr_met_red = int(input("Current  Meter Reading : "))
prev_met_red = int(input("Pevious Meter Reading  : "))

print("Present Units : ",curr_met_red)
print("Previous Units: ",prev_met_red)
units = (curr_met_red-prev_met_red)
print("Units cosumed :",units)


print("-"*30)



"""Telangana electricity slab or tariff rates
Category 1(between - 0to 100)
0-50 Units - ₹1.45 consumer charges : 25₹
51-100 units - ₹ 2.60 consumer charges : 30₹

Category 2(between - 100 to 200)
0-100 Units - ₹3.30 consumer charges : ₹50
101-200 units - ₹ 4.30 consumer charges : 50₹
Category 3(more than 200 units)
0-200 Units - ₹5 consumer charges : ₹60
201-300 units - ₹ 7.20 consumer charges : ₹60
301-400 units - ₹ 8.50 consumer charges : ₹80
401-800 units - ₹ 9 consumer charges : ₹80
Above 800 Units - ₹ 9.5 consumer charges : ₹80"""

if units<=100:
  cat=1
  print("You are belogns to Category 1"), print("between - 0to 100".center(30))
if units>100 and units<=200:
  cat=2
  print("You are belogns to Category 2"), print("between - 100to 100".center(30))
if units>200:
  cat=3
  print("You are belogns to Category 2"), print("more than 300".center(30))

if cat==1:
  if units<=50:
    charge=(units*1.95)
    cc=25.00
    duty=units*0.06    
    bill= charge+cc+duty
    
  elif units>=51 and  units<=100:
    charge=72.5+(units-50)*3.10
    cc=30.00
    duty=units*0.06 
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
elif cat==2:
  if units<100:
    charge=(units*3.40)
    cc=50.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
  elif units>101 and units<=200:
    charge=330+(units-100)*4.80
    cc=50.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
elif cat==3:
  if units<=200:
    charge=(units*5.10)
    cc=60.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
  elif units>=201 and units<=300:
    charge=1000+(units-200)*7.70
    cc=60.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
  elif units>=301 and units<=400:
    charge=1000+720+((units-300)*9.00)
    cc=80.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
  elif units>=401 and units<=800:
    charge=1000+720+850+((units-400)*9.50)
    cc=80.00
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
  elif units>=801:
    charge=1000+720+850+3600+((units-800)*10)
    cc=80
    duty=units*0.06    
    bill= charge+cc+duty
    #print("TOTAL DUE : ",bill)
    


print("Electrical charges : ",charge)
print("Cosumer charges    : ",cc)
print("Electrical Duty    : ",duty)
print("-"*30)
print("-"*30)
print("TOTAL DUE          : ",bill)



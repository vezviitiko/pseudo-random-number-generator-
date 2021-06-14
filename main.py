import time

def random_number(minimum,maximum):
    now = str(time.clock())
    rnd = float(now[::-1][:5:])/100000
    return minimum + rnd*(maximum-minimum)
    
for i in range (1000):
    print(int(random_number(0, 100)))
    

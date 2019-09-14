hr = input("Enter the hours ")
rate = input("Enter the rate per hour ")



try:
    hr = float(hr)
    rate = float(rate)
except Exception as e:
    quit()

def computepay(hr,rate):
    pay = 0.0;
    if hr<=40:
        pay += hr * rate
    else :
        pay += 40 * rate + (hr - 40) * 1.5 * rate

    return pay

p = computepay(hr, rate);
print(p)

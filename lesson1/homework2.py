a = int(input())
m = a//60
hour = m//60
m1 = int(((m%60)*60)/60)
s = a-((hour*3600)+(m1*60))
hs = f"{hour:02}"
print(f"{hour:02}" + ":" + f"{m1:02}" + ":" + f"{s:02}")

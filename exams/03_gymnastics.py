RUS_RIBBON_DIF = 9.100
RUS_RIBBON_EX = 9.400
RUS_HOOP_DIF = 9.300
RUS_HOOP_EX = 9.800
RUS_ROPE_DIF = 9.600
RUS_ROPE_EX = 9.000

BUL_RIBBON_DIF = 9.600
BUL_RIBBON_EX = 9.400
BUL_HOOP_DIF = 9.550
BUL_HOOP_EX = 9.750
BUL_ROPE_DIF = 9.500
BUL_ROPE_EX = 9.400

ITA_RIBBON_DIF = 9.200
ITA_RIBBON_EX = 9.500
ITA_HOOP_DIF = 9.450
ITA_HOOP_EX = 9.350
ITA_ROPE_DIF = 9.700
ITA_ROPE_EX = 9.150

country = str(input())
app = str(input())
score = 0

if country == "Russia":
    if app == "ribbon":
        score = RUS_RIBBON_DIF + RUS_RIBBON_EX
    elif app == "hoop":
        score = RUS_HOOP_DIF + RUS_HOOP_EX
    elif app == "rope":
        score = RUS_ROPE_DIF + RUS_ROPE_EX
elif country == "Bulgaria":
    if app == "ribbon":
        score = BUL_RIBBON_DIF + BUL_RIBBON_EX
    elif app == "hoop":
        score = BUL_HOOP_DIF + BUL_HOOP_EX
    elif app == "rope":
        score = BUL_ROPE_DIF + BUL_ROPE_EX
elif country == "Italy":
    if app == "ribbon":
        score = ITA_RIBBON_DIF + ITA_RIBBON_EX
    elif app == "hoop":
        score = ITA_HOOP_DIF + ITA_HOOP_EX
    elif app == "rope":
        score = ITA_ROPE_DIF + ITA_ROPE_EX

perc = ((20 - score)/20)*100
print(f"The team of {country} get {score:.3f} on {app}.")
print(f"{perc:.2f}%")
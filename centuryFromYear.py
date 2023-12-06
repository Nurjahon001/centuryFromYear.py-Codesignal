def solution(year):
    if year%100==0:
        return year/100
    elif year%100!=0:
        return (year//100)+1

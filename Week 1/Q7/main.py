from  datetime import timedelta, date
start_date=date(1980,11,12)
end_date=date(2008,7,25)
count_wed=0
while start_date<=end_date:
    if start_date.weekday()==2:
        count_wed+=1
    start_date+=timedelta(days=1)
print(count_wed)

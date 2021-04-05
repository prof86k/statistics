
# # li = [
#         67, 72, 72, 51, 64, 61, 68, 57,
#         73, 70, 65, 66, 74, 71, 65, 62, 68,
#         76, 69, 52, 70, 65,66, 75, 71, 74, 75,
#         72, 54, 56, 58, 63, 68, 74, 69,
#         56, 67, 71, 75, 68, 62, 72, 61,
#         65, 64, 72, 56, 65, 74, 64,80,81,89
#     ]

fin = []
def range_sort(lis,_from,by):
    gets = {}

    start = _from
    end = start + by
    results = []
    for i in lis:
        if int(i) >= start and int(i) <= end:
            results.append(i)
            fin.append(i)
    gets[str(start)+"-"+str(end)] = results,len(results)
    return gets
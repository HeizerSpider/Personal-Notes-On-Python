listinlist=([[3.6] ,[1 ,2 ,3] ,[1 ,1 ,1]])

def find_average(list):
    i=0
    k=0
    total_sum=0
    summations=[]
    elements=0
    overall_avg=0
    while i<len(list):
        j=0
        individual_sum=0
        while j<len(list[i]):
            individual_sum+=list[i][j]
            j+=1
            elements+=1
        summations.append(individual_sum/len(list[i]))
        total_sum+=individual_sum
        i+=1
    overall_avg=total_sum/elements
    print(summations, overall_avg)

if __name__=="__main__":
    find_average(listinlist)

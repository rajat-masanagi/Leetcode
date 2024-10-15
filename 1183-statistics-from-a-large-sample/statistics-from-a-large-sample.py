class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        max_freq=0
        min_i=0
        max_i=0
        mode=0
        sums=0
        k=0

        for i in range(len(count)):
            if count[i]!=0:
                min_i=i
                break

        for i in range(len(count)-1,-1,-1):
            if count[i]!=0:
                max_i=i
                break

        for i in range(len(count)):
            if count[i] > max_freq:
                max_freq=count[i]
                mode=i
            sums+=count[i]*i
            k+=count[i]
        mean=sums/k

        cum_freq=0
        if k%2==0:
            median_e1=k//2-1
            median_e2=k//2
            for i in range(len(count)):
                cum_freq+=count[i]
                if median_e1 < cum_freq:
                    m1=i
                    break
            cum_freq=0
            for i in range(len(count)):
                cum_freq+=count[i]
                if median_e2 < cum_freq:
                    m2=i
                    break
            median=(m1+m2)/2

        else:
            median_o=(k+1)//2
            for i in range(len(count)):
                cum_freq+=count[i]
                if median_o <= cum_freq:
                    median=i
                    break

        return [min_i,max_i,mean,median,mode]
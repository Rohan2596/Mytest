def guessno(n):
	start=1
	end=n
	while start <= end:
		mid = int((start + end)/2)
		print("This no :",mid)
		if int(input())==1:
			print("Number found",mid)
			break
        elif int(input("If less than : "))==1:
            end = mid - 1
        elif int(input("If greater than : "))==1:
            start = mid + 1
n=int(input("Enter the number"))
guessno(n)
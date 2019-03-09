def main():
	number = [6,5,4,3]
	number.sort(reverse = True) #Sort Descending
	maks_equationglobal = str(number[0])
	point = 0
	lastsymbol = ""
	for i in range(1,4):
		#Pertambahan
		maks_equationlocal = maks_equationglobal + "+" + str(number[i]) 
		maks_localpoint = eval(maks_equationlocal)
		lastsymbol_local = "+"
		#Pengurangan
		localequation = maks_equationglobal + "-" + str(number[i]) 
		localpoint = eval(localequation) 
		if(abs(localpoint-24) < abs(maks_localpoint-24)):
			maks_localpoint = localpoint
			maks_equationlocal = localequation
			lastsymbol_local = "-"
		#Perkalian
		localequation = maks_equationglobal + "*" + str(number[i]) 
		localpoint = eval(localequation) 
		if(abs(localpoint-24) < abs(maks_localpoint-24)):
			maks_localpoint = localpoint
			maks_equationlocal = localequation
			lastsymbol_local = "*"
		if(lastsymbol == "+" or lastsymbol == "-"):
			localequation = "(" + maks_equationglobal + ")*" + str(number[i]) 
			localpoint = eval(localequation) 
			if(abs(localpoint-24) < abs(maks_localpoint-24)):
				maks_localpoint = localpoint
				maks_equationlocal = localequation
				lastsymbol_local = "*"
		#Pembagian
		localequation = maks_equationglobal + "/" + str(number[i]) 
		localpoint = eval(localequation)

		if(abs(localpoint-24) < abs(maks_localpoint-24)):
			maks_localpoint = localpoint
			maks_equationlocal = localequation
			lastsymbol_local = "/"
		if(lastsymbol == "+" or lastsymbol == "-"):
			localequation = "(" + maks_equationglobal + ")/" + str(number[i]) 
			localpoint = eval(localequation) 
			if(abs(localpoint-24) < abs(maks_localpoint-24)):
				maks_localpoint = localpoint
				maks_equationlocal = localequation
				lastsymbol_local = "/"
		maks_equationglobal = maks_equationlocal
		maks_global = maks_localpoint
		if(lastsymbol_local == "+"):
			point += 5;
		elif(lastsymbol_local == "-"):
			point += 4
		elif(lastsymbol_local == "*"):
			point += 2
		elif(lastsymbol_local == "/"):
			point += 1 
	point -= abs(maks_global - 24) - maks_equationglobal.count("(")
	print(str(point) + " " + str(maks_global) + " " + str(maks_equationglobal))
main()
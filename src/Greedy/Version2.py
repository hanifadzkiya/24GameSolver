def main():
	sums = 0
	cnt = 0
	for a in range(13):
		for b in range(13):
			for c in range(13):
				for d in range(13):
					number = [a+1,b+1,c+1,d+1]
					number.sort(reverse = True) #Sort Descending
					maks_equationglobal = str(number[0])
					lastsymbol = ""
					point = 0
					for i in range(1,4):
						#Perkalian
						maks_equationlocal = maks_equationglobal + "*" + str(number[i]) 
						maks_localpoint = point + 3 - abs(24-eval(maks_equationlocal))
						lastsymbol_local = "*"
						#Pertambahan
						localequation = maks_equationglobal + "+" + str(number[i]) 
						localpoint = point + 5 - abs(24-eval(localequation)) 
						if(localpoint > maks_localpoint):
							maks_localpoint = localpoint
							maks_equationlocal = localequation
							lastsymbol_local = "+"
						#Pengurangan
						localequation = maks_equationglobal + "-" + str(number[i]) 
						localpoint = point + 4 - abs(24-eval(localequation)) 
						if(localpoint > maks_localpoint):
							maks_localpoint = localpoint
							maks_equationlocal = localequation
							lastsymbol_local = "-"
						#Pembagian
						localequation = maks_equationglobal + "/" + str(number[i]) 
						localpoint = point + 2 - abs(24-eval(localequation))
						if(localpoint > maks_localpoint):
							maks_localpoint = localpoint
							maks_equationlocal = localequation
							lastsymbol_local = "/"
						
						maks_equationglobal = maks_equationlocal
						maks_global = maks_localpoint
						#lastsymbol = lastsymbol_local
						#print(point)
					
					sums = sums + maks_global
					cnt = cnt + 1
					print(cnt, " ",maks_equationglobal, " ", maks_global)
	print(sums / cnt)
main()
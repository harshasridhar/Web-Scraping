import requests
from bs4 import BeautifulSoup
import pandas as pd 
url="http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"  #link to the website to be scraped
cols=['Name','15CS51','15CS562','15CS52','15CS553','15CS53','15CS54','15CSL57','15CSL58','SGPA']  #columns in the results file
labs=['15CSL57','15CSL58'] #Subject codes of the Labs
electives=['15CS553','15CS562'] #Subject codes of the electives
def credits(subj,marks):
	if subj in labs:  
		credit=2
	elif subj in electives:
		credit=3
	else :
		credit=4

	if marks>=90 and marks<=100:
		grade=credit*10
	elif marks >=80 and marks<=89:
		grade=credit*9
	elif marks >=70 and marks<=79:
		grade=credit*8
	elif marks >=60 and marks<=69:
		grade=credit*7
	elif marks >=50 and marks<=59:
		grade=credit*6
	elif marks >=40 and marks<=49:
		grade=credit*5
	elif marks >=30 and marks<=39:
		grade=credit*4
	elif marks >=20 and marks<=29:
		grade=credit*3
	elif marks >=10 and marks<=19:
		grade=credit*2
	elif marks >=0 and marks<=9:
		grade=credit*1
	else:
		grade=0
	return grade

usns=[] #specify the USNs for which the results have to be obtained

df=pd.DataFrame(columns=cols,index=usns)

for usn in usns:
	r=requests.post(url=url,data={'sln':usn})
	soup=BeautifulSoup(r.text,'html.parser')

	name=soup.find_all('td')[3].text #Name is present as table data
	name=name.replace(':','')
	
	df['Name'][usn]=name
	if(name.isspace()): #if the USN is invalid
		continue
	
	soup1=soup.find_all("div",class_="divTableCell")
	 #The subject codes along with marks are stored in Table with the cells having div="divTableCell"
	
	if(soup1[6].text not in cols[1:8]): #incase the student does not belong to the semester that is being considered
		continue

	#format: df[subject_code][usn]=marks
	df[soup1[6].text][usn]=soup1[10].text
	df[soup1[12].text][usn]=soup1[16].text
	df[soup1[18].text][usn]=soup1[22].text
	df[soup1[24].text][usn]=soup1[28].text
	df[soup1[30].text][usn]=soup1[34].text
	df[soup1[36].text][usn]=soup1[40].text
	df[soup1[42].text][usn]=soup1[46].text
	df[soup1[48].text][usn]=soup1[52].text
	df['SGPA'][usn]=round((credits(soup1[6].text,int(soup1[10].text))+\
					credits(soup1[12].text,int(soup1[16].text))+\
					credits(soup1[18].text,int(soup1[22].text))+\
					credits(soup1[24].text,int(soup1[28].text))+\
					credits(soup1[30].text,int(soup1[34].text))+\
					credits(soup1[36].text,int(soup1[40].text))+\
					credits(soup1[42].text,int(soup1[46].text))+\
					credits(soup1[48].text,int(soup1[52].text)))/26,2)
	#SGPA is the sum of credits scored divided by the total number of credits and is rounded off to 2 places

df=df.sort_values(by=['SGPA'],ascending=False) #Sort the rows based on the SGPA in descending order

df.to_csv('Final.csv',sep=',') #Store the contents of the data frame as a CSV file with ',' as separator

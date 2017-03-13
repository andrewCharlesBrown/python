# This program breaks up strings composed of email addresses that are part of a database field not in first normal form.
# It then checks against a current list of addresses known to be correct (up to date).
# If an address exists in the database that is no longer relevant (or if it has been misspelled) it is returned and can then be found and deleted more easily. 


def main():
	
	found = False #boolean found becomes true if an email in the table is matched against one that is correct
	lstA = [] #lstA data structure holds the lists created from reading in the file (split method returns a list)
	lstB = [] #lstB data structure holds emails appended from lstA
	lstC = [] #lstC data structure holds the emails known to be correct
	
	f1 = open('emailVariable.txt', "r") #open the suspicious email text doc for reading (some of these addresses may no longer be active)
	f2 = open('emailConstant.txt', "r") #open the email text doc that is correct (should be exported from database/mail server)
	
	for line in f1:
		lstA = line.split(";") #split strings using ';' delimiter
		for j in lstA: # iterate through lstA items
			lstB.append(j.replace("\n", "")) #remove newline characters from string and append to list
	print(lstB)
	
	for line in f2:
		lstC.append(line.replace("\n", ""))
	print(lstC)
	
	for i in lstB:
		found = False
		for j in lstC:
			if i == j:
				found = True
		if found == False: print(i)
		
			
				
if __name__ == "__main__":
	main()
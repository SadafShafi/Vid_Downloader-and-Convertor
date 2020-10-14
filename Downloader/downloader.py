import subprocess as ss

def download(link):
	# print(link)
	ss.call(link,shell=True)
	try:
		download(link)
	except:
		download(link)

print("getting started...............\n\n")

x = open("links.txt","r")
lister = []
for a in x:
	lister.append(a)
# print(lister)
# x = lister
# print(x)for a in lister:
	link = "youtube-dl "+a 
	print("Downloading link : ",link)
	try:
		download(link)
	except:
		download(link)





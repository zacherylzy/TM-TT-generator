from random import randint

alltopics = []
completedtopics = []


#read all the topics, add them to a temporary list
topics = open("/Users/zacherylzy/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Desktop - Macbook Air/NUS/CCAs/Toastmasters/topics.txt", "r")
for line in topics:
    alltopics.append(line.strip())

#read the completed file first
completed = open("/Users/zacherylzy/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Desktop - Macbook Air/NUS/CCAs/Toastmasters/completed.txt", "r")
for lines in completed:
    completedtopics.append(lines.strip())

#write to completed
addcompleted = open("/Users/zacherylzy/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Desktop - Macbook Air/NUS/CCAs/Toastmasters/completed.txt", "a")


for i in range(len(alltopics)):
    i = randint(0, len(alltopics))
    print(i)
    if alltopics[i] not in completedtopics:  #not yet completed/found in completed so break and print the i
        print(alltopics[i])
        addcompleted.write(alltopics[i])
        addcompleted.write("\n")
        addcompleted.close()
        break
    else: #already completed/found in completed, continue loop again
        continue

"""
for i in alltopics:
    if i[-1] != "?":
        print(i)

#add a random factor inside
"""

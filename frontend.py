import streamlit as st
st.title('Toastmasters Table Topics Generator')


from random import randint

alltopics = []
completedtopics = []


#read all the topics, add them to a temporary list
topics = open("topics.txt", "r")
for line in topics:
    alltopics.append(line.strip())

#read the completed file first
completed = open("completed.txt", "r")
for lines in completed:
    completedtopics.append(lines.strip())

#write to completed
addcompleted = open("completed.txt", "a")


for i in range(len(alltopics)):
    i = randint(0, len(alltopics))
    st.write(i)
    if alltopics[i] not in completedtopics:  #not yet completed/found in completed so break and print the i
        st.write(alltopics[i])
        addcompleted.write(alltopics[i])
        addcompleted.write("\n")
        addcompleted.close()
        break
    else: #already completed/found in completed, continue loop again
        continue


#for i in alltopics:
    #if i[-1] != "?":
       # print(i)

#add a random factor inside

#add a random factor inside

print('Welcome to my Computer Quiz')

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Ok! Let's play :)")

score=0
wrong=0

answer = input("what does CPU stand for? ")

if answer.lower() =="central processing unit":
    print('Correct!')
    score+=1
  
else:
     print('Incorrect!')
     wrong+=1

answer = input("what does GPU stand for ? ")

if answer.lower() =="graphic processing unit":
    print('Correct!')
    score+=1
    
else:
    print('Incorrect!')
    wrong+=1
    

answer = input("what does RAM stand for ? ")

if answer.lower() =="random access memory":
   print('Correct!')
    score+=1
else:
    print('Incorrect!')
    wrong+=1

answer = input("what does PSU stand for ? ")

if answer.lower() =="power supply":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    wrong+=1
   

print("Total Correct Answers!", str(score),"/4"," Total Incorrect Answers! "+ str(wrong))


print("You got " + str((score/4)*100) + " %.")

    


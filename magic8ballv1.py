import time
import random

print("Curious about what 2022 holds? Ask the all-knowing, all-seeing, Magic 8 Ball.")
print("Gather your question in your mind. No need to type out your question! Magic 8 Ball only needs you to focus your energy on the quesion you ask. On your mark...get set...ask!")

time.sleep(15)

print("Silence! Your answer is almost ready.")

time.sleep(5)

answerList = ["Probably not going to happen in 2022..." , "2022 is your year, baby!" , "Yes, this will come to pass in 2022." , "Try in 2025 or so..."]

answer = random.choice(answerList)

print(answer)

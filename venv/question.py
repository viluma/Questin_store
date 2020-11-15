#!/usr/bin/python
import random

class Node:

    def __init__(self, id, text, subject, topic, difficulty, marks):
        self.id = id
        self.text = text
        self.subject = subject
        self.topic = topic
        self.difficulty = difficulty
        self.marks = marks
        self.next = None

#Question_store setting the first node of linkedlist to none
class QuestionStore:
    #setting the first question on the linkedlist to none
    def __init__(self):
        self.head = None

    #print_question print all quetions from the question_store
    def print_question(self):
        f = open("f1.txt", "r")
        print(f.read())
        f.close()

     #create_question is a function that creates new question.
    def create_question(self):
        nums = int(input("How many nodes do you want to create: "))
        if nums == 0:
            return
        for i in range(nums):
            f=open('f1.txt','a+')
            id=random.random()
            print(id)
            subject = input('add new question \n Enter the subject')
            print(subject)

            topic = input('Enter the question topic:')
            print(topic)

            text = input('Enter the question text:')
            print(text)

            difficulty = input('how difficult the question is,choose between easy, medium or hard')
            print(difficulty)

            marks = input('Enter the mark:')
            print(marks)
            f.write(marks+'\n')
            questions={"id":(id),"subject":subject, "topic":topic, "text":text,"difficulty":difficulty,"marks":marks}
            f.write(str(questions)+'\n')
            f.close()



#creating question_store object
question_store = QuestionStore()
#creating new question in the question store
question_store.create_question()
#print all the questions inside the question store
question_store.print_question()

#The questions are saved in f1.text file

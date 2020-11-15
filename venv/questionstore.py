
    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while   n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

def update_question(self, x):
        if self.head is None:
            print("List has no elements")
            return
        n = self.head
        while n is not None:
            if n.topic == x:
                n.id = id
                n.text = text
                n.subject = subject
                n.difficulty = difficulty
                n.marks = marks
                n.topic = topic
                print("Question updated")
                return True
            n = n.next
        print("Question not found")
        return False


#creating question_store object
question_store = QuestionStore()
#storing a new question
question_store.create_question()
#printing all question from question_store
question_store.print_question()
#delect a specific question passing the question id into the delete function.
question_store.delete_question("0.9247406593894356")
#updating a specific question
question_store.update_question("9247406593894356")
#printing all the question in the question_store
question_store.print_question()


# Insert append atributes: (text, subject, topic, difficulty, marks)
question_store.append("what is your favourite java framework","java frameworks", "java","hard","100")
question_store.append("what is your favourite python framework","python frameworks", "python","easy","100")
question_store.print_list()
question_store.append("what is your favourite php framework","php frameworks", "php","medium","150")
question_store.all_subjects()

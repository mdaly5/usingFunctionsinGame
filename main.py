# Getting to Know You?
# What do you know about Daniel?

def call_questions(questions, info):
  student_answers = []
  index = 0
  correct_count = 0
  for question in questions:
    answer= input(question)
    if answer.lower().strip() == info[index]:
      correct_count +=1
    index +=1
  student_answers.append(answer)
  return correct_count

daniel_info = ['confluence academy', 'lagos', '7']
daniel_questions = ['What school does Daniel teach at? ', 'In what city was Daniel born? ', 'How many years has Daniel been a teacher? (Use number keys) ']

mike_info = ['university city', 'kansas city', '16']
mike_questions = ['In what city does Mike teach? ', 'In what city was Mike born? ', 'How many years has Mike been a teacher? (Use number keys)']


def determine_avg(questions, info):
  percent = 0
  num_correct = call_questions(daniel_questions, daniel_info)
  percent= (f'You got {(num_correct/len(questions))*100}% of the questions correct.')
  return percent
print(determine_avg(daniel_questions, daniel_info))

# print(call_questions(daniel_questions, daniel_info))
# print(call_questions(mike_questions, mike_info))



#Loop through questions about Daniel. Create a list of student answers



  

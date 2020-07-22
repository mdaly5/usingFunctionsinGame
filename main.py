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
our_questions = [daniel_questions, mike_questions]
our_info = [daniel_info, mike_info]

def determine_avg(questions, info):
  percent_list = []
  for index in range(len(questions)):
    num_correct = call_questions(questions[index], info[index])
    percent_list.append((num_correct/len(questions[index]))*100)
  return percent_list

# def results(a_list):
#   statement = 'You got {a_list[0]}% of the questions correct about Daniel and {a_list[1]}% of the questions correct about Michael.'
#   return statement

final = determine_avg(our_questions, our_info)

def main(num1, num2):
  if final[0] > final[1]:
    statement = (f'You got {num1}% of the questions about Daniel correct and {num2}% of the questions about Michael correct. You know Daniel better than Michael.')
    return statement
  elif final[0] < final[1]:
    statement = (f'You got {num1}% of the questions about Daniel correct and {num2}% of the questions about Michael correct. You know Michael better than Daniel.')
    return statement
  else:
    statement = (f'You got {num1}% of the questions about Daniel correct and {num2}% of the questions about Michael correct. You know Daniel and Michael equally well.')
    return statement

print(main(final[0], final[1]))
print('hello')




  

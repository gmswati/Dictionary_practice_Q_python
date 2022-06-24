question_list = {
1:"How many continents are there?",     # pehla question
2:"What is the capital of India?",  # doosra question
3:"NG mei kaun se course padhaya jaata hai?" # teesra question
}

options_list = {
 #pehle question ke liye options
 1:{1:"Four", 2:"Nine", 3:"Seven", 4:"Eight"},
 #second question ke liye options
 2:{1:"Chandigarh", 2:"Bhopal", 3:"Chennai", 4:"Delhi"},
 #third question ke liye options
 3:{1:"Software Engineering", 2:"Counseling", 3:"Tourism", 4:"Agriculture"}
}
# solution_list=[3,4,1]

# for question in question_list:
#     print(question,'.', question_list[question])
#     for option in options_list:
#         print(option,'.',options_list[option])
Question_no=['First','Second','Third']
i=1
Total_ques=len(question_list)
# global answed_correctly
# why I can't able to make it global here?
answed_correctly=0
count_Life_line=0
while i<4:
    print('your',Question_no[i-1],'question is :')
    print(i,'.',question_list[i])
    j=1
    while j<=4:
        print(j,'.',options_list[i][j])
        # break
        j+=1
    # i+=1


    def lifeline():
        Lifeline_5050=input("do you want to take lifeline.write 'yes' or 'no': ")
        if Lifeline_5050=='yes':
            global count_Life_line
            global answed_correctly
            if count_Life_line==0:
                count_Life_line+=1
                Ll_options_list=[['seven','eight'],['delhi','chennai'],['software engineering','counseling']]
                j=1
                while j<=2:
                    print(j,'.',end='')
                    print(Ll_options_list[i-1][j-1])
                    j+=1
                answer=int(input('enter your answer in option no.'))
                solution_list=[1,1,1]
                if solution_list[i-1]==answer:
                    # c+=1
                    answed_correctly+=1
                    print('absolutely right')
                    print('A big clap for you')

                else:
                    print('wrong answer')
                    print('sorry!,you are out of the game')
                    # break
            else:
                print("sorry! you do'nt have lifeline left.")
                lifeline()

        else:
            print('Great!')
            answer=int(input('enter your answer in option no.'))
            solution_list=[3,4,1]
            if solution_list[i-1]==answer:
                # c+=1
                answed_correctly+=1
                print('absolutely right')
                print('A big clap for you')
            else:
                print('wrong answer')
                print('sorry!,you are out of the game')
                # break       
    lifeline()

    i+=1

if answed_correctly==Total_ques:
    print('Played fantastic!,Keep it up...')
else:
    print('played well, but needed little more practice...')

    
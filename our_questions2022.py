import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import csv

question_list = [{
    'number': 1,
    'is_last': False,
    'question': 'Is transport of stuff in Ghana a problem?: ',
    
    'A': 'Definitely',
    'B': 'Probably',
    'C': 'Maybe',
    'D': 'Not Really'

},

    {'number': 2,
    'is_last': False,
    'question' : 'How often do you transfer parcels or packages?',
    'A' : 'Very often',
    'B' : 'Often',
    'C' : 'Rarely often',
    'D' : 'Never'
},

    {'number': 3,
    'is_last': False,
    'question': 'What means of transport of your stuff do you prefer?',
    'A': 'IAS Ghana Limited',
    'B': 'OAk Express Limited',
    'C': 'DHl Express',
    'D': 'STC bus'
    
    
},
    {'number': 4,
    'is_last': False,
    'question': 'How time efficient is transport of cargo for you?: ',
    'A': 'Almost Instantly',
    'B': 'Very Quick',
    'C': 'Relatively Slow',
    'D': 'Very Delayed and Inconsistent'
    
},
    {'number': 5,
    'is_last' : False,
    'question' : 'How convenient or inconvenient is it for you when transporting your stuff?',
    'A' : 'Very convenient',
    'B' : 'Convenient enough',
    'C' : 'Somewhat inconvenient',
    'D' : 'Pretty inconvenient'
},

    {'number': 6,
    'is_last': True,
    'question': 'Would you prefer a step forward technologically advanced means of transporting your stuff?',
    'A': 'Very much',
    'B': 'Somehow',
    'C': 'Maybe',
    'D': 'Not Sure'
    
    
},
    
   

    ]
    
responses_list = []


def save_results_to_text(responder_name, selections_dict):
    output_file_name = f"output_{responder_name}_.txt"

    with open(output_file_name, 'w') as output_file:
        output_file.write("Que,Ans,Descr,Responder\n")
        for key in selections_dict:
            que_number = int(key)
            ans = selections_dict[key][1]
            ans, descr = ans.split(".")

            output_file.write(
                f"{que_number}, {ans}, {descr}, {responder_name}\n"
    
        )
    #just inserted    
#    name = ['A', 'B', 'C', 'D']
 #   score = [23, 23, 34, 45]
  #  position = [0, 1, 2, 3]

#    plt.bar(position, score, width=0.5, color= 'gold')
 #   plt.title('Question 1')
  #  plt.xticks(position, name)

   # plt.show()







# DA - this function should end here
# DA - now create a function that reads all the files that are saved'''

    df = pd.read_csv(output_file_name, sep=",")
    print(df)

    # merge multiple dataframes
    #output_files = []
    

    output_files = ["output_Bernard Govina_.txt"]
    df_list = output_files
    for file_name in output_files:
        df = pd.read_csv(file_name)
        df_list.append(df)

    df_all = pd.concat(df_list, axis=0)
    print("df_all: ")
    print(df_all)


#def put_responses_in_list():
 #   responses_list.append(f"output_{responder_name}.txt")

# all_responses
#with open('output_files.csv', 'w', newline='') as f:
    


'''   def combine_responses():
    
        output_files = []

        output_files = ["output_Bernard Govina_.txt", "output_Biney Daniel_.txt", "output_Akpalu Emmanuel_.txt", "output_William Kabu_.txt","output_Abatey David Alegre_.txt", "output_Adika Harold_.txt","output_Aduhene Kingsley_.txt",""]
        df_list = []
        for file_name in output_files:
            df = pd.read_csv(file_name)
            df_list.append(df)
'''
    
#    grouping data
#def get_results_by_question(df, question_number):
#    question_subset = df.query(f"Que=={question_number}")
#    group_by_responses = question_list.groupby("Ans")
#    response_counts: pd.DataFrame = group_by_responses.count()["Que"]
#    response_counts.plot(
#        kind="bar",
#        title=f"Question {ques_num}",
#        xlabel="Choice",
#        ylabel="Count"
#    )
#    plt.show()

'''
    if __name__ == '__main__':
        # enter the file names here
        output_files = []
        df_list = []
        for file_name in output_files:
            df = pd.read_csv(file_name)
            df_list.append(df)
'''
 

if __name__ == '__main__':
    st.header("Green Phantom Innovation Project Questionnaire")

    #selections = []
    selections_dict = {}  # key = question_num, value = []
    for question_dict in question_list:
        st.write(
            f"{question_dict['number']}. {question_dict['question']}")

        # ans_list = [". No Answer Selected "] DA: lets use variables to avoid confusion.
        default_answer = ". No Answer Selected" #DA: (*)
        ans_list = [default_answer]
        for option in ["A", "B", "C", "D"]:
            ans_list.append(f"{option}. {question_dict[option]}")
        choice = st.radio(f"Make a selection below", ans_list)
        # selections.append(choice)
        selections_dict[question_dict['number']] = [
            question_dict['question'], choice]

    st.write("Below is a summary of your answers:")

    # selections
    selections_dict
    # DA: we need to initialize this to false before each check. Else, if wrong_ans is set to True, there is no way for it to be reset to False.
    wrong_ans = False
    for que_num in selections_dict:
      # if que_num in selections_dict[que_num[1]] == ". No Answer Selected ": DA- error here. see below

      # DA using a variable to avoid problem of different spaces between different occurences
        if selections_dict[que_num][1] == default_answer: # See (*) above
            print(
                f"Checking question {que_num} {selections_dict[que_num][1]} == {default_answer}")
            wrong_ans = True

    responder_name = ""
    with st.form(key='my_form'):

        responder_name = st.text_input("Please enter your name:")
        submit_button = st.form_submit_button(
            label='Submit Questionnaire'
        )
    if submit_button:
        try:
            no_name = responder_name == ""
            if no_name or wrong_ans:
                # DA added so we see the state of these checks
                print(f"no_name {no_name}: wrong_ans {wrong_ans}")
                raise Exception("Oops you should enter your name")
        except Exception as ex:
            st.error(
                "Please enter a name before submitting or check that you have only valid answers")

        else:
            save_results_to_text(responder_name, selections_dict)
           # combine_responses()


name = ['A', 'B', 'C', 'D']
score1A = ()
score1B = ()
score1C = ()
score1D = ()

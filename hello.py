import streamlit as st 
st.title("Accuracy in MCQ's based Exams")
sec = st.number_input("Enter total no. of sections:",min_value=1)
steps = 1
total_mrks,secured_mrks = 0,0 
while(steps<=sec):
    s_qns = st.number_input(f'Enter total qns in section-{steps}',min_value=1)
    qns_ans = st.number_input(f"Enter qns answered in section-{steps}:",min_value=0)
    crt_ans = st.number_input(f"Enter correctly answered questions in section-{steps}:",min_value=0)
    m = st.number_input(f"Enter marking scheme per question for crt ans in section-{steps}",min_value=0)
    st.subheader(f'Expected Marks of Section-{steps}')
    a=crt_ans*m 
    st.write(a)
    marks=0
    status = st.radio(f"Negative marking per qn in section-{steps}:",("yes","no"))
    if(status=="yes"):
        neg_marks = st.number_input(f"Enter negative marks per qn in section-{steps}",min_value=0.0)
        marks = a - (qns_ans-crt_ans)*neg_marks
    else:
        marks=a

    st.subheader(f'Section-{steps} marks:')
    st.write(marks)
    st.subheader(f'Section-{steps} Accuracy')
    if qns_ans>0:
       acc = round(marks/(s_qns*m)*100,2)
    else:
      acc=0
    st.write(acc)
    
    total_mrks+=s_qns*m
    secured_mrks+=marks 
    steps+=1
st.subheader('Total marks Obtained:')
st.write(secured_mrks)
if total_mrks>0:
    acc = round((secured_mrks/total_mrks)*100,2)
else:
    acc=0
st.subheader('Total accuracy Obtained')
st.write(acc)

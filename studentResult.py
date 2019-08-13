exam1=float( input("Enter 1st examination score out of 100:") )
exam2=float( input("Enter 2nd examination score out of 100:") )
sports1=float(input( "Enter score of sports activity out of 50:" ))
activity1=float( input("Enter singing score out of 20:") )
activity2=float( input("Enter Dancing score out of 20:") )
activity3=float( input("Enter painting score out of 20:") )
exam_score_obtained=exam1+exam2
total_exam_score=200
total_sports_score=50
total_activities_score=60
obtained_activity_score=activity1+activity2+activity3

obtained_exam_percentage=(exam_score_obtained/total_exam_score)* 50

obtained_activities_percentage=( obtained_activity_score/60)*30

obtained_sports_percentage=( sports1/50 )*20

print(" total percentage obtained is : ", obtained_exam_percentage+obtained_activities_percentage+obtained_sports_percentage )

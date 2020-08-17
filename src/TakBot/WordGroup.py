
class WordGroup:

    Category_Greeting_Generic =  ['Hello','Greetings', 'Heya','Halo','Hi','Hi there','Sup']
    Category_Greeting_Morning = ['Rise and shine','Morning']
    Category_Greeting_Afternoon= ['Afternoon','Lunch time hello']
    Category_Greeting_Evening = ['Evening','Hi night owl']

    Category_Greeting_All = []
    Category_Greeting_All.extend(Category_Greeting_Generic)
    Category_Greeting_All.extend(Category_Greeting_Morning)
    Category_Greeting_All.extend(Category_Greeting_Afternoon)
    Category_Greeting_All.extend(Category_Greeting_Evening)


    Category_Question = ['who','what','when','why','how']
    Category_Weather = ['weather','rain','clear','cold','hot']
    Category_Location = ['inside','outside','indoor','outdoor']

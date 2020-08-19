
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

    Category_Accept = ['yes','y','confirm','consent','agress']


    Category_Question = ['who','what','when','why','how','check']
    Category_Weather = ['weather','rain','clear','cold','hot']
    Category_Location = ['inside','outside','indoor','outdoor']
    Category_Travel = ['go to', 'visit','']
    Category_Place = ['museum','cafe','shop' ,'store','cinema','arcade','shop','market','restaurant' , ' bar ','club']


    Category_Action  = ["send"]
    Category_Retrieve = ['get','find','search','obtain','take']
    Category_Delivery  = ['send', 'deliver','drop','dispatch','post','bring','pass','give']
    Category_Medium = ["email","mail"]

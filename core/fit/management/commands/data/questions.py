try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

text = StringIO("""Id|Sequence|QuestionContent|IsReversed|IsActive|IsCorp|DimensionId|CategoryId|Weight|QuestionTypeId
2|2|When learning new things I take a lot of notes.|0|1|0|1|1|1|1
3|3|When learning something new, I use specific strategies to monitor the accuracy of my knowledge.|0|1|0|1|1|1|1
4|4|I use memory strategies to help me remember things I need to do.|0|1|0|1|1|1|1
5|5|I misplace things daily.|1|1|0|1|1|1|1
6|6|I am good at remembering names of people I meet.|0|1|0|1|1|1|1
7|7|After being interrupted, I have a hard time remembering what I was doing previously.|1|1|0|1|1|1|1
201|121|You need to lose 20 or more pounds.|1|1|0|3|32|0|1
9|8|I do not seek out mentally challenging situations.|1|1|0|1|2|1|1
202|122|You have poor posture.|1|1|0|3|32|0|1
11|9|I am drawn to tasks that require problem solving.|0|1|0|1|2|1|1
13|10|It is important for me to be mentally challenged everyday.|0|1|0|1|2|1|1
203|123|You are overweight.|1|1|0|3|32|0|1
15|11|I enjoy working on mentally challenging tasks for long hours.|0|1|0|1|2|1|1
16|12|I procrastinate things that I do not want to deal with.|1|1|0|1|3|1|1
18|13|I avoid doing things that are difficult.|1|1|0|1|3|1|1
19|14|I tend to get things done ahead of deadlines.|0|1|0|1|3|1|1
20|15|I deal with a difficult situation by tackling it right away.|0|1|0|1|3|1|1
21|16|I am disciplined in my choices to avoid temptations.|0|1|0|1|3|1|1
22|17|I buy things spontaneously and regret the purchase later.|1|1|0|1|3|1|1
23|18|I am easily distracted when reading.|1|1|0|1|4|1|1
24|19|In a large social setting I have a difficult time focusing on one conversation.|1|1|0|1|4|1|1
25|20|There are often times when I lose focus during a conversation with a co-worker or significant other.|1|1|0|1|4|1|1
26|21|I can stay focused on a task for hours at a time.|0|1|0|1|4|1|1
27|22|When working to meet a deadline, I stay focused until it is accomplished.|0|1|0|1|4|1|1
28|23|When I am interrupted, I can easily shift my attention back to what I was doing before.|0|1|0|1|4|1|1
29|24|I feel my days are spent doing things I have to do each day, rather than things I want to do each day.|1|1|0|1|5|1|1
30|25|I have freedom to choose what I do each day.|0|1|0|1|5|1|1
31|26|I have a clear sense of purpose that drives my daily decisions.|0|1|0|1|5|1|1
32|27|I am good at understanding sarcasm.|0|1|0|1|6|1|1
33|28|I have been known to offend people by making a social faux pas (i.e., an insensitive remark or error in social etiquette).|1|1|0|1|6|1|1
204|124|You sleep soundly.|0|1|0|3|33|0|1
205|125|The room you sleep in is designated solely to sleeping.|0|1|0|3|33|0|1
206|126|On average, you sleep 7-8 hours per night.|0|1|0|3|33|0|1
207|127|You should get more sleep.|1|1|0|3|33|0|1
39|29|I am good at detecting when people are lying.|0|1|0|1|6|1|1
45|30|Even when I do not agree with someone's point of view, I try to understand his or her perspective.|0|1|0|1|6|1|1
46|31|I do not appreciate hearing other people's opinions when they are different from mine.|0|1|0|1|6|1|1
47|32|I actively seek out feedback from other people regarding areas I can improve.|0|1|0|1|6|1|1
48|33|I would care if the stock market crashed?|0|1|0|4|18|1|0
49|34|What is the ratio of the total mortgage left on your home to your household annual after tax salary?|1|1|0|4|18|1|5
50|35|I am confident with my retirement plan?|0|1|0|4|18|1|0
51|36|I am knowledgeable on the differences and similarities between stocks, bonds, mutual funds, and ETFs.|0|1|0|4|18|1|0
52|37|I feel prepared for the cost of a family.|0|1|0|4|18|1|0
53|38|I feel financially secure about my future.|0|1|0|4|18|2|0
54|39|I am concerned about my credit card debt?|1|1|0|4|19|1|0
55|40|I do not regret expenditures in the past three months.|1|1|0|4|19|1|0
56|41|I would feel nervous if myself or someone in my household lost their job?|1|1|0|4|19|2|0
57|42|I owe money to three or more creditors.|1|1|0|4|19|1|0
58|43|I have a monthly budget.|0|1|0|4|19|1|0
59|44|I am successful at not spending more than my monthly budget.|0|1|0|4|19|1|0
60|45|Are you confident in the amount of life insurance you have?|0|1|0|4|20|1|1
61|46|Do you feel paying bills is overwhelming?|1|1|0|4|20|1|1
62|47|Do you feel you spend too much money on dining out?|1|1|0|4|20|1|1
210|170|I enjoy working out with a friend.|0|1|0|3|34|0|1
211|171|Discussing my physical health with another person feels good.|0|1|0|3|34|0|1
212|172|It's better to figure out my exercise routine alone.|1|1|0|3|34|0|1
213|173|I am part of a fitness group or team, which meets at least three times a month.|0|1|0|3|34|0|1
71|48|Do you feel that your current wealth is holding you back from doing what you want?|1|1|0|4|20|2|1
72|49|If you made more money, would you be happier or less worried?|0|1|0|4|20|1|3
73|50|Are you concerned about your short-term financial future?|1|1|0|4|20|3|1
74|51|Do you care about your work/job?|0|1|0|4|21|1|0
75|52|Do you feel that you save enough of your (or household) take home pay?|0|1|0|4|21|1|1
76|53|How much of your discretionary budget is dedicated to healthy activities?|0|1|0|4|21|1|2
77|54|Do you feel you have gotten paid for your contributions at work and do you feel as though you are being adequately compensated for your work, given your talent, education, and drive?|0|1|0|4|21|2|0
78|55|Are you in a better place financially than you were 3 years ago?|0|1|0|4|21|1|1
79|56|Do financial concerns ever cause you to have trouble sleeping?|1|1|0|4|22|1|1
80|57|Over the past three months, how many days have financial concerns caused restless nights?|1|1|0|4|22|1|1
81|58|My partner and I agree on financial decisions.|0|1|0|4|22|1|7
82|59|My partner is fully aware of my financial situation.|0|1|0|4|22|1|7
83|60|If you have financial concerns, are there people you can turn to for help?|0|1|0|4|22|1|1
84|61|Do you ever feel awkward engaging with people that have more money than you?|1|1|0|4|22|1|1
85|62|Do you ever feel awkward engaging with people that have less money than you?|1|1|0|4|22|1|1
86|63|I am generally sad when I wake up in the morning.|1|1|0|2|7|0|1
87|64|I am generally not afraid of much.|0|1|0|2|7|0|1
88|65|I have a fear of losing control.|1|1|0|2|7|0|1
89|66|I rarely worry about my health.|0|1|0|2|7|0|1
90|67|I am on medication to help me with my mood or with my sleep.|1|1|0|2|7|0|1
91|68|There are things I do to forgive myself if I have made a mistake.|0|1|0|2|8|0|1
92|69|When I think about my flaws as a person, it makes me feel more cut off from others.|1|1|0|2|8|0|1
93|70|When things get difficult I am really hard on myself.|1|1|0|2|8|0|1
94|71|When I'm having challenges in my life, I realize that I'm not alone and that others have difficult.|0|1|0|2|8|0|0
95|72|One of the things which interest me is to understand and manage my strengths and weakness.|0|1|0|2|8|0|1
96|73|Sitting quietly with my thoughts and feelings is not that important to me|1|1|0|2|8|0|1
97|74|Sometimes I react and I don't know why I'm reacting that way|1|1|0|2|8|0|1
98|75|I can deal with my anger, fear, or worry, if I am am in pursuit of a goal.|0|1|0|2|8|0|1
99|76|When something bad happens to me, it bothers me, but I can usually shake it off quite easily.|0|1|0|2|9|0|1
100|77|Setbacks don't discourage me|0|1|0|2|9|0|1
101|78|I heard that I was really loved and cared for when I was a young child.|0|1|0|2|9|0|1
102|79|I usually find myself feeling overwhelmed.|1|1|0|2|9|0|1
103|80|I have something I can do to calm myself if I am really upset.|0|1|0|2|9|0|1
104|81|My family and friends don't have much to do with my success|1|1|0|2|10|0|1
105|82|If I made a list of everything I felt grateful for, it would be a long list.|0|1|0|2|10|0|1
106|83|I do something each day to remind me of what makes me so fortunate|0|1|0|2|10|0|1
107|84|I struggle to be optimistic.|1|1|0|2|10|0|1
108|85|I have an easy time seeing the positive in situations.|0|1|0|2|10|0|1
109|86|My tendency is to really persist with a difficult task.|0|1|0|2|10|0|1
110|87|My spiritual beliefs help me deal with difficult situations.|0|1|0|2|11|0|1
111|88|There is a power bigger than me in this world which I feel connected to.|0|1|0|2|11|0|1
112|89|Sitting quietly to meditate or pray is not part of my daily or weekly routine.|1|1|0|2|11|0|1
113|90|I think about the meaning and purpose of my life.|0|1|0|2|11|0|1
114|91|I feel relieved after sharing my worries with a friend.|0|1|0|2|12|0|1
115|92|There is someone I can turn to if I'm having problems with my family or at work|0|1|0|2|12|0|1
116|93|One of my goals is to understand other people's behaviors and intentions|0|1|0|2|12|0|1
117|94|My friends or colleagues will come to me if they need help with a difficult social situation.|0|1|0|2|12|0|1
120|97|You consume seven or more servings of vegetables each day.|0|1|0|3|13|0|1
121|98|You drink eight or more eight-ounce glasses of water per day.|0|1|0|3|13|0|1
122|99|You eat four or more times per day.|0|1|0|3|13|0|1
123|100|You ingest a wide variety of fruits and vegetables of various colors.|0|1|0|3|13|0|1
124|101|You consume more sugar than you should.|1|1|0|3|13|0|1
125|102|You know how many servings of fruits and vegetables you should consume per day.|0|1|0|3|14|0|1
126|103|You know how to eat a healthy and balanced diet.|0|1|0|3|14|0|1
127|104|You know how many calories you should eat per day to achieve or maintain your ideal weight.|0|1|0|3|14|0|1
128|105|You know how many grams or teaspoons of sugar you consume per day.|0|1|0|3|14|0|1
129|106|You have a good understanding of current concepts in nutrition.|0|1|0|3|14|0|1
130|107|You frequently get up throughout the day to walk around or perform chores.|0|1|0|3|15|0|1
131|108|You become short of breath when climbing multiple flights of stairs.|1|1|0|3|15|0|1
132|109|How many hours per day do you watch television?|0|1|0|3|15|0|8
133|110|You often sit three hours or more at a time without getting up to move around.|1|1|0|3|15|0|1
134|111|You spend a total of ten or more hours seated per day.|1|1|0|3|15|0|1
135|112|You engage in 150 minutes per week of moderate aerobic activity or 75 min per week in vigorous aerobic activity.|0|1|0|3|16|0|1
136|113|You know what types of aerobic activity will most benefit you.|0|1|0|3|16|0|1
137|114|You are satisfied with your current level of aerobic fitness/activity.|0|1|0|3|16|0|1
138|115|Aerobic exercise is an important component of your physical fitness.|0|1|0|3|16|0|1
139|116|You consistently strength train two days per week.|0|1|0|3|17|0|1
140|117|You know how to organize your strength training in a way that best meets your needs.|0|1|0|3|17|0|1
141|118|You should strength train more often.|1|1|0|3|17|0|1
142|119|You have more body pain than you should.|1|1|0|3|17|0|1
143|120|You like the way you look.|0|1|0|3|32|0|1
144|0|Does the employees seem more productive?|0|NULL|1|NULL|NULL|0|1
145|0|Are there less sick days?|0|NULL|1|NULL|NULL|0|1
146|0|How many sick days were taken last month?|0|NULL|1|NULL|NULL|0|1
147|0|Do the employees seem happier?|0|NULL|1|NULL|NULL|0|1
148|0|Is the company more profitable?|0|NULL|1|NULL|NULL|0|1
149|0|How aligned are your personal values aligned with the stated values of your employer?|0|NULL|1|NULL|NULL|0|1
150|0|How aligned are the company vales as exhibited in the behavior of the company?|0|NULL|1|NULL|NULL|0|1
151|0|How aligned are you with the culture of your current employer?|0|NULL|1|NULL|NULL|0|1
152|0|How aligned are you with the reason the company you work for exists (aka Their Purpose statement)?|0|NULL|1|NULL|NULL|0|1
153|0|I believe in what we, why we do it, and how we do it?|0|NULL|1|NULL|NULL|0|1
154|0|How supportive is your employer with your personal development?|0|NULL|1|NULL|NULL|0|1
155|9999|How supportive is the <strong>company</strong> with your professional development?|1|1|1|NULL|9|1|1
156|0|To what extent are your work contributions appreciated?|0|NULL|1|NULL|NULL|0|1
157|0|To what extent does your company help you develop and execute your personal strategic plan?|0|NULL|1|NULL|NULL|0|1
158|0|Do you feel proud to tell people where you work?|0|NULL|1|NULL|NULL|0|1
159|0|My employer cares about my needs?|0|NULL|1|NULL|NULL|0|1
160|0|Do you have the tools to enable you to do your job effectively?|0|NULL|1|NULL|NULL|0|1
161|0|Do you have the opportunity to contribute to decisions that affect you?|0|NULL|1|NULL|NULL|0|1
162|0|Do you understand how your role contributes to achieving business outcomes?|0|NULL|1|NULL|NULL|0|1
163|0|Do you feel valued for the work you do?|0|NULL|1|NULL|NULL|0|1
164|0|Are you skills, needs, and passions being fulfilled and maximized?|0|NULL|1|NULL|NULL|0|1
165|142|I understand how my role contributes to achieving business outcomes.|0|NULL|1|NULL|NULL|0|1
166|143|Did the company mission statement and environment matter in your choice to work there?|0|NULL|1|NULL|NULL|0|1
167|144|Does the company promote a healthy lifestyle|0|NULL|1|NULL|NULL|0|1
168|145|If the company left Boulder would you go with the company|0|NULL|1|NULL|NULL|0|1
169|146|Does it matter to you that you live in Boulder area|0|NULL|1|NULL|NULL|0|1
170|147|Does it matter to you that you live in Colorado|0|NULL|1|NULL|NULL|0|1
171|148|The environment in which I work is healthy and positive?|0|NULL|1|NULL|NULL|0|1
172|149|Would you consider yourself an active person|0|NULL|1|NULL|NULL|0|1
173|150|Do you swim at least once a week (Plug in miles)|0|NULL|1|NULL|NULL|0|1
174|151|Do you ride your bike at least once a week (Plug in miles)|0|NULL|1|NULL|NULL|0|1
175|152|Do you run a least once a week (Plug in miles)|0|NULL|1|NULL|NULL|0|1
176|153|Do you do anything other than drive to work|0|NULL|1|NULL|NULL|0|1
177|154|Do you go to the gym/yoga/Pilates at least once a week|0|NULL|1|NULL|NULL|0|1
178|155|How many days did you bike/run to work this month (Plug in miles)|0|NULL|1|NULL|NULL|0|1
179|156|Have you ever done a triathlon|0|NULL|1|NULL|NULL|0|1
180|157|Have you ever done a 5k?|0|NULL|1|NULL|NULL|0|1
181|158|Do you feel your activity level is improving?|0|NULL|1|NULL|NULL|0|1
182|159|Do you feel more productive?|0|NULL|1|NULL|NULL|0|1
183|160|Do other employees seem to care about being physically active?|0|NULL|1|NULL|NULL|0|1
209|1|I break learning new things into small steps.|0|1|0|1|1|1|1""")

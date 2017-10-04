try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

text = StringIO("""Id|GoalId|TaskString
1|1|View content related to nutrition in the FIT library
2|1|View content related to aerobic fitness in the FIT library
3|1|View content related to strength training in the FIT library
4|1|View content related to a short-term finance topic in the FIT library
5|1|View content related to a term-term finance topic in the FIT library
6|2|Start going to bed 30 minutes earlier than your normal bedtime
7|2|Take a 20-45 minute afternoon nap
8|2|Eat 4-5 servings of dark greens
9|2|Eat fresh fish 2 times this week
10|2|Keep a memory notebook that helps you remember your to-do-list
11|2|Make a list at the beginning of each day of what you need to accomplish that day
12|2|Use humor when trying to remember something
13|2|Use coconut or avocado oil to cook with 
14|2|Remove distractions from your environment (e.g. work, home)
15|2|Stay nourished: have a low-carb snack or meal every 3-4 hours
16|2|Practice shifting attention away from temptations
17|2|When you meet someone new, pause and repeat the person's name back to them 
18|2|When you meet someone new, come up with a visual image for the person
19|2|When you meet someone new, link a feature of the person with someone you already know
20|2|Keep your grocery list in a memory notebook
21|2|Organize your shopping list based upon where items are located in the store
22|3|Sit in direct sunlight first thing in the morning for 10 minutes
23|3|Turn off all electronics 2 hours before bedtime
24|3|Do not consume caffeine after 2 PM 
25|3|Take a 20-45 minute nap in the afternoon
26|3|Use your willpower to help improve your sleep habits
27|3|Write down your worries before going to sleep
28|3|Try to go to sleep at the same time each night
29|4|Read blog about learning styles myth
30|4|Engage in a hands-on learning activity
31|4|Pick something new you want to learn and use visual, auditory, & hands-on activies
32|5|Create an action plan for attaining your goals (including monitoring & evaluating your goals)
33|5|Write down 3 characteristics about self-disciplined people you know
34|5|Spend at least 5 minutes telling someone else your goals & how you are going to accomplish them
35|5|Journal daily about how you are going to accomplish a goal
36|5|Journal about what distracts you from making progress towards your goals 
37|5|Write down 3 ways you can be more effective in regulating your emotions
38|5|Repeat this mantra when tempted, "Willpower is my desire."
39|5|When tempted, smile; then think about your strong self control 
40|5|Start to recognize your obstacles to reaching your goals 
41|6|Read about neuroplasticity 
42|6|Discuss an abstract topic like space, time, or social justice with a friend
43|6|Read a book of your choice
44|6|Read about a subject you are interested in but know very little about
45|6|When traveling to a new destination use a map instead of your GPS
46|6|Practice laughing everyday
47|6|Work on improving your sense of humor 
48|6|Try a new activity
49|6|Learn and use a new vocabulary word this week 
50|6|Improve engagement during a conversation create a picture of what the person is saying
51|6|Become more focused & take notes during meetings or when on the phone 
52|7|Visualize full engagement at work for 2 minutes each morning
53|7|Only work on one task at a time until it is complete
54|7|Remove distractions by cleaning desk
55|7|Reorganize part of your office
56|7|During a conversation ask follow-up questions
57|7|Repeat back what you heard from a cowoker or boss in your own words
58|7|Teach something you learned this week to someone else
59|7|Take regular 5 to 10 minutes breaks at work
60|8|Prior to working out visualize perfect performace in your sport or hobby
61|8|Focus on mindfulness during the sport or exercise activity
62|8|Break a goal into small steps
63|8|Tell someone about your fitness goals
64|8|Keep a journal of your fitness progress
65|9|Only work on one task at a time until it is complete
66|9|Remove distractions by cleaning out one space in your home
67|9|Focus on mindful attention during tasks (i.e., pay attention to mind wandering or distractions)
68|9|Use active listening at home (i.e., listening carefully without interrupting)
69|9|During a conversation, ask follow-up questions
70|9|Pay attention to your breath and be fully present withyour morning routine at home
71|9|Remove things from your house that you no longer feel connected to
72|10|Go to bed 30 minutes earlier
73|10|Make sure you are getting 7-8 hours of sleep per night
74|10|Take a 20-45 minute nap afternoon
75|10|Engage in 5 to 20 minutes of mindfulness meditation everyday
76|10|Work on present moment awareness throughout the day
77|10|Engage in 20 minutes of exercise everyday
78|10|Build your willpower muscle by eliminate 1 high-sugar food from diet 
79|10|At night write down your successes from the day
80|10|Write down 3 things you can control during the day
81|10|Reflect upon 1 thing you could have done better and have compassion for yourself 
82|11|Read about coping skills
83|11|Create an action focus plan to solve a problem in your life
84|11|Read about how your body reacts to stress
85|11|Seek out social support from trusted friend
86|11|Weave moments of present moment awareness throughout the day
87|11|Engage in 20 minutes of exercise everyday to reduce stress
88|11|When you feel stressed, think about how the stessor is might be making you stronger in some way
89|11|Talk to a friend about a specific stressor in your life
90|12|Read about optimism & think about your best possible self
91|12|Journal about a quality in your self that you admire
92|12|Create one goal and spend 2 minutes a day visualizing reaching that goal
93|12|Replace negative thoughts with positive thoughts
94|12|Remind yourself that joy & happiness can be learned
95|12|Consciously challenge your negative self-talk
96|13|Learn a mindfulness based breathing techique
97|13|Learn a new meditation techique 
98|13|Clean out 1 room in your house or office this week to decrease distractions
99|13|Become aware of & mitigate distractions at work or home
100|13|Try to spend time in nature everday
101|13|Schedule a 5-minute break every hour
102|13|Schedule a specific time to exercise everyday 
103|13|Eat a meal mindfully
104|13|Pay attention to your breathing for 2-3 minutes a day
105|14|Read an article about improving intrinsic motivation 
106|14|Connect your goals to your personal values and identity
107|14|Connect with the pleasure of cooking a healthy meal
108|14|Focus on how good it feels when you exercise
109|14|Reconnect with the meaningful aspects of your job
110|14|Journal about what is meaningful to you in your life
111|14|Spend more time each day doing things you enjoy
112|15|Identify activities you feel obligated to engage in & brainstorm on ways to make them more meaningful
113|15|Identify values and principles that are important to you
114|15|Create an action plan to eliminate some activities that are not meaningful to you
115|15|Identify a nonprofit organization that has meaning to you
116|15|Voluteer your time to a nonprofit organization or someone in need
117|15|Donate money to a nonprofit organization or someone in need
118|15|Have a kind conversation with the clerk at the grocery store or at the gas station
119|15|Journal about what is meaningful to you in your life
120|15|Engage with a peer group which interests you (e.g., religious, sports or any group which appeals to you) 
121|16|Be aware of how you label yourself & how that limits your growth 
122|16|Tell a friend about your envisioned furture self (i.e., who you want to become)
123|16|Be aware of the limitations you put on yourself
124|16|Look at qualities in yourself that you want to change or develop
125|16|Read about positive psychology & your limitless capacity for growth
126|16|Begin to link your goals to who you want to become
127|17|Focus on similarities between self and others
128|17|Consider someone else's perspective or point of view
129|17|Notice when you are being judgmental throughout the day
130|17|Offer to help someone who looks like they need a hand
131|17|Try to step into the shoes of someone you do not agree with on a political, religious or social matter. 
132|18|Spend time with a loyalist (i.e., a nutrient rich individual)
133|18|Minimize time with people who are negative (i.e., a toxic individual)
134|18|Work to enhance your relationship with a family member who challengs you
135|18|Pick a person to mentor at work or in your community
136|18|Be vulnerable by sharing about something difficult in your life with someone you trust
137|18|When communicating ask more questions
138|19|Ask questions while listening 
139|19|Paraphrase what someone said before talking about yourself
140|19|Ask a deep & meaningful question to someone you live or work with
141|19|Read about & practice active listening
142|19|Read about a current political situation & be prepared to talk about it
143|20|Find someone who will be available for you to talk to or visit with once a week for a month
144|20|Make one call a day to say hello to a friend or family member
145|20|Set up a network of people who can support you during a difficult time
146|20|Learn the rule, "When anxious or sad, make contact with someone"
147|20|Join a class you are interested in (e.g., dance class, wine making, parenting)
148|21|Find a safe place to go to where you feel calm and resourced
149|21|Make a list of several people who really care about you
150|21|Spend time appreciating nature at least 5-10 minutes each day (e.g., observe the clouds, find a favorite tree)
151|21|Make a list of your virtues, and put them next to your bed and look at them before going to sleep
152|21|Identify a negative thought and try to replace with a positive thought
153|21|Engage in brisk physical exercise 20-30 minutes per day
154|22|Try to eat 8 servings fruits and vegetables a day
155|22|Read about sleep health in our FIT Library
156|22|Move your body most days (20-30 minutes) doing any activity which is fun for you
157|22|Learn about healthy and unhealthy fats
158|22|Schedule one-on-one time with someone you want to get closer to
159|22|Expose yourself to bright light when you wake up each morning
160|22|Take a brisk 10 minute walk when you are feeling down 
161|22|Read about cravings and addictions
162|23|Notice triggers for cravings
163|23|Remove something from your environment which you crave 
164|23|Identify and monitor your stress since it diminishes willpower 
165|23|Subsitite the negative craving for something healthy 
166|23|Schedule two 10 minute rest breaks during your work day 
167|24|Increase positive self talk. Once a day say something kind to yourself about yourself 
168|24|When you find yourself being self-critical, change the thought to an affirmation
169|24|Self-care Commandment: Do not speak badly about yourself
170|24|Speak to yourself as though you are someone you respect
171|24|Ask one person for realistic reflection on your negative self talk 
172|24|Graciously accept a sincere compliment
173|25|Notice what makes you angry or frustrated each day. Keep a log for a week, and look for patterns.
174|25|Ask someone you trust who will give you honest feedback about your anger
175|25|Journal about your feelings once a day. The next day read what you wrote about on the previous day with a respectful and critical eye. Do this for one week
176|25|Take a one minute pause to check in with your body three times a day
177|25|Check to see if you are H.I.T.T (Hungry, Irritated, Thirsty or Tired) twice a day for one week
178|26|Stop three times a day, pause, and focus upon exhaling
179|26|Drink a glass of cool water three times a day and totally focus on the sensations of drinking the water
180|26|Make a note at lunch time each day to grade yourself on an anxiety scale from 1-10 (i.e., 1 = low; 10 = high)
181|26|Identify three things which make you anxious (e.g. money, work, your health)
182|26|Focus upon your hands and your feet three times a day
183|26|Diaphragmatic belly breathing: slow exhale from your belly, hold for 4 seconds, inhale slowly without any effort.
184|27|Write a complimentary letter to yourself as though you were your own best friend writing
185|27|Change your critical self-talk by noticing one kind thing about yourself
186|27|Remember that everyone struggles and suffers. You are not alone
187|27|Notice when you are judging yourself harshly 
188|27|Observe, but do not act on your feelings when you are criticized by someone else
189|28|Observe yourself without judgement several times a day
190|28|Take one minute to observe yourself before you enter a difficult conversation or meeting
191|28|Quitely observe yourself when you are angry, jealous, or sad
192|28|Notice when you are blaming and not taking personal responsibility
193|29|Express gratitude once a day to a co-worker or family member for a specific virtue which you see that they have
194|29|Practice a random act of kindness to someone who is not expecting it. Do this once a day for a week
195|29|Get in touch with one person and express how grateful you are to have them in your life
196|29|First thing when you wake up in the morning, acknowledge one thing that you are looking forward to that day
197|29|First thing in the morning, acknowledge one thing about the previous day that made you happy
198|30|Read about neuroplasticity and learn about how you can change your negative thoughts and feelings through changing your brain connections
199|30|Take in the good by pausing for 20-30 seconds when you notice something which feels good and positive
200|30|Find a way to be of service to someone else (e.g., tutor a child, offer a sick person food)
201|30|Lean into something that is uncomfortable in your life and accepted it
202|30|Practice delaying gratification throughout the day (e.g., avoid obsessively checking phone, 
203|30|Do one thing to deepen one meaninful relationship in your life
204|30|Focus upon your accomplishments and not your failures
205|30|Help a friend with finances or work
206|30|Create an action plan to limit your time with a negative person
207|30|Identify and build upon a strength you have
208|31|Read about stress resilience in the FIT Library
209|31|Identify your inner resources (e.g., sensitivity, generosity, sense of humor)
210|31|Notice your negative thinking
211|31|Pause and become more aware of your breath
212|31|Identify a particular difficuty as a positve challenge designed to help you grow
213|31|Seek out several people with whom you can honestly share your challenges with
214|31|Schedule a massage with a professional or a significant 
215|31|Check email only at specific times each day
216|31|When feeling overwhelmed, think about a happy memory for 2 minutes
217|31|Play your favorite music when you feel emotionally challenged
218|31|Use your emotional journal to write about the stressors in your life
219|31|Make a list of what is in your control and what's not in your hands
220|32|Go to sleep at around the same time each night
221|32|Eliminate caffeinated drinks after 2 pm in the afternoon 
222|32|Try to sleep between 7-9 hours a night 
223|32|Sleep in a very dark room 
224|32|Sleep in a cool room 
225|32|Turn off electronics or bright screens 2 hours before retiring at night 
226|32|Exercise most days for 20-30 minutes 
227|32|Create a calm evening ritual
228|32|If you suspect you might have a sleep disorder, then see a professional to seek diagnosis and treatmen
229|32|Write a "To Do" List before bed in your journal
230|32|Schedule two 10 minute rest breaks during your work day each day for a week
231|32|Record feelings about your day in your Worry Journal at night
232|32|To have a more restful sleep, each night before bed write down one thing which worries you, and resolve to take care of it tomorrow
233|33|Watch your natural breath patterns and try to simply accept them
234|33|Breathe into and out of your diaphragm slowly focusing on the exhale
235|33|Breathe in for 4 seconds, hold your breath for 4 seconds and exhale breath for 4 seconds.
236|33|Breathe in and imagine that you are breathing in love, breathe out imagining that you are breathing out love to others
293|34|Write a statement defining your purpose in this world
294|34|Identify two activities (like running, meditation, feeding the homeless and cooking for others), which enhance a sense of meaning and purpose in your life.
295|34|Write down two spiritual beliefs that you have in your journal
296|34|Find one activity which makes you feel connected to a purpose greater than your self
297|34|Consider that this is your last month on earth, what would you want to do with your time? Write down your ideas in your journal
298|34|Write down your strengths and virtues. Ask yourself how you are putting them to use?
299|34|Do something today which benefits another person or cause
300|34|Spend time in nature 
301|34|Identify a memory of an inspiring place in nature and close your eyes to imagine it
302|34|If you have a relationship with God, devote more time to your relationship 
303|35|Identify a place in nature which connects you to a feeling of awe.
304|35|Begin a mindfulness practice by sitting quietly for two minutes a day and simply observing your thoughts.
305|35|Imagine for one minute each day (when you get into bed at night) that you are never alone, and that everything is interconnected. 
306|35|Study a world religion which you knowvery little about
307|35|Read about the neuroscience of spiritual experiences (Newberg etc) in the FIT Library
308|35|Read about the health benefits of meditation in the FIT Library
309|35|Think of what it is that you yearn for for the planet or for humanity (i.e more love and peace, healthier oceans)
310|36|Set aside a special time each day to devote to meditation or prayer
311|36|Identify a special place where you can be with your meditation or prayer practice each day
312|36|Make sure you wont be interrupted when you sit down to meditate or pray
313|36|Set a timer for 5 minutes and devote that time to slience
314|36|Sit quietly for 5 minutes a day simply observing your thoughts without judgment
315|36|Observe your judgments, when they arise and let them pass. 
316|36|Imagine that you are the sky and that your thoughts are the clouds passing by 
317|36|Close your eyes and imagine your most favorite place in nature
318|37|Have a kind conversation with the clerk at the grocery store or at the gas station
319|37|Make eye contact with and smile at someone at work or at home once a day for a week 
320|37|Develop trust by practicing vulnerability. Tell one person something which makes you feel mildly afraid or ashamed
321|37|Engage with a peer group which interests you (e.g., religious, sports or any group which appeals to you) 
322|37|Write an email expressing your gratitude to one person a day for two weeks
323|37|Ask for help from somebody at work
324|37|Invite someone at work or home to collaborate with you on a task which you need help with
325|37|At the end of each day, reflect on ways you could have improved listening
326|37|Spend a few moments considering someone else's point of view
327|37|Pay a sincere compliment
328|38|Read dictionary definition of empathy; The ability to understand and also share the feelings of another person
329|38|Intentionally shift all of your attention onto someone else as they are speaking to you
330|38|Challenge yourself to be curious about strangers
331|38|Learn about someone else's life and what it feels like to be them
332|38|Challenge yourself to change a prejudice you might have about another person
333|38|Try to step into the shoes of someone you do not agree with on a political, religious or social matter. 
334|38|Offer to help someone who looks like they need a hand
335|38|Ask for clarification when listening
336|38|Apologize when you think you might have hurt someone's feelings
337|39|Practice non-violent communication: Say, "When you (identify the behavior)", "I feel (state how you feel)", "So please (make a request)."
338|39|Increase your social purpose by collaborating with one person on a home or work project for one week
339|39|Practice active listening and don't speak during one conversation a day; just listen
340|39|Listen more than you speak for one day at a time for a week
341|39|Increase attentiveness when listening by not focusing on yourself
342|39|During a conversation, ask follow-up questions
343|39|Spend 2 minutes a day considering similarities between you and someone you dislike or disagree with
344|40|Practice radical listening where all of your attention is on the other person you are conversing with
345|40|Observe the facial expressions of the person you are listening to
346|40|Ask a deep and meaningful question 
347|40|Paraphrase what someone else said before talking about yourself
348|41|Select eating habits or nutritonal content from the library.
349|41|Eat 4-6 times per day (at or below your BMR). This should include 3 substantive meals with 2-3 smaller meals. This helps stabilize blood sugar & promotes satiety. 
350|41|Consume 35 grams of fiber (or more) per day. 
351|41|Consume 7-13 servings of fruits or vegetables per day. 
352|41|Consume less than 6tsp of added sugar if you are a woman, or 9tsp if you are a male.
353|41|Take 2 min each day to focus on the way you want to look and feel; contrast that with your actions. Are your actions moving you closer or farther away from that ideal?
354|41|Start a daily food log within your journal.
355|42|Familiarize yourself with weight loss & nutritional content in the library
356|42|Eat 4-6 smaller meals each day, consuming less than your BMR calories (see: http://www.calculator.net/bmr-calculator.html). Keep daily caloric consumption at or below your BMR, endeavoring to add expenditure.
357|42|Consume 500 ml of cold water before each meal. 
358|42|Journal your food/ caloric consumption at least 5 days per week. Those who record their caloric intake are much more successful.
359|42|Before you consume any calories, be certain that you are fully aware of what you are consuming and why you are consuming it. We achieve the outcomes we want when our actions are intentional.
360|43|Eat 4-6 times per day.
361|43|Exercise: at least 2.5 hours of aerobic activity per week, and 2 days of some strength training (see assesment filters to identify point of entry) 
362|43|Consume a minimum of 2L of water each day. Water is the soup of life, and all cellular transactions are mediated through consumption of water. 
363|43|Stand up and move around for 5-10 min every hour.
364|43|Consume 30-38g. of fiber for men, and 25g or more per day. 
365|43|If you are feeling uninspired or flat, examine your mental and emotional state, stand up tall making your body as big as possible while redirecting and energizing your thoughts.
366|44|Choose an article or video from the library related to nutritonal content
367|44|Watch a nutritional video from the libary
368|44|Look at the nutritional information from 2 meals today and record how many grams of fiber and sugar per serving in each
369|44|Journal 3 days worth of meals this week and estimate how many calories those meals contained.
370|44|Learn about 2 core concepts in nutrition per week (see the library for topics)
371|45|Study and apply 1 or more inactivity related strategies from the library
372|45|Stand up and move about for 5-10 min every 45-60 min.
373|45|Trade sitting desk for standing desk if possible.
374|45|Watch less than 2.5 hours of television per day. 
375|45|View stairs and walking as opportunities for physical activity in lieu of elevators or escalators. 
376|45|Begin exercising 4 or more days per week. This should include at least 2 days of aerobic activity and 2 days of strength training.
377|46|Focus on and track daily nutritional habits (see nutrition content) 
378|46|Engage in a minimum of 2.5hours of moderate aerobic activity per week (see fitness table and filters). Engage in at least 2 days of strength training (see strength training content).
379|46|Journal: identify and revisit 5 things you want to achieve physically, be creative and honest in this exercise.
380|46|Select at least 3 mobility exercises to complete within a 7 day period (these can be incorporated within a strength session)
381|46|Increase the duration and intensity of exercise each week by 10%.
382|46|The ultimate aim should be to acquire 6 or more hours of physical activity per week.
383|47|Complete 2 strength sessions 20-40 min in duration (never do more than you are currently able)
384|47|Complete one or two level 1 strength session from the library
385|47|Make sure you select 2 foam rolling and 3 mobility exercises to complete throughout the week.
386|47|Log your workouts in your journal including how you felt
387|47|Try and mentally rehearse each session if you have time to look at them in advance. 
388|47|Raise your level of arousal and alertness before each session. Our mental and emotional states prepare our body.
389|48|See level 2 guidelines in the library for guidance
390|48|Complete 2-3 strength sessions per week, each lasting between 40-60 minutes (never do more than your body can currently handle) 
391|48|Choose and complete one or more level 2 strength sessions from the library
392|48|Make sure you select 2 foam rolling and 3 mobility exercises to complete throughout the week.
393|48|Log your workouts in your journal including how you felt
394|48|Try and mentally rehearse each session if you have time to look at them in advance. 
395|48|Raise your level of arousal and alertness before each session. Our mental and emotional states prepare our body.
396|49|Complete 2-4 strength training sessions each week
397|49|Select level 1, 2, or 3 workouts from the library. Try to avoid putting strength days back to back.
398|49|Make sure you select 2 foam rolling and 3 mobility exercises to complete throughout the week.
399|49|Log your workouts in your journal including how you felt
400|49|Try and mentally rehearse each session if you have time to look at them in advance. 
401|49|Raise your level of arousal and alertness before each session. Our mental and emotional states prepare our body.
402|50|Complete 2-4 strength sessions per week
403|50|Select level 2,3 or 4 workouts from the library. Try and avoid intense strength sessions on back to back days.
404|50|Make sure you select 2 foam rolling and 3 mobility exercises to complete throughout the week.
405|50|Log your workouts in your journal including how you felt
406|50|Try and mentally rehearse each session if you have time to look at them in advance. 
407|50|Raise your level of arousal and alertness before each session. Our mental and emotional states prepare our body.
408|51|Review level 1 related material from the library
409|51|Work up to getting 150 minutes of light-moderate cardio/aerobic training each week. Never do more than you can currently tolerate
410|51|Schedule and plan all of your workouts. Failure to plan is the same as planning to fail. 
411|51|Mentally rehearse the sessions before you perform them. This prepares the mind, and the mind prepares the body (see mental preparation)
412|51|Take a 15-20oz water bottle with you for each session
413|51|When it becomes hard to get or keep going, focus on why you are exercising. Identify 3 reasons.
414|51|Log your workouts in your journal under the physical dimension. 
415|51|Select and perform 3 mobility exercises.
416|52|Review level 2 related content from the library, or select workouts from the library
417|52|Get 2.5-3hours of aerobic activity per week, 30-75 minutes of this should be moderate to vigorous (see library for guidelines)
418|52|Schedule and plan all of your workouts. Failure to plan is the same as planning to fail. 
419|52|Mentally rehearse the sessions before you perform them. This prepares the mind, and the mind prepares the body (see mental preparation)
420|52|Take a 15-20oz water bottle with you for each session
421|52|When it becomes hard to get or keep going, focus on why you are exercising. Identify 3 reasons.
422|52|Log your workouts in your journal under the physical dimension. 
423|52|Select and perform 3 mobility exercises.
424|53|Review level 3 related content from the library, or select workouts from the library
425|53|Get 3- 5 hours of aerobic activity 3 weeks per month. 75-120 minutes of this should be at 75% or higher intensity (see library)
426|53|Schedule and plan all of your workouts. Failure to plan is the same as planning to fail. 
427|53|Mentally rehearse the sessions before you perform them. This prepares the mind, and the mind prepares the body (see mental preparation)
428|53|Take a 15-20oz water bottle with you for each session
429|53|When it becomes hard to get or keep going, focus on why you are exercising. Identify 3 reasons.
430|53|Log your workouts in your journal under the physical dimension.
431|53|Select and perform 3 mobility exercises.
432|54|Review level 4 related content from the library, or select workouts from the library
433|54|Get 4 or more hours of aerobic exercise per week or more, 90 min or more should be at 75% intensity or higher (see library)
434|54|Schedule and plan all of your workouts. Failure to plan is the same as planning to fail. 
435|54|Mentally rehearse the sessions before you perform them. This prepares the mind, and the mind prepares the body (see mental preparation)
436|54|Take a 15-20oz water bottle with you for each session
437|54|When it becomes hard to get or keep going, focus on why you are exercising. Identify 3 reasons.
438|54|Log your workouts in your journal under the physical dimension.
439|54|Select and perform 3 mobility exercises.
440|55|Focus your energy only taking action towards the outcomes you want to achieve. 
441|55|Learn and apply 1-3 self image, or self compassion related content pieces from the library.
442|55|Acknowledge when you feel hopeless or helpless, and shift your awareness towards the FIT process and working towards your goals and vision statement. 
443|55|In your journal, write 3 things you admire about yourself. Do this 5 days per week.
444|55|Each morning focus on 3 ways in which you can make others feel better today. 
445|56|Finish 1-3 sleep related content pieces in the library.
446|56|Exercise at least 4 days each week
447|56|Read 30 min before bed.
448|56|Enter a journal entry envisioning and describing the way you want to feel and interact throughout the following day.
449|57|Schedule an exercise or "play" session with one of your friends this week
450|57|Workout with a friend, or group of friends at least once per week
451|57|Participate in one or more group exercise classes per week
452|57|If you dont belong to some sort of health club, look into joining one in your area.
453|58|Start a budget and maintain it weekly. Use the budgeting tool in the library
454|58|Update your budget - use the budgeting tool in the library
455|58|Create a log of expenses - track these expenses on a weekly basis
456|58|Separate expenses into essentials and discretionary - try to minimize discretionary spending 
457|58|Evaluate purchases by cost per use - try to increase the efficiency of your purchases
458|59|Consolidate debt, especially credit card - Refer to the library for best strategies for reducing debt
459|59|Get credit reports - Refer to the library for best strategies on improving credit scores
460|59|Reduce debt on highest interest loan - take an extra $50 from discretionary spending to pay off loan
461|59|Pay an extra $100 down on outstanding loan - or across multiple loans
462|59|Work on debt exposure tool in the library
463|60|Don't use any drive-in window for a week
464|60|Don't dine out for a week
465|60|Don't buy any after market coffee for a week
466|60|Don't drink any soda for a week
467|60|Put $5 a day into a saving jar for the week. DO NOT TOUCH for 6 months 
468|60|Reduce electricity and water consumption
469|61|Open a savings account at another bank
470|61|Open a Roth or traditional IRA - refer to the library for understanding investment strategies
471|61|Put an extra $50 a week into a retirement account
472|62|Open a retirement account - refer to the library for understanding investment strategies
473|62|Speak to an/your investment advisor - refer to the library for what to look for in an advisor
474|62|Understand what it means to invest - educate yourself in the library
475|62|Use portfolio tool to help plan for your future
476|63|Use the risk aversion tool in the library to help you understand your personal risk tolerance
477|63|Adjust your portfolio based on your risk aversion
478|63|Think about the return and risk you want in your portfolio and then construct how you want your portfolio to look
479|64|Check to see if home buying is better than renting - use buy home versus rent tool
480|64|Check to see if you can afford the home you want to buy - use the mortgage to after tax salary rule
481|65|Pay all bills right away
482|65|Speak to a friend about money problems - try to list them from biggest concern to smallest concern
483|65|Make a money/spending/payment plan before making a tough or quick decision
484|65|Make a list of needs versus wants - and then assign your financial resources to each
485|65|Take a daily money minute to think about the ways to improve and tackle any money problems
486|66|Assess how much my family needs- use the insurance tool in the library
487|66|Buy an umbrella policy- review why this is so important
488|66|Set up an emergency fund- review in the library how to use the emergency fund
489|67|Assess the benefit of current short-term salary versus your future potential income elsewhere- go to the library to explore this further
490|67|Negotiate for higher salary- read in the library best tips and strategies
491|67|Invest in yourself and go back to school-read in the library why and when this is a good choice
492|67|Negotiate for more than just salary- understand the benefits of additional perks
493|67|Understand the time and cost of looking for a new job- review in the library
494|68|Plan a vacation- take time to enjoy life and leave work behind
495|68|Invest in your health- join the gym, try a new sport, sign up for a race.
496|68|Visit a new location- explore the world and new and different cultures
497|69|Move $5 or more of discretionary spending to a charity on a weekly basis
498|69|Volunteer your time to a local charity and invest in your community
499|70|Pursue a new opportunity to assess your market worth - review strategies in the library
500|70|Explore if there is a market for your skill and talents beyond your current job - go the library to understand more
501|71|Increase your physical activity - go to the gym/run/exercise an extra one or more days a weeks
502|71|Get a massage
503|71|Decrease your discretionary budget by 5% and put into savings or healthy activities
504|72|Talk with your partner about your finances-short-term and long-term, all concerns, and your goals
505|72|Talk with a friend about money issues-short-term and long-term, all concerns, and your goals
506|72|Help a friend with finances or work problems
507|73|Discuss any financial worries with someone close
508|73|Speak with an investment advisor to create a long-term plan
509|73|Create a short-term plan for debt payments-review in the library""")

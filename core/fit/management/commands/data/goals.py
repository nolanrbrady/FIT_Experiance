# -*- coding: utf-8 -*-
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

text = StringIO("""Id|GoalString|SubDimensionId
1|Learn something new this week|1
2|Improve memory|1
3|Increase sleep quality|1
4|Disregard the learning styles myth|1
5|Take steps to ensure your success and reach your goals|1
6|Increase intellectual capacity|2
7|Increase engagement at work|2
8|Increase engagement during sport or exercise|2
9|Increase engagement at home|2
10|Increase willpower|3
11|Improve stress management skills|3
12|Increase optimism|3
13|Improve attention|4
14|Increase internal motivation|5
15|Establish your purpose|5
16|Work on developing your identity|5
17|Improve empathic skills|6
18|Develop more positive social relationships|6
19|Improve conversation skills|6
20|Connect with others to develop a sense of wellbeing|7
21|Recognize and create new positive resources|7
22|Improve brain health|7
23|Become aware of cravings and addictions|7
24|Increase self-respect|8
25|Identify your anger triggers|8
26|Develop body awareness|8
27|Increase self compassion|8
28|Cultivate self observation|8
29|Develop gratitude practices|9
30|Increase authentic happiness|9
31|Develop stress hardiness|10
32|Increase sleep health|10
33|Develop comfort your stillness and breath|11
34|Identify higher meaning in your life|11
35|Familiarize yourself mindfulness or prayer practice|11
36|Establish a meditation or prayer practice|11
37|Increase social connections and support|12
38|Practice empathy|12
39|Improve communication skills|12
40|Improve listening skills|12
41|Improve Eating Habits|13
42|Lose Weight|13
43|Increase Energy Levels & Improve Health|13
44|Improve Nutrition Knowledge|14
45|Move More|15
46|Improve Physical Fitness Levels|15
47|Level 1 (Very Little Activity )|16
48|Level 2(Active 2-3 times, weekly)|16
49|Level 3 (Active 4-5 times, weekly)|16
50|Level 4 (In training)|16
51|Level 1 (Very Little Activity )|17
52|Level 2(Active 2-3 times, weekly)|17
53|Level 3 (Active 4-5 times, weekly)|17
54|Level 4 (In training)|17
55|Improve Self Image|32
56|Improve Sleep Habits|33
57|Increase Social Engagement|34
58|Work on your Budget|19
59|Eliminate bad debt|19
60|Start to implement bite-size money goals|19
61|Increase your monthly savings allocation|19
62|Review your investing strategy|18
63|Understand your risk aversion|18
64|Buying a home?|18
65|Banish toxic money thoughts|20
66|Review insurance needs|20
67|Review your current employment|20
68|Spend on Experiences, Not Things|21
69|Donate to a charity that holds a personal attachment|21
70|Maximize your talents|21
71|Get Your finances and body in shape|21
72|Have the money talk|22
73|Improve sleep|22""")

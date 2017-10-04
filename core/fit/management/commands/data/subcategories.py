try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

text = StringIO("""Id|Name|CategoryId|Multiplier
1|Learning Strategies|1|5
2|Intellectual Engagement|1|5
3|Effortful Control|1|5
4|Attention|1|5
5|Autonomy|1|5
6|Social Cognition|1|5
7|General Emotional Health|2|5
8|Self Compassion & Self Awareness|2|5
9|Stress Resilience|2|5
10|Gratitude & Positivity|2|5
11|Spiriturality|2|5
12|Social Engagement|2|5
13|Nutrition|3|5
14|Nutrition Knowledge|3|5
15|Inactivity|3|5
16|Aerobic Activity|3|5
17|Strength Training|3|5
18|Long Term Financial|4|5
19|Short Term Financial|4|5
20|Reduce Sadness|4|5
21|Increase Happiness|4|5
22|Social/Emotional Support|4|5
32|Improve Self Image|3|5
33|Improve Sleep Habits|3|5
34|Social Aspects of Training|3|5""")

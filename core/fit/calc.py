import logging
import math
import decimal as dec
from django.contrib.auth.models import User
import portal.core.fit.models as models
import portal.core.fit.utils as utils

logger = logging.getLogger('fit')


def getSubScoreColorByScore(dimension, score, memo=None):
    if memo is not None:
        if dimension in memo:
            mod = memo[dimension]
        else:
            mod = models.ScoreColor.objects.get(pk=dimension)
            memo[dimension] = mod
    else: 
        mod = models.ScoreColor.objects.get(pk=dimension)
    if score < 10:
        color = mod.low
    elif score >= 10 and score < 15:
        color = mod.medium
    elif score >= 15 and score < 20:
        color = mod.high
    else:
        color = mod.max
    return color


# List<Question> questions, SubCategory subCategory, List<Answer> answers, decimal shortTermValue
#
def getSubCatScore(subquestions, subcategory, answers, shortTermValue):
    
    score = utils.SubCategoryScore()

    total = 0
    subCatDivisor = dec.Decimal(len(subquestions))

    index = {a.question.id: a for a in answers}
    
    # TODO: single efficient query for Qs and As 
    for question in subquestions:
        
        answer = index.get(question.id, None)
                
        if answer:
            #grabbing answer.Value from Long-Term, question 5 to use in Short-Term calc later
            if (question.id == 52):
                shortTermValue = answer.value;
            
            #calculate reversed score
            if question.is_reversed:
                if answer.value == 0:
                    pass
                else:
                    answer.value = -(answer.value - 6)
            
            #accounted for double and triple points
            if question.weight == 0:
                question.weight = 1 # WTF?
                total += answer.value
            else:
                total += answer.value * question.weight;
            
            if question.weight > 1:
                subCatDivisor += question.weight - 1
            
            #support N/A value
            if answer.value == 0 and subcategory.id != 19:
                subCatDivisor -= question.weight;
            
            #special case: Short-Term, question 12
            if subcategory.id == 19 and question.id == 59 and answer.value > 0:
                total += shortTermValue / 2
                subCatDivisor += dec.Decimal('0.5')
            elif subcategory.id == 19 and question.id == 59 and answer.value == 0:
                total += shortTermValue / 2
    
    score = utils.SubCategoryScore(
        SubCategory = subcategory,
        Score = (total * subcategory.multiplier) / float(subCatDivisor) if subcategory.multiplier > 1 else total,
        #grab shortTermValue and return it to use in the next subCat calc
        ShortTermValue = shortTermValue
    )
    return score


# private static DimensionScores GetDimAndSubScoresByCategoryId(List<Answer> answers, currentDimension):

def getDimAndSubScoresByCategoryId(answers, currentDimension, memo=None):
    
    #var categoyRepo = new BaseRepository<Dimension>();
    #var questionRepo = new BaseRepository<Question>();
    #var subCategoryRepo = new BaseRepository<SubCategory>();
    
    #questions = [q for q in models.Question.objects.filter(dimension=currentDimension, is_active=True).all()]
    
    scores = []
    
    currentShortTermValue = 0
    
    subcategories = models.SubCategory.objects.filter(dimension=currentDimension).all()
    
    for subcategory in subcategories:
        subquestions = list(models.Question.objects.filter(dimension=currentDimension, subcategory=subcategory, is_active=True).all())
        score = getSubCatScore(subquestions, subcategory, answers, currentShortTermValue)
        currentShortTermValue = score.ShortTermValue
        score.Color = getSubScoreColorByScore(score.SubCategory.dimension, score.Score, memo)
        scores.append(score)
    
    # sum of all the sub cat scores divided by total dimensions
    avg_score = sum([s.Score for s in scores]) / len(scores)
    
    dimAndSubScores = utils.DimensionScores(
        Dimension = currentDimension,
        DimScore = avg_score,
        SubCatScores = scores
    )
    return dimAndSubScores


# public static decimal GetGraphBalanceScore(DimensionScores cognitive, DimensionScores emotional, DimensionScores physical, DimensionScores financial)
#
def getGraphBalanceScore(cognitive, emotional, physical, financial):
    
    # List<DimensionScore> dimScores = new List<DimensionScore>();
    dimScores = []
    
    #get 4 dim scores
    dimScores.append(utils.DimensionScore(Dimension = cognitive.Dimension, Score = cognitive.DimScore))
    dimScores.append(utils.DimensionScore(Dimension = emotional.Dimension, Score = emotional.DimScore))
    dimScores.append(utils.DimensionScore(Dimension = physical.Dimension, Score = physical.DimScore))
    dimScores.append(utils.DimensionScore(Dimension = financial.Dimension, Score = financial.DimScore))
    
    #FIT = sum(4 dim scores)
    fitScore = sum([s.Score for s in dimScores])
    
    #calc BALANCE aka standard deviation
    dimAverage = fitScore / len(dimScores)
    sumOfSquaresOfDifferences = sum([(s.Score - dimAverage) * (s.Score - dimAverage) for s in dimScores])
    balance = math.sqrt(sumOfSquaresOfDifferences / (len(dimScores) - 1))
    
    return balance


def getSubScoreDescription(items):
    return items


def getDimensionDescription(items):
    
    # items: List<OverviewData>
    for item in items:
        item.rampingUp = ""
        item.developer = ""
        item.experienced = ""
        item.FITastic = ""
    return items
    for item in items:
        id = item.subScores[0].SubCategory.dimension.id
        
        if id == models.dimensions.DimensionId.Cognitive.value:
            item.rampingUp = "Negative thinking patterns might be dragging other areas of your life down, and you might have difficulty gaining control over your thoughts, such as staying focused and not being distracted. In addition to being uninterested in learning new things, you may not believe in your own ability to reach competency in various tasks. You have the tendency to avoid obtaining feedback from other people because you believe your perspective is better than others. You may not be aware of the limitations you set on yourself by believing that your situation is out of your control; thereby, significantly undermining your potential to bring growth and improvements to your life."
            item.developer = "Although you might set goals and wish to learn new things, you may not engage in the most productive thinking processes to help you attain those goals. Thus, your cognitive habits might be sabotaging your ability to reach your goals. You may be easily distracted and have a hard time concentrating when under pressure. You can be prone to evading challenges, especially when it involves learning new things. You may be hesitant to seek other people's opinions and perspective because this threatens your belief system. There might be times that you second guess your ability to succeed, which undermines your likelihood of setting challenging goals. Thus, you may accomplish much less than you are capable."
            item.experienced = "Your cognitive habits are progressing towards a highly efficient mental framework, though there are still areas that need improvement. You might be likely to set the bar high in terms of your goals, and are inclined toward learning new things, but some of your thinking might undercut your ability to fully reach your potential. Though you are focused on attaining what you set out to accomplish, you might find there are times you are easily distracted or you might have difficulty staying focused for long periods. At times you may feel a victim of circumstance and might need to work on developing a growth mindset where you feel more in control of your own thinking, decisions, and, therefore, your situation."
            item.FITastic = "Your cognitive habits are effective, productive, and fully integrated with your purpose and goals. Your method of approaching problems is likely to help you find solutions to difficult situations. You create environments that help you thrive, and your thinking directly impacts your likelihood to be successful in what you set out to accomplish. You seek out feedback and are eager to understand other people's perspectives. You are able to focus your attention on the task at hand until it is accomplished. You enjoy learning, do not shy away from challenges, and believe in your ability to succeed. In short, you are cognitively FITastic."
        elif id == models.dimensions.DimensionId.Emotional.value:
            item.rampingUp = "At this point in your life you may be experiencing worries or fears and may have a difficult time understanding your emotions. You may be lacking in the skills which allow you to be kind to yourself, and your ability to deal with stress is not yet developed. Sensing a disconnect from your emotions may make you feel out of control at times and may interfere with your social interactions and your ability to get close to others. You may not be experiencing much gratitude in your day-to-day life, and negative thoughts may be your default position. You may not have a spiritual practice at this time or may not be fulfilled by it if you do. You are beginning  your journey to emotional FITness."
            item.developer = "Although you may be interested in emotional fitness, you are still in the beginning stages of your journey. Emotional stability may be something you experience on occasion, but not consistently. Your emotional intelligence may be growing. Positivity and your ability to feel resilient to stress have the potential for growth, but they are not yet working optimally for you and may be preventing you from thriving in the other dimensions. You may be on the road to feeling more optimistic and may be working on your negativity bias, trying to turn it around to better serve your emotional health. Building your self-awareness skills, cultivating your spiritual practice, and developing your social acumen will serve you well on this and the other FIT dimensions."
            item.experienced = "You have developed some emotional awareness and have a sense of self which are creating some emotional resilience and helping you to feel more consistent and balanced. You are working on being able to manage your emotional distress more easily, and you have some tools in your emotional toolbox. You may be working with your thoughts to help you change how you feel. At this point you may be able to sustain a feeling of emotional wellness for longer periods of time. Overwhelming feelings may occur less frequently, as you are still learning to regulate your nervous system. If you fall into this range, you are doing well from an Emotional FITness perspective, but your life would benefit from deepening your emotional, spiritual, and social repertoire."
            item.FITastic = "A positive mindset and keen self-awareness characterize your emotional skills. If your scores fall into this range you are emotionally resilient and have a spiritual connection, which creates more meaning and productivity in your work and home life. You are reaping the benefits of gratitude practices, and you appreciate that being compassionate with yourself has its benefits. Your social skillfulness positively impacts how supported you feel and how healthy you are physically. Your emotional strengths and habits are creating a strong platform for further developing balance amongst the Cognitive, Physical, and Financial dimensions of your FIT life.";    
        elif id == models.dimensions.DimensionId.Physical.value:
            item.rampingUp = "In this range, you may be experiencing the lack of a well-defined sense of personal ideal or archetype related to your physical body. Currently, you are at higher risk for a variety of poor health outcomes and constellations of different illnesses. You may be suffering from low self-image and diminished feelings of self-efficacy. A lack of physical activity and substandard nutrition increase the likelihood you may be suffering from mental and emotional problems. The good news is, when individuals in this category take action, the results can be massive. You have great potential for change and growth.   With changes, you can often experience quite dramatic outcomes, and virtually any well-directed action will yield positive results.  You will greatly benefit from developing a clear vision for your ideal physical state and taking positive action in that direction."
            item.developer = " You probably are not consistently adhering to desirable food and exercise choices. Improvements should be focused on gaining knowledge about nutrition and exercise habits. Growth should be focused on finding realistic ways to make positive lifestyle changes.  At this time, you tend to have poor nutritional habits and low levels of physical activity, both of which contribute to low levels of energy and negative self-image. The good news is you can greatly benefit from clearly stating your desired physical outcomes.  You currently possess immense potential for development.  Even minor lifestyle changes can produce significant improvements in your overall physical health.   Creating concepts of personal physical standards and ideals, coupled with well-directed action, can produce impressive results in your life."
            item.experienced = "You are currently attempting to make physical fitness a priority in your life but have ample room for improvement with nutritional components or activity levels. Often, you perform well with either nutrition or physical activity, but rarely apply equal effort to both at the same time. Therefore, consistent application of both sound nutritional and exercise habits (simultaneously) is critical to personal development.  Focus on creating more balance between nutrition and exercise, as well as making small improvements in both areas, to generate the best outcomes.  Core concepts for you include defining your desired physical outcomes as well as opportunities for improvement, then taking the necessary steps and appropriate actions in this direction."
            item.FITastic = "You make physical fitness a top priority, working out everyday or most days during the week. You are acutely aware of nutrition and have healthy eating habits.  One hallmark you possess is a well-developed sense of your personal, physical ideal. You tend to have a strong mental image pertaining to how you want to look, feel, or perform physically. Sound exercise and nutritional habits have become part of your routine. In order for you to maintain a growth state,  seek out new physical challenges, continually change exercise modalities, and safely try new activities. The healthiest within this group understand the importance of consuming several servings of fruits and vegetables each day, and the necessity of sleep. You experience a high degree of balance across the subcategories within the Physical dimension."
        elif id == models.dimensions.DimensionId.Financial.value:
            item.rampingUp = "You are taking your first steps toward financial FITness, but it may feel overwhelming initially. This could be a function of any or all of the following: significant debt, limited cash flow, a low paying job, no financial savings, or frequent sleepless nights.  One or a combination of these factors may be contributing to significant financial concerns that are increasing sadness and limiting your happiness. You are at a place where you need some guidance and are ready to make significant growth in your Financial FITness."
            item.developer = "Although you may be striving toward financial FITness, you may need to overcome some significant hurdles.  These may include a short-term cash flow problem, no long-term financial plan, concerns over a job, or the weight of paying bills.  Your current wage may be holding you back, and you may have trouble sleeping at night because of financial worries. Although you are headed in the right direction, you are looking for some guidance in terms of moving forward on your financial goals."
            item.experienced = "Your financial outlook is progressing to allow you to put yourself in a position to best maximize the other dimensions for a FIT and fulfilling life.  You may have some short-term cash concerns or the workings of a long-term financial plan. The disposable income you have may allow you to pursue a healthy lifestyle, but you may have some worries about your immediate financial future. You are looking for some guidance in how to continue your progression past a place of worry to optimal Financial FITness."
            item.FITastic = "Your financial outlook puts you in a position to best maximize the other dimensions for a FIT and fulfilling life.  You have no short-term cash concerns, you have a long-term financial plan, and the disposable income you have allows you to pursue a healthy lifestyle. Your high Financial FITness puts you in an optimal place to focus on achieving BALANCE in your life through Cognitive, Emotional, and Physical FITness."
        else:
            raise Exception(item.subScores[0].SubCategory.dimension)
    return items

    

class UsersAnswers(object):
    
    @staticmethod
    def scores(user, survey, cognitiveBool=1, financialBool=1, emotionalBool=1, physicalBool=1):
        # transcribed from .Net
        
        answers = []
        data = []
        
        answers = list(models.Answer.objects.filter(survey=survey).all())
        
        answer = utils.OverviewData()
        
        for dim in models.Dimension.objects.all():
            if dim.name == 'Cognitive':
                cog = dim
            elif dim.name == 'Emotional':
                emo = dim
            elif dim.name == 'Physical':
                phy = dim
            elif dim.name == 'Financial':
                fin = dim
        
        # grab dimension score and its sub cats score in 1 method
        # as DimensionScores
        memo = {} # poor-man's memoization
        cognitiveScores = getDimAndSubScoresByCategoryId(answers, cog, memo)
        emotionalScores = getDimAndSubScoresByCategoryId(answers, emo, memo)
        physicalScores = getDimAndSubScoresByCategoryId(answers, phy, memo)
        financialScores = getDimAndSubScoresByCategoryId(answers, fin, memo)
        
        if cognitiveBool:
            answer = utils.OverviewData(
                id = "cognitive",
                order = 1,
                label = "Cognitive",
                color = "#FFB163",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = cognitiveScores.SubCatScores
            )
            answer.score = round(cognitiveScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
            data.append(answer)
        else:
            answer = utils.OverviewData(
                id = "cognitive",
                order = 1,
                label = "Cognitive",
                color = "#D3D3D3",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = cognitiveScores.SubCatScores
            )
            answer.score = round(cognitiveScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
                subscore.Color = "#D3D3D3"
            data.append(answer)
        
        if emotionalBool:
            answer = utils.OverviewData(
                id = "emotional",
                order = 3,
                label = "Emotional",
                color = "#63C7E7",
                weight = 0.5,
                subScores = emotionalScores.SubCatScores,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
            )
            answer.score = round(emotionalScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
            data.append(answer)
        else:
            answer = utils.OverviewData(
                id = "emotional",
                order = 3,
                label = "Emotional",
                color = "#D3D3D3",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = emotionalScores.SubCatScores
            )
            answer.score = round(emotionalScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
                subscore.Color = "#D3D3D3"
            data.append(answer);
        
        if physicalBool:
            answer = utils.OverviewData(
                id = "physical",
                order = 4,
                label = "Physical",
                color = "#D38989",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = physicalScores.SubCatScores
            )
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
            data.append(answer)
        else:
            answer = utils.OverviewData(
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                id = "physical",
                order = 4,
                label = "Physical",
                color = "#D3D3D3",
                weight = 0.5,
                subScores = physicalScores.SubCatScores
            )
            answer.score = round(physicalScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
                subscore.Color = "#D3D3D3"
            data.append(answer)
        
        if financialBool:
            answer = utils.OverviewData(
                id = "financial",
                order = 2,
                label = "Financial",
                color = "#A7D4A4",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = financialScores.SubCatScores
            )
            answer.score = round(financialScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
            data.append(answer)
        else:
            answer = utils.OverviewData(
                id = "financial",
                order = 2,
                label = "Financial",
                color = "#D3D3D3",
                weight = 0.5,
                balance = round(getGraphBalanceScore(cognitiveScores, emotionalScores, physicalScores, financialScores), 2),
                subScores = financialScores.SubCatScores
            )
            answer.score = round(financialScores.DimScore, 2)
            for subscore in answer.subScores:
                subscore.Score = round(subscore.Score, 2)
                subscore.Color = "#D3D3D3"
            data.append(answer)

        for item in data:
            item.weight = 25 / len(item.subScores)
        #
        data = getSubScoreDescription(data)
        data = getDimensionDescription(data)
        logger.info("Scores for {}".format(user))
        return data


class SurveyMatrix(object):
    
    def __init__(self, latest=True):
        self._cols = []
        self._rows = []
        self._surveys = []        

    def dimensions(self):
        # change order if necessary
        for dim in models.Dimension.objects.all():
            if dim.name == 'Cognitive':
                cog = dim
            elif dim.name == 'Emotional':
                emo = dim
            elif dim.name == 'Physical':
                phy = dim
            elif dim.name == 'Financial':
                fin = dim
        return (cog, emo, phy, fin)
    
    def user_surveys(self, latest=True):
        # memoize
        if self._surveys:
            for user, survey in self._surveys:
                yield user, survey
        questionCount = models.Question.objects.exclude(dimension__isnull=True).count()
        for user in User.objects.all():
            try:
                completed = []
                for _n, survey in enumerate(models.Survey.objects.filter(user=user, is_active=False).order_by('modified'), start=1):
                    num_answers = models.Answer.objects.filter(survey=survey).count()
                    if num_answers == questionCount:
                        completed.append(survey)
                if not completed:
                    raise models.Survey.DoesNotExist
                if latest:
                    completed = [completed[-1]]
                self._surveys.append((user, completed))
                yield (user, completed)
            except models.Survey.DoesNotExist:
                print('No survey for {}'.format(user))
    
    def questions(self):
        for _n, dim in enumerate(self.dimensions(), start=1):
            subtotal = models.Question.objects.filter(dimension=dim).count()
            _z = len(str(subtotal))
            for _num, question in enumerate(models.Question.objects.filter(dimension=dim).order_by('seq'), start=1):
                qid = '{}.{}'.format(_n, str(_num).zfill(_z)) 
                yield(qid, question)
    
    def scores(self):
        #
        scores_cols = ['Email']
        scores_cols.extend([d.name for d in self.dimensions()])
        data = calc.UsersAnswers.scores(user, survey)
        for item in data:
            print(json.dumps(item.to_dict(), indent=4))
        _tmp = {v.id: v.score for v in data}
        scores_row = [user.email]
        scores_row.extend([_tmp[col.lower()] for col in cols[1:]])
        rows.append(row)
        
    
    def subscores(self):
        xref = {}
        rows = []
        cols = ['Email']
        for d in self.dimensions():
            _z = len(str(models.SubCategory.objects.filter(dimension=d).count()))
            for n, c in enumerate(models.SubCategory.objects.filter(dimension=d), start=1):
                idx = '{}.{}'.format(d.id,str(n).zfill(_z))
                xref[c.name] = idx
                print(idx, c.name)
                cols.append(idx)
        for user, surveys in self.user_surveys():
            for survey in surveys:
                data = UsersAnswers.scores(user, survey)
                index = {}
                for entry in data:
                    print(entry.id, entry.score)
                    for subscore in entry.subscores:
                        idx = xref[subscore.SubCategory.name]
                        index[idx] = subscore.Score
                # repack in col-order | overkill?
                row = [user.email]
                for idx in cols[1:]:
                    row.append(index.get(idx, None))
                rows.append(row)
        return cols, rows, xref 
        
        
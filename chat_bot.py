

brick1=7.5
brick2=8.5
goods=['кирпич1','кирпич2','кирпич3','кирпич4','кирпич5','кирпич6',
       'черепица1','черепица2','брущатка1','брущатка2','блок1','блок2',
       'гавайская','гавайская пицца','неополитано','неополитано пицца','чили',
      'чили пицца','гавайскую','гавайскую пиццу','пиццу неополитано','неополитано пиццу',
      'чили пиццу','пиццу чили']

order_words=['заказ','беру','закажу', 'заказываю', 'хочу','давай','возьму']
bye=['Щастливо','До скорого','Обращайтесь','Всего хорошего']
order_from_client=[]
ordered={'клиент':'','товар':'','шт':''}

BOT_CONFIG = {

    'intents':{
        'hello':{
            'examples':['Привет','Добрый день','Шалом','Здрасьте','Здорова','Добрый вечер','хелов'],
            'responses':['Привет','Доброго времени суток','Здравствуйте','Приветствую']
        },
        'hello_ukr':{
            'examples':['Привіт','Доброго дня','Шалом','Вітаю','Здоров','Доброго вечора','хелов'],
            'responses':['Привіт','Доброго дня','Добридень','Привітулі']
        },        
        'complim':{
            'examples':['приятно','любезно','нравишся'],
            'responses':['взаимно','приятно с тобой общаться','мне нравится']
        },  
        'bye':{
            'examples':['Пока','Выход','exit','Досвидания','Всего хорошего','Всего доброго','Прощай'],
            'responses':['Щастливо','До скорого','Обращайтесь','Всего хорошего']
        },
        'thanks':{
            'examples':['Спасибо','Благодарю','Спасибо большое'],
            'responses':['Обращайтесь еще','Пожалуста','На здоровье']
        },
        'name':{
            'examples':['Как тебя звать','Как твое имя','Как тебя зовут','Ты кто','кто ты'],
            'responses':['Меня не зовут, я прихожу','Могу быть Олегом','Могу быть Катей','Я просто бот']
        },
        'doing':{
            'examples':['Как дела','Че как','Как оно ничего', 'как жизнь', 'как житуха'],
            'responses':['Все гуд','Все круто','Отлично','Курю бамбук']
        },         
        'season':{
            'examples':['какой сейчас сезон','какое время года'],
            'responses':['зима','весна','лето','осень']
        },
        'city':{
            'examples':['где ты находишся','ты из какого города'],
            'responses':['Киев','Обухов']
        },
        'weather':{
            'examples':['какая сейчас погода','погода'],
            'responses':['солнце светит','местами дождь','пасмурно']
        },
        'money':{
            'examples':['какой курс доллара','по чем евро','курсы валют'],
            'responses':['небольшой','думаю где то по 30','хороший']
        },
        'can':{
            'examples':['что ты умееш','что ты умееш делать','что ты можеш делать','что ты знаеш','чем можеш помочь'],
            'responses':['умно отвечаю','шучу','принимаю заказы','сообщаю цену','чем смогу помогу']
        },
        'news':{
            'examples':['какие новости','что нового','что расскажеш'],
            'responses':['все по старому','много хороших новостей','без изменений']
        },
        'joke':{
            'examples':['анекдот','умееш шутить','что то смешное','шути'],
            'responses':['Мне как-то очень трудно\n' 
                'держаться от греха подальше.','Что у женщины на уме,\n'
                'то у мужика в кредит.','Изобрели робот-пылесос - и что, прогресс остановился?\n'
                'Где робот-ванна, где робот-унитаз?..']
        },
        'order':{
            'examples':['хочу сделать заказ','хочу заказать товар','можно заказать товар',
                        'заказать что то','нужно разместить заказ','заказываю'],
            'responses':['какой товар хотите заказать','что именно заказать']
        },
        'food':{
            'examples':['еду','что то поесть','покушать','хавчик', 'хочу есть'],
            'responses':['кухня украинская, итальянская, японская, грузинская']
        },
        'bricks':{
            'examples':['кирпич', 'заказать кирпич'],
            'responses':['какой именно интересует: рядовой, облицовочный, печной']
        },
        'bricks2':{
            'examples':['кирпич рядовой','рядовой кирпич' ],
            'responses':[f'можем предложить: кирпич1 - {brick1}, кирпич2 - {brick2}'],
            'context':['']
        },
        'bricks3':{
            'examples':['кирпич облицовочный','облицовочный кирпич'],
            'responses':['можем предложить: кирпич3 - 17,5, кирпич4 - 18,5']
        },
        'bricks4':{
            'examples':['кирпич печной','печной кирпич'],
            'responses':['можем предложить: кирпич5 - 27,5, кирпич6 - 38,5']
        },
        'roof':{
            'examples':['черепицу','керамическую черепицу','черепицу керамическую'],
            'responses':['можем предложить: черепица1-20, черепица2-25']
        },
        'blocks':{
            'examples':['блоки','керамоблоки','газоблоки'],
            'responses':['можем предложить блок1-10, блок2-15']
        },
        'bruki':{
            'examples':['брущатку','нужна брущатка'],
            'responses':['можем предложить: брущатка1-10, брущатка2-15']
        },
        'pizza':{
            'examples':['хочу заказать пиццу','давай пиццу','какую то пиццу', 'хочу пиццу','пиццу','пицца'],
            'responses':['у нас есть: гавайская пицца, неополитано  пицца, чили пицца']
        },
        'pizza_cost':{
            'examples':['сколько стоит пицца','какая цена','какие цены', 'какая цена пиццы', 'какие цены на пиццу'],
            'responses':['гавайская пицца-100, неополитано  пицца-120, чили пицца-115']
        },    
       'putin':{
            'examples':['путин'],
            'responses':['хуйло!']
        },      
        'ukr':{
            'examples':['слава украине'],
            'responses':['Героям слава']
        }, 
        'empty':{
            'examples':['',' '],
            'responses':['напиши свой вопрос','не хочеш со мной общаться?','не кривляйся']
        }
    },

    'failure_phrases': [
        'Перефразируйте вопрос',
        'Не понятно',
        'Моя твоя не понимать'
    ]
}

import pickle
import random
import nltk
from sklearn.svm import LinearSVC, SVC
from sklearn.feature_extraction.text import TfidfVectorizer


X_texts = [] # реплики
y = [] # их класы

for intent, intent_data in BOT_CONFIG['intents'].items():
        for example in intent_data['examples']:
            X_texts.append(example)
            y.append(intent)

vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4))
X = vectorizer.fit_transform(X_texts)
clf = LinearSVC().fit(X, y)

# save model to a file
# filename = 'bot_LinearSVC.sav'
# pickle.dump(clf, open(filename, 'wb'))

#### load the model from disk ######

# clf = pickle.load(open('bot_LinearSVC.sav', 'rb'))
# result = loaded_model.score(X_test, Y_test)

#######################

# clf_proba = SVC(probability=True).fit(X, y)

# def get_intent(question):
#     question_vector = vectorizer.transform([question])
#     intent = clf.predict(question_vector)[0]

#     index = list(clf_proba.classes_).index(intent)
#     proba = clf_proba.predict_proba(question_vector)[0][index]
#     print(intent,proba)
#     if proba < 0.11:
#         return intent

def get_intent(question):
    question_vector = vectorizer.transform([question])
    intent = clf.predict(question_vector)[0]

    examples = BOT_CONFIG['intents'][intent]['examples']
    for example in examples:
        dist = nltk.edit_distance(question,example)
        if len(question)<=1:
            intent='empty'
            return intent
        else:
            dist_percentage = dist / len(question)
            # print(intent,dist_percentage)
            if dist_percentage < 0.45:
                return intent
            

def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases) 
    

def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'йцукенгшщзхъфывапролджэячсмитьбю- ']
    text = ''.join(text)
    return text

# with open('dialogues.txt', encoding="utf8") as f:
#     content = f.read()

# dialogues = [dialogue_line.split('\n') for dialogue_line in content.split('\n\n')]

# questions = set()
# qa_dataset = [] # [[q,a],[q1,a1],...]

# for replicas in dialogues:
#     if len(replicas) < 2:
#         continue

#     question, answer = replicas[:2]
#     question = filter_text(question[2:])
#     answer = answer[2:]

#     if question and question not in questions:
#         questions.add(question)
#         qa_dataset.append([question, answer])


# qa_by_word_dataset = {}  # {'word':[q,a], ....}

# for question, answer in qa_dataset:
#     words = question.split(' ')
#     for word in words:
#         if word not in qa_by_word_dataset:
#             qa_by_word_dataset[word]=[]
#         qa_by_word_dataset[word].append((question, answer)) # was like this ([question, answer])

# qa_by_word_dataset_filtered={word: qa_list
#                             for word, qa_list in qa_by_word_dataset.items()
#                             if 100 <=len(qa_list) <= 5000}

# save a dictionary "qa_by_word_dataset_filtered" to a file "dialogues.pkl"


# a_file = open("dialogues.pkl", "wb")

# pickle.dump(qa_by_word_dataset_filtered, a_file)

# a_file.close()

a_file = open("/home/Vitaliy4D/mysite_1/dialogues.pkl", "rb")
qa_by_word_dataset_filtered = pickle. load(a_file)
a_file. close()


def generate_answer_by_text(text):
    text = filter_text(text)
    words = text.split(' ')
    qa = []
    for word in words:
        if word in qa_by_word_dataset_filtered:
            qa += qa_by_word_dataset_filtered[word]
    qa=list(set(qa))[:1500] # discrease time of work

    results = []
    for question, answer in qa:
        dist = nltk.edit_distance(question,text)
        dist_percentage = dist / len(question)
        results.append([dist_percentage,question, answer])

    if results:
        # results = min(results, key=lambda pair: pair[0]) 
        dist_percentage, question, answer = min(results, key=lambda pair: pair[0])
        if dist_percentage < 0.45:
            return answer


def get_failure_phrases():
    phrases=[]
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases) 


stats = [0,0,0]
def get_bot_response(question):
    
    # NLU
    intent = get_intent(question)
    
    # question_order_word=' '.join(question.split(' ')[:1])
    # question_goods=' '.join(question.split(' ')[1:])
    
    # if question_order_word and question_goods not in ['',' ',None]:
    #     if any(question_order_word in s for s in order_words):
    #         if any(question_goods in s for s in goods):
    #             client_name=input('имя?')
    #             quantity=input('шт?')
    #             if client_name and quantity:
    #                 ordered.update({'клиент':client_name,'товар':question_goods,'шт':quantity})
    #                 print(f'Твой заказ: {client_name,question_goods,quantity} принят')
    #                 intent='bye'
    #         else:
    #             pass    

    # getting answer
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            stats[0]+=1
            return answer
            
    # generate answer by context
    answer = generate_answer_by_text(question)
    if answer:
        stats[1]+=1
        return answer
    # if none of above give an answer
    stats[2]+=1
    answer = get_failure_phrases()
    return answer

# question = None
# while question not in ['exit','выход'] and answer not in bye:
#     question = input()
#     answer = get_bot_response(question)
    

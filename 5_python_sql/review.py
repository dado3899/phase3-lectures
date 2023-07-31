# Join tables in Python
class Journal:
    def __init__(self,name):
        self.name = name
        self.specilties = []
        self.articles = []
class Author:
    def __init__(self,name):
        self.name = name
        self.articles = []

    def submitArticle(self,topic, date, journal):
        new_article = Article(topic,date,self,journal)
        self.articles.append(new_article)
        journal.articles.append(new_article)
        return new_article

class Article:
    all_articles = []
    def __init__(self, topic, date, author, journal):
        self.author = author
        self.journal = journal
        self.topic = topic
        self.date = date
        
        Article.all_articles.append(self)

    def get_topic(self):
        return self._topic
    def set_topic(self,value):
        # if isinstance(value,str):
        if type(value) is str and value in self.journal.specilties:
            self._topic = value
        else:
            raise ValueError("Not valid topic")
    topic = property(get_topic,set_topic)

j = Author("Jerrick")
flatirons_journal = Journal("Flatirons Journal of science and shit")
flatirons_journal.specilties = ["Software Engineering", "Cybersecurity","CSS"]
j.submitArticle("CSS","7/28/23",flatirons_journal)
print(j.articles)
print(flatirons_journal.articles)
print(Article.all_articles)
# SQL Basics

# Run sql file
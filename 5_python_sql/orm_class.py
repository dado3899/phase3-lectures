# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("science.db")
cursor = connection.cursor()

# print(cursor.execute('''
# SELECT journals.name, articles.topic, authors.name
# FROM articles
# JOIN authors, journals
# ON articles.author_id = authors.id AND articles.journal_id = journals.id
# ''').fetchone())

# print(cursor.execute('''
# INSERT INTO journals (name)
# VALUES (?)
# ''',("Testing journal",)).fetchone())


class Journal:
    all_journals = []
    def __init__(self,id_input=None, name=None):
        self.name = name
        self.id = id_input
        self.articles = []
        Journal.all_journals.append(self)

    def add_self_to_database(self):
        cursor.execute('''
        INSERT INTO journals (name)
        VALUES (?)
        ''', (self.name,))
        connection.commit()
        all_journals = cursor.execute('''
        SELECT * FROM journals
        ''').fetchall()
        self.id = all_journals[-1][0]


    @classmethod
    def get_from_database(cls):
        all_journals = cursor.execute('''
        SELECT * FROM journals;
        ''').fetchall()
        for journal in all_journals:
            Journal(journal[0],journal[1])

class Author:
    all_authors = []
    def __init__(self,id_input,name):
        self.name = name
        self.id = id_input
        self.articles = []
        Author.all_authors.append(self)

    def submitArticle(self,topic, date, journal):
        new_article = Article(topic,date,self,journal)
        self.articles.append(new_article)
        journal.articles.append(new_article)
        return new_article
    
    @classmethod
    def get_from_database(cls):
        all_authors = cursor.execute('''
        SELECT * FROM authors;
        ''').fetchall()
        for author in all_authors:
            Author(author[0],author[1])

class Article:
    all_articles = []
    def __init__(self, id_input, topic, date, author, journal):
        self.id = id_input
        self.author = author
        self.journal = journal
        self.topic = topic
        self.date = date
        Article.all_articles.append(self)

    @classmethod
    def get_from_database(cls):
        all_articles = cursor.execute('''
        SELECT * FROM articles;
        ''').fetchall()
        for article in all_articles:
            actual_author = None
            for author in Author.all_authors:
                if author.id == article[3]:
                    actual_author = author
            actual_journal = None
            for journal in Journal.all_journals:
                if journal.id == article[4]:
                    actual_journal = journal
            Article(
                id_input=article[0],
                topic=article[1],
                date = article[2],
                author=actual_author,
                journal=actual_journal
                )
        
def get_all_from_database():
    Journal.get_from_database()
    Author.get_from_database()
    Article.get_from_database()

    # print(Article.all_articles[0].journal.name)
    # print(Journal.all_journals)
    # print(Author.all_authors)
get_all_from_database()

j3 = Journal(name="Test Journal 3")
j3.add_self_to_database()
print(j3.id)
# Article.get_from_database()
# print(Article.all_articles)
# journal = Journal("Test Journal")
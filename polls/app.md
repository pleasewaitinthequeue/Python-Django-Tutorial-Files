# What to Expect in 'App' Folder

## Index
1. [Project Root](../README.md)
2. [/Project/Project](../mysite/project.md)
3. [/Project/App (that's where we are!)](./app.md)

### URLs ([urls.py](./urls.py))
In the previous [urls.py](../mysite/urls.py) file routing for the project was negotiated.  In this folder we are dealing with routing for just the 'App' level.  The app_name will determine the base level route used to trigger the default path.  Defined at '' it is called 'index'.  Notice how it also directs us to [views.IndexView](./views.py).  All of the routing for our app is going to be determine here.

```
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```

We have four views defined above:
- The **Default View**
  - Called by /polls
  - Renders a list of all Questions in the Database
- The **Question View**
  - Called by /polls/:id
  - Renders the Question and all of its Choices
- The **Results View**
  - Called by /polls/:id/results
  - Shows how all votes are tallied
- The **Voting View**
  - Called by /polls/:id/vote
  - Takes the User Input and Saves it
  - Throws an Error if the User didn't make a choice

### Model View Template (MVT)

#### [models.py](./models.py)

Our polls app has two basic objects.  First we import the libraries that we need.  A couple of our fields are dates, so we need datetime, and models, and we would also like to localize the timezone to the server's timezone, so we need that library too.
```
import datetime

from django.db import models
from django.utils import timezone
```
**Questions** and **Choices**.  They include the following Relational and Computed Fields:

##### Question
- question_text: character field
- pub_date:  date time field
- a function that returns the string of question_text by default
- was_published_recently
  - admin_order_field: organizes objects in the admin view
  - boolean: the value used in our app
  - short_description: identifies the field to the admin view

```
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
```
##### Choice
- question:  foreign key linking it to Question
- choice_text:  character field
- votes:  integer field to count the number of votes
- a function that returns the choice_text by default

```
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
```

#### views.py
Rather than exhaustively explain all views, we are just going to focus on the Index View.

```
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question
```
```
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
```
The first thing that polls does after loading the imports is to name its template.  Next it pulls data from our project's database using the information we gave it in settings.py.  Note that we are using djangoey syntax to specify the following approximate SQL Code:
```
  select
    top(5) *
  from questions
  where pub_date < sysdate
  order by pub_date desc;
```
```
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
```

#### template
The index view identifies a template:  [./templates/polls/index.html](./templates/polls/index.html).  The .html file is written in a hybrid syntax that allows for markers that django can find.  Note how the {% %} and {{ }} characters separate HTML from Python Syntax.  This allows for us to write and customize templates for our Views.
```
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}">
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
Notice above that we have done conditional handling for No Data or Some Data.  Our View is defined as a Class so that it can be imported into our urls.py file.  In our Views File we have imported our data model from [./models.py](./models.py).

### So What?

When we open our Oracle Database, we have two tables, **polls_question** and **polls_choice**.  Export those tables as SQL Setup Statements we get the following:
#### polls_question SQL
```
CREATE TABLE "SYSTEM"."POLLS_QUESTION"
  (	"ID" NUMBER(11,0) GENERATED BY DEFAULT ON NULL
    AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999
    INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL ENABLE,
 "QUESTION_TEXT" NVARCHAR2(200),
 "PUB_DATE" TIMESTAMP (6) NOT NULL ENABLE,
  PRIMARY KEY ("ID")
 USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
 STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
 PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
 TABLESPACE "SYSTEM"  ENABLE
  ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
NOCOMPRESS LOGGING
 STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
 PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
 TABLESPACE "SYSTEM" ;
 ```
#### polls_choice
```
  CREATE TABLE "SYSTEM"."POLLS_CHOICE"
   (	"ID" NUMBER(11,0) GENERATED BY DEFAULT ON NULL
    AS IDENTITY MINVALUE 1 MAXVALUE 9999999999999999999999999999
    INCREMENT BY 1 START WITH 1 CACHE 20 NOORDER  NOCYCLE  NOKEEP  NOSCALE  NOT NULL ENABLE,
	"CHOICE_TEXT" NVARCHAR2(200),
	"VOTES" NUMBER(11,0) NOT NULL ENABLE,
	"QUESTION_ID" NUMBER(11,0) NOT NULL ENABLE,
	 PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM"  ENABLE,
	 CONSTRAINT "POLLS_CHO_QUESTION__C5B4B260_F" FOREIGN KEY ("QUESTION_ID")
	  REFERENCES "SYSTEM"."POLLS_QUESTION" ("ID") DEFERRABLE INITIALLY DEFERRED ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;

  CREATE INDEX "SYSTEM"."POLLS_CHOI_QUESTION_I_C5B4B260"
  ON "SYSTEM"."POLLS_CHOICE" ("QUESTION_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "SYSTEM" ;
```
While we might ahve written the SQL Create Table Statement by hand - we may not have thought to create an index afterwards.

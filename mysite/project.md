# What to Expect in 'Project' Folder

## Index
1. [Project Root](../README.md)
2. [/Project/Project (that's where we are!)](project.md)
3. [/Project/App](../polls/app.md)

## settings.py (Framework Configuration)
The file settings.py \[[/project/settings.py](settings.py)\] is used to set all of the project level specifications.  More about [Settings.py](https://docs.djangoproject.com/en/2.2/topics/settings/) is available on the Django Website.  A full list of settings and their values, is also available on the [Django Website](https://docs.djangoproject.com/en/2.2/ref/settings/).

The Settings.py file sets the following Attributes:
- **Base Path** for the Application
- **Secret Key** for the Production App
- A Debug Flag that is set to **True** which provides additional logging.
- List of **Allowed Hosts**
- Installed Django Dependencies and Middleware
- Root URL Definition
- A list of Templates Required to Support the Application
- The Project default **Web Server Gateway Interface (WSGI)** Application
- **Database Engine** Configuration and **Connection Information**
- Default Password Validation (for Admin App)
- **Internationalization / Localization** Information
- Static File Location Settings Including:
  - Cascading Style Sheets (CSS)
  - JavaScript
  - Image Assets

## urls.py (Project Routing Configuration)

The **urlpatterns** list routes URLs to specific views. For more information about urlpatterns, visit [Django Topics (URLs)](https://docs.djangoproject.com/en/2.2/topics/http/urls/).

Examples:
1. Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
1. Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
1. Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

```
# import supporting libraries
from django.contrib import admin
from django.urls import include, path
```
As a part of the tutorial we added to this configuration file in order to route to additional webpages.  Above, the supporting libraries from django help allow the path returns in the urlpatterns list.  Note that since polls is an app that we defined, we have to include its .urls file in the path definition.
```
# define url patterns
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## wsgi.py
[Web Server Gateway Interface (WSGI)](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) or 'whiskey' is calling convention for web servers to forward specific requests to python based applications.  Let's not worry about WSGI, other than that we need it to receive requests from the webserver.

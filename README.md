# Examus comments framework

**Comments framework for django sites**

# Requirements

* Python (3.5)
* Django (1.8)
* jQuery (2.1.4)

# Installation

Add `'comments'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'comments',
    )

Add `'comments.urls'` to your `urls.py`.

    urlpatterns = (
        ...
        url(r'^comments/', include('comments.urls')),
    )

# Example

Add `{% load comments %}` and jQuery to head of your html

    {% load comments %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://yastatic.net/jquery/2.1.4/jquery.min.js"></script>
    </head>

Add `{% comments_block %}` in place for comments

    <body>
    {% comments_block %}
    </body>

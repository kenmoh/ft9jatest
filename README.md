# PROOJECT SUMMARY

### Title: Stock PerformanceTracker.

### Description:

This application help stock traders tracks their profit or loss overtime on per minute interval.

### Features:

```
1. User Dashboard
1. Admin Dashboard
1. Line graph
```

### Technologies used:

```
1. Python: Programming Language
1. Django: Python web framework
1. MongoDB: NoSQL Database
```

```
In this project, we developed a simple stock trading performance tracker using the technologies above as part of the project requirements.

To communicate with MongoDB database, we used Djongo, which is an Object Document Mapper(ODM) similar to the built-in Django ORM. Although djongo is not the best, but it works fine for a project as little as this as it helps to still make use of the Django built-in admin.

Graph is a part of the project features, so we used Pyplot(Python library for plotting and displaying graph) to plot and display the chart to the user. It’s easy to use and it fits well for this project hence, the choice.
To give it a little bit of styles, we used bootstrap
```

### LIMITATIONS

```
Django wasn’t built with NoSQL databases in mind, so using Django with MongoDB always take lots of work around. Libraries like Mongoengine and PyMongo can also be used, but you’d loose the Django ORM and Django Admin (two powerful features of Django) with these options. Using Djongo will affect performance as what it does is to conver SQL queries to MongoDB queries. Djongo is still very unstable and has lots of issues on github and aslo does not support Django version greater than 3.0.5.
Frameworks such as FastAPI, Flask, Litestar will be a good fit to pair with MongoDB.

```

### ADMIN LOGIN

```
username: admin
password: admin
```

### RUN TEST

```
python manage.py test
```

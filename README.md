
# Goals
The goal of this session is to distinguish between the three layers of a backend api

# Database / data storage
A populated and schemad database - the data is the ground source of all truth for the universe.
This is really the most important bit.

The simplest database I can think of is a dictionary

This of course is deleted on restarting / cleared from ram

We use mongo (other databases exist)

We shall be using shelve for this tutorial (basically an on disk dictionary, not so different from an s3 file

# API to serve it up

There are only really two types of api that should be used in this day and age.
REST and GraphQL (with lambdas being a good way of serving things up too, but not an API as such)

There are many libraries available for both.

Today we shall be using strawberry.

# Server

There are many web servers available.
These include django, uvicorn and other asgi's, flask.
We shall start today by building with uvicorn (shipped with strawberry and we shall transition to chalice)

Chalice has serverless benefits. Uvicorn runs well on something like elastic beanstalk where you have a few
instances of the server permanently running


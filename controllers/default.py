# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return dict(message="Hello from MyApp", counter=session.counter)

def first():
    form = SQLFORM.factory(Field('visitor_name', requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)

def second():
    if not request.function=='first' and not session.visitor_name:
        redirect(URL('first'))
    return dict()

def workflow():
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return dict(message="Hello from MyApp", counter=session.counter)

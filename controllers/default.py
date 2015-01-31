# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def upload():
    import os
    import json

    imgData = json.loads(request.vars['data'])
    #imgData_length = len(imgData)
    #imgData_offset = imgData_length - (imgData_length % 4 if imgData_length % 4 else 4)
    #print imgData_length, imgData_offset
    #imgData = imgData.decode('base64')
    #imgData = base64.b64decode(imgData, '/+')

    imgData = imgData.decode('base64')
    #print imgData[:15]
    #print imgData[15:20]
    myfile = os.path.join(request.folder, 'static/images', 'imageToSave.png')

    fh = open(myfile, "wb")
    #fh.write(imgData[15:])
    fh.write(imgData)
    #fh.write(urllib.unquote(imgData).decode('base64'))
    fh.close()

    pass
    #return P()

def image_upload_test():
    return dict()

def fabric_test():
    return dict()

def kinetic_test():
    return dict()

def lightbox():
    return dict()

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)

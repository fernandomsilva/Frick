# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def test():
    return dict(test='foi')
	
def	overimages():
	return dict()

def open_state():
	import os
	import json
	from functions import readGroup

	filename = json.loads(request.vars['filename'])

	file = os.path.join(request.folder, 'static/states/user', filename + '.lightboxstate')

	file_contents = []
	filehandler = open(file, "r")
	for line in filehandler:
		file_contents.append(line[:-1])
	filehandler.close()
	
	result = []
	menu = True
	file_contents = file_contents[1:]
	#for element in file_contents[1:]:
	while (len(file_contents) > 3):
		print len(file_contents)
		element = file_contents[0]
		if (menu):
			if (element == "\\menu"):
				menu = False
				del file_contents[0]
			else:
				if (element[0] != "\\"):
					result.append(element)
					del file_contents[0]
				else:
					result.append(readGroup(file_contents, element))

	result.append(file_contents[1])
					
	return T(json.dumps(result))

def save_state():
	import os
	import json

	data = request.vars['data']
	filename = request.vars['filename']
	
	file = os.path.join(request.folder, 'static/states/user/', filename + '.lightboxstate')

	filehandler = open(file, "w")
    #for line in file_contents:
	filehandler.write(json.loads(data))
	filehandler.close()
	#filenames = []
	#for x in os.listdir(path):
	#	filenames.append([x[:-14], time.ctime(os.path.getmtime(path + x))])
	
	pass
	#return T(json.dumps(filenames))
	
def state_list():
	import os
	import time
	import json
	
	path = os.path.join(request.folder, 'static/states/user/')

	filenames = []
	for x in os.listdir(path):
		filenames.append([x[:-14], time.ctime(os.path.getmtime(path + x))])

	#result = ""
	#for x in filenames:
	#	result = result + "<tr><td><i class=\"fa fa-file-o\"></i>" + str(x[0]) + "</td><td style=\"text-align: center;\">" + str(x[1]) + "</td></tr>"
	
	return T(json.dumps(filenames))

def upload():
    import os
    import json

    imgData = json.loads(request.vars['data'])
    imgData = imgData.decode('base64')

    infofile = os.path.join(request.folder, 'static/images/user', 'info.txt')

    file_contents = []

    filehandler = open(infofile, "r")
    for line in filehandler:
        file_contents.append(line)
    filehandler.close()

    index = int(file_contents[0])
    file_contents[0] = str(index + 1) + '\n'

    imagefile = os.path.join(request.folder, 'static/images/user', str(index) + '.png')

    filehandler = open(imagefile, "wb")
    filehandler.write(imgData)
    filehandler.close()

    file_contents.append(str(index) + '\n')

    filehandler = open(infofile, "w")
    for line in file_contents:
        filehandler.write(line)
    filehandler.close()

    return T(str(index) + '.png')

def image_upload_test():
    return dict()

def fabric_test():
    return dict()

def kinetic_test():
    return dict()

def lightbox():
    import os
    import json

    infofile = os.path.join(request.folder, 'static/images/user', 'info.txt')

    file_contents = []

    filehandler = open(infofile, "r")
    for line in filehandler:
        file_contents.append(line[:-1] + '.png')
    filehandler.close()

    return dict(image_list=' '.join(file_contents[1:]))

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

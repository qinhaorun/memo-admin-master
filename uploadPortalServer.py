import pymysql
import sys
from resttest import app
import flask
from flask import Flask
from os import urandom

from flask_cors import CORS, cross_origin

from configdb import mysql
from configdb import mySQLConnectionPool

from flask import jsonify
from flask import flash, request
from datetime import datetime
from datetime import timezone
import json
import random
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from bs4 import BeautifulSoup 

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import hashlib


from os import listdir
from os.path import isfile, join

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4
import requests
# firebase init
servicekey = {'type': 'service_account', 'project_id': 'sixdegreestest2-f5666', 'private_key_id': '9fd6b042e0ca7ed9da86b802190bedcf521bab19', 'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDbhN1852ldP8km\nYDfX9nTvh+hhZ7sLn9FoAUvfNOVuYYz4G8fH4lybeCIw1A4nhleNiQehmrREKiY+\n6IzSQxHWjhn64vDJEHSFOaONeGKy1ekmWk48BslXfnzzRAhPv2UGkNEEwSEAlKuu\nB5qlV4WnxOjTlDJiJ6THOE2h7sVNnpl7KGVjjixCl6/yjLbRJ1F/swgftPM3Vsa2\neyUkoxY9POe8cxU2wEGxFT5vRjXYbLqY4CIrJ2O2hl0cSAk/gmqpMdMnVMvez40V\nmV9fq2l0gvv43+64AwpKN+D2HUhhxuQ0UgOmJVUj7h8D6aWpiBZIeYvYWXVKdO5v\nGC5O03yLAgMBAAECggEAB8ju9+fXBz0PW6KMPcbvlQe7WH+kFQCecwifZwjfsr9C\nj2agz6MPSLOFIY6A+qrbfllOjCR0jHmi20FGWTXoCIqykNYCgbGT3Z5SgV5fFbDb\nW1usLER2AyR+YZGB6p4YLZhDfrPWAUjEdoquKSXw8fxcNhX/3BZEKY0tckw0SBEt\nKHVCUSA+FK45KWte4k71rds1KlUj4I+FU/KVlfcwjFcW3wE6txAOyvPZAKHHVTVO\nfK0zt8yRYOGJCfiKh1hNBx50Ja/j6goidJNh3pd/cDAV7wma2wUP7wHb6td1z1j0\n/AcR1TI2s6BdHMqJ8gRYkY23pcE9hmek/By9iv5m7QKBgQD3/tfmD5HmDn0ZYldM\nd5k7huXjQbeWwlwAZRFFRBWl8WdtweIM924s70eMSLCle5aXL2pFdzukf2qMcbTb\nwYVcMpgd8Tsaz1ITtUSAJrvU2jMa1DgIfTJmL2gV7ZMdrQRufo6TJuRP7t7s4r4N\nS1ZI4gZ/y9PY/u7TUdvEbuxpLQKBgQDimrlh0kMvpnVBqTVdGBb/+yniqhOpQyrr\n05lAnhEZeo7LPRDezMY/PGZmvS3mrsCL3rDpm7ZOW1/33A8OcXgIAplr6U4vE49p\nCHO8zefsBUyBr+63n7NKv98X7jpipS5eB7TzvqNyrJ3iIJ8KN5MEGWgjg2a4XdOI\ndj8mcFkflwKBgCqBmr3LE2XMO/L64R2xLil+0K5oGDCV9bD3ocMujUtZGjI81iME\n0fSPusK3vtdOXJxjOyLW8fkbAcc6whYckGAiJ+KR82CAAoBwRGJ2wSEVmUbS8xu5\nYccT/xIrG1kty6GovYVJWD6/IaSWpJ6guBRb8WM8K355C7RaxoFfxdOtAoGAfWRS\n2u+H4BFDZ08jyVzwNTwdpGCquooBcTfI4PnWynuIEqy67h7wQMPCgm2CvdjLkVps\nGQjiK5/ijfxGlJ5zZjNSBGW4rtIrFFrp+HsUMAWKnWTmOtPzWZSs9cgMpNN0wfGP\nzyUZuvYL87pLZ1LzVlxcxPIMYE8DI8sTDMk0eAcCgYAdipj5H2xAGW3T1/iy23Eb\nCEBAT0i+zehCLN5mn0OUGKOiPc9XTN71gIHNz7VATkCQa19lHZajDgjVJJbNPH9w\najyNB5eSOW5p0krOWh6TTWl7uN3J5/rxLIleRKJmZ4k9eFEcVqbut3mu27Z9FoXi\nIEye6Lnd/GvxFbzlOYMgJg==\n-----END PRIVATE KEY-----\n', 'client_email': 'firebase-adminsdk-39aem@sixdegreestest2-f5666.iam.gserviceaccount.com', 'client_id': '116727891677568526628', 'auth_uri': 'https://accounts.google.com/o/oauth2/auth', 'token_uri': 'https://oauth2.googleapis.com/token', 'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs', 'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-39aem%40sixdegreestest2-f5666.iam.gserviceaccount.com'}

# cred = credentials.Certificate(servicekey)
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'sixdegreestest2-f5666.appspot.com'
# })

# bucket = storage.bucket()

# input filename first. This is unique globally 


# def urlFromUploadFilename( filename ):
# 	blob1 = bucket.blob('/AvatarAssets/' + filename)
# 	new_token = uuid4()
# 	metadata  = {"firebaseStorageDownloadTokens": new_token}
# 	blob1.metadata = metadata
# 	with open(os.path.join(mypath, filename ), 'rb') as my_file:
# 		blob1.upload_from_file(my_file)
# 		blob1.make_public()
# 		blob1.public_url
# 		url = blob1.public_url + "?alt=media&token=" + str(new_token)
# 	return url



def updateFileMap(filename, url, avatarId):
	try:
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sqlquery = "INSERT INTO avatarfilemap(filename, fileurl, aid) VALUES(%s, %s, %s)"
		binddata = ( filename, url, avatarId )
		cursor.execute( sqlquery, binddata )
		conn.commit()
	except Exception as e:
		raise e


def delFileMap( filename ):
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "DELETE FROM avatarfilemap WHERE filename = %s"
	cursor.execute( sqlquery, filename )
	conn.commit()


def checkFileMapExist( filename ):
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "SELECT * FROM avatarfilemap WHERE filename = %s"
	cursor.execute( sqlquery, filename )
	ret = cursor.fetchone()
	if( ret == None ):
		return False
	else:
		return True


def checkIdExist( filename, avatarId ):
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "SELECT * FROM avatarfilemap WHERE aid = %s LIMIT 1"
	cursor.execute( sqlquery, avatarId )
	ret1 = cursor.fetchone()
	sqlquery = "SELECT * FROM avatarfilemap WHERE filename = %s LIMIT 1"
	cursor.execute( sqlquery, filename )
	ret2 = cursor.fetchone()
	if( (ret1 == None) and (ret2 == None) ):
		return 0
	elif ret1 != None:
		return 1
	else:
		return 2





def parseAndUploadPostures(mypathFileUrlList, fileUniqueName, avatarId):
	# parse and upload postures
	# without the preview. 
	# will overwrite existing db postures
	ReservedAnimations = ["a", "e", "i", "o", "u"]
	jsonName = fileUniqueName + ".json"
	jsonUrl = mypathFileUrlList[jsonName]
	jsondata = requests.get(jsonUrl)
	dat = json.loads(jsondata.content)
	keylist = list(dat.keys())
	if "animations" not in keylist:
		return False
	animationJson = dat["animations"]
	animations = list(animationJson.keys())
	Postures = [ x for x in animations if x not in ReservedAnimations ]
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "DELETE FROM avatar_postures WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	for pos in Postures:
		sqlquery = "INSERT INTO avatar_postures(posture_name, posture_name_disp, aid) VALUES (%s, %s, %s)"
		binddata = (pos, pos, avatarId)
		cursor.execute( sqlquery, binddata )
	return True


def parseAndUploadAccls(mypathFileUrlList, fileUniqueName, avatarId):
	# parse and upload skins
	# without the preview
	# will overwrite existing db skins. 
	# jsonpath = join(mypath, fileUniqueName) + ".json"
	jsonName = fileUniqueName + ".json"
	jsonUrl = mypathFileUrlList[jsonName]
	jsondata = requests.get(jsonUrl)
	dat = json.loads(jsondata.content)
	keylist = list(dat.keys())
	if "skins" not in keylist:
		return False
	skinJson = list(dat["skins"])
	skinls = [ x["name"] for x in skinJson ]
	# delete all existing skin ls. 
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "DELETE FROM avatar_accessories WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	for sk in skinls:
		sqlquery = "INSERT INTO avatar_accessories(aid, acc_type, acc_name, acc_name_disp) VALUES (%s, %s, %s, %s)"
		acctype = sk.split("/")[0]
		binddata = (avatarId, acctype, sk, sk )
		cursor.execute( sqlquery, binddata )
	return True





def uploadFromSingleFilename(mypathFileUrlList, fileUniqueName, avatarId):
	# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.startswith(fileUniqueName)]
	# print(onlyfiles)
	# check file exists 
	upload_map = {}
	for item in list(mypathFileUrlList.keys()):
		url = mypathFileUrlList[item]
		upload_map[item] = url
		if( checkFileMapExist( item ) ):
			delFileMap(item)
		updateFileMap(item, url, avatarId )
	return True
	# print( upload_map )




def deleteAvatarById(avatarId):
	try:
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sqlquery = "DELETE FROM avatar WHERE aid = %s"
		cursor.execute( sqlquery, avatarId )
		sqlquery = "DELETE FROM avatar_accessories WHERE aid = %s"
		cursor.execute( sqlquery, avatarId )
		sqlquery = "DELETE FROM avatar_postures WHERE aid = %s"
		cursor.execute( sqlquery, avatarId )
		sqlquery = "DELETE FROM avatarfilemap WHERE aid = %s"
		cursor.execute( sqlquery, avatarId )
		return True
	except Exception as e:
		return False




def uploadMainAvatarEntry(mypathFileUrlList, fileUniqueName, avatarId):
	jsonname = fileUniqueName + ".json"
	atlasname = fileUniqueName + ".atlas"
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sqlquery = "DELETE FROM avatar WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	# upload to main entry
	sqlquery = "INSERT INTO avatar(aid, jsonName, atlasName, avatar_name) VALUES (%s, %s, %s, %s)"
	binddata = ( avatarId, jsonname, atlasname, fileUniqueName )
	cursor.execute( sqlquery, binddata )



def getAllAvatarMetas(avatarId):
	conn = mySQLConnectionPool.connection()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	# get main
	sqlquery = "SELECT * FROM avatar WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	ret_main = cursor.fetchone()
	# get postures
	sqlquery = "SELECT * FROM avatar_postures WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	ret_pos = list(cursor.fetchall())
	# get acc 
	sqlquery = "SELECT * FROM avatar_accessories WHERE aid = %s"
	cursor.execute( sqlquery, avatarId )
	ret_acc = list(cursor.fetchall())
	# get filemap 
	sqlquery = "SELECT * FROM avatarfilemap WHERE aid = %s"
	cursor.execute( sqlquery, avatarId ) 
	ret_file = list(cursor.fetchall()) 
	response = {}
	response['status_code'] = 200
	response['ret_main'] = ret_main
	response['ret_pos'] = ret_pos
	response['ret_acc'] = ret_acc
	response['ret_file'] = ret_file
	return response



def uploadAvatarMainBundle(mypathFileUrlList, fileUniqueName, avatarId):
	uploadFromSingleFilename(mypathFileUrlList, "bayc", 1)
	uploadMainAvatarEntry(mypathFileUrlList, "bayc", 1)
	parseAndUploadAccls(mypathFileUrlList, "bayc", 1)
	parseAndUploadPostures(mypathFileUrlList, "bayc", 1)
	res = getAllAvatarMetas(avatarId)
	return res


# mypath = "/Users/lmt/Desktop/skin/withmouths/bayc/"
# fileUniqueName = "bayc"
# avatarId = 1
# uploadAvatarMainBundle(mypath, fileUniqueName, avatarId)


@app.route( '/upload_avatar_bundle', methods = ['POST'] )
def upload_avatar_bundle():
	try:
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		_json = request.json
		loginemail = _json['loginemail']
		fileurlList = _json['urlList']
		avatarId = _json['avatarId']
		fileUniqueName = _json['fileUniqueName']
		if fileurlList and loginemail and avatarId != None and fileUniqueName and request.method == 'POST':
			res = uploadAvatarMainBundle( fileurlList, fileUniqueName, avatarId )
			if res:
				response = {}
				response['message'] = "upload_avatar_bundle succeeded. "
				response['status_code'] = 200
				response['data'] = res
				return response
			else:
				response = {}
				response['message'] = "upload_avatar_bundle err. "
				response['status_code'] = 202
				return response
		else:
			response = {}
			response['message'] = "upload_avatar_bundle data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route( '/create_avatar_metadata', methods = ['POST'] )
def create_avatar_metadata():
	try:
		_json = request.json
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		skeletonName = _json['skeletonName']
		defaultAnimationName = _json['defaultAnimationName']
		defaultSkinName = _json['defaultSkinName']
		avatar_name = _json['avatar_name']
		profile_photo = _json['profile_photo']
		profile_posture = _json['profile_posture']
		fileUniqueName = _json['fileUniqueName']
		if avatarId and fileUniqueName and loginemail and request.method == 'POST':
			exist = checkIdExist( fileUniqueName, avatarId )
			if exist != 0:
				response = {}
				response['message'] = "avatarId not unique. " if exist == 2 else "fileUniqueName not unique. "
				response['status_code'] = 202
				return response
			sqlquery = "INSERT INTO avatar(skeletonName, defaultAnimationName, defaultSkinName, avatar_name, profile_photo, profile_posture, aid, fileUniqueName) VALUES( %s, %s, %s, %s, %s, %s,%s, %s ) "
			binddata = ( skeletonName, defaultAnimationName, defaultSkinName, avatar_name, profile_photo, profile_posture, avatarId, fileUniqueName )
			cursor.execute( sqlquery, binddata )
			conn.commit()
			response = {}
			response['message'] = "create_avatar_metadata succeeded. "
			response['status_code'] = 200
			return response
		else:
			response = {}
			response['message'] = "create_avatar_metadata data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()



@app.route( '/update_avatar_metadata', methods = ['POST'] )
def update_avatar_metadata():
	try:
		_json = request.json
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		skeletonName = _json['skeletonName']
		defaultAnimationName = _json['defaultAnimationName']
		defaultSkinName = _json['defaultSkinName']
		avatar_name = _json['avatar_name']
		profile_photo = _json['profile_photo']
		profile_posture = _json['profile_posture']
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if avatarId and loginemail and profile_posture and profile_photo and defaultAnimationName and defaultSkinName and request.method == 'POST':
			sqlquery = "UPDATE avatar SET skeletonName = %s, defaultAnimationName = %s, defaultSkinName = %s, avatar_name = %s, profile_photo = %s, profile_posture = %s WHERE aid = %s"
			binddata = ( skeletonName, defaultAnimationName, defaultSkinName, avatar_name, profile_photo, profile_posture, avatarId )
			cursor.execute( sqlquery, binddata )
			conn.commit()
			response = {}
			response['message'] = "update_avatar_metadata succeeded. "
			response['status_code'] = 200
			return response
		else:
			response = {}
			response['message'] = "update_avatar_metadata data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()






@app.route( '/update_avatar_skinpreview', methods = ['POST'] )
def update_avatar_skinpreview():
	try:
		_json = request.json
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		acc_name = _json['acc_name']
		acc_type = _json['acc_type']
		acc_name_disp = _json['acc_name_disp']
		acc_url = _json['acc_url']
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if avatarId and acc_name and loginemail and request.method == 'POST':
			sqlquery = "UPDATE avatar_accessories SET acc_type = %s, acc_name_disp = %s, acc_url = %s WHERE aid = %s AND acc_name = %s"
			binddata = ( acc_type, acc_name_disp, acc_url, avatarId , acc_name )
			cursor.execute( sqlquery, binddata )
			conn.commit()
			response = {}
			response['message'] = "update_avatar_skinpreview succeeded. "
			response['status_code'] = 200
			return response
		else:
			response = {}
			response['message'] = "update_avatar_skinpreview data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()



@app.route( '/update_avatar_pospreview', methods = ['POST'] )
def update_avatar_pospreview():
	try:
		_json = request.json
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		posture_name = _json['posture_name']
		posture_name_disp = _json['posture_name_disp']
		posture_preview_url = _json['posture_preview_url']
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if avatarId and posture_name and loginemail and request.method == 'POST':
			sqlquery = "UPDATE avatar_postures SET posture_name_disp = %s, posture_preview_url = %s WHERE aid = %s AND posture_name = %s"
			binddata = ( posture_name_disp, posture_preview_url, avatarId , posture_name )
			cursor.execute( sqlquery, binddata )
			conn.commit()
			response = {}
			response['message'] = "update_avatar_pospreview succeeded. "
			response['status_code'] = 200
			return response
		else:
			response = {}
			response['message'] = "update_avatar_pospreview data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()





@app.route( '/get_existing_aid_meta', methods = ['POST'] )
def get_existing_aid_meta():
	try:
		_json = request.json
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		fileUniqueName = _json['fileUniqueName']
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if loginemail and avatarId and fileUniqueName and request.method == 'POST':
			res = getAllAvatarMetas(avatarId)
			response = {}
			response['message'] = "get_existing_aid_meta succeeded. "
			response['status_code'] = 200
			response['res'] = res
			return res
		else:
			response = {}
			response['message'] = "get_existing_aid_meta data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()





@app.route( '/delete_byaid', methods = ['POST'] )
def delete_byaid():
	try:
		_json = request.json
		loginemail = _json['loginemail']
		avatarId = _json['avatarId']
		fileUniqueName = _json['fileUniqueName']
		conn = mySQLConnectionPool.connection()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if loginemail and avatarId and fileUniqueName and request.method == 'POST':
			res = deleteAvatarById(avatarId)
			response = {}
			response['message'] = "delete_byaid succeeded. " if res else "delete_byaid error"
			response['status_code'] = 200 if res else 202
			return response
		else:
			response = {}
			response['message'] = "delete_byaid data incomplete. "
			response['status_code'] = 201
			return response 
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()







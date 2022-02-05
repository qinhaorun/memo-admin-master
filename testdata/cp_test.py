import requests
import json

# 1. upload meta data =============================================
datajson = {
     "loginemail": "_sys",
	"avatarId": 1,
	"fileUniqueName": "bayc",
	"skeletonName": "",
	"defaultAnimationName": "",
	"defaultSkinName": "default",
	"avatar_name": "BAYC",
	"profile_photo": "",
	"profile_posture": ""
}

pref = "https://memology-demo.herokuapp.com/"
path = pref + "create_avatar_metadata"
r = requests.post(path, json=datajson, headers={})

# parse result 202 & 201 means file existed before. delete them. 
b'{"message":"fileUniqueName not unique. ","status_code":202}\n'
b'{"message":"create_avatar_metadata succeeded. ","status_code":200}\n'

# 1.1 delete all avatar data by aid =============================================
pref = "https://memology-demo.herokuapp.com/"
path = pref + "delete_byaid"

datajson = {
	"loginemail": "_sys",
	"avatarId": 1,
	"fileUniqueName": "bayc"
}
r = requests.post(path, json=datajson, headers={})

# result 
r.content
b'{"message":"delete_byaid succeeded. ","status_code":200}\n'



# 2. upload files =============================================
retdata = {"bayc.atlas": "https://storage.googleapis.com/sixdegreestest2-f5666.appspot.com//AvatarAssets//Users/lmt/Desktop/skin/withmouths/bayc/bayc.atlas?alt=media&token=3f6b50f1-6c9f-4741-93a3-a5e4648f27c9", "bayc.json": "https://storage.googleapis.com/sixdegreestest2-f5666.appspot.com//AvatarAssets//Users/lmt/Desktop/skin/withmouths/bayc/bayc.json?alt=media&token=94bc17aa-e72d-480f-8cbd-b7cb1aa786d7", "bayc.png": "https://storage.googleapis.com/sixdegreestest2-f5666.appspot.com//AvatarAssets//Users/lmt/Desktop/skin/withmouths/bayc/bayc.png?alt=media&token=502820c8-57ab-4d64-a5b6-9b34d0b3c749", "bayc_2.png": "https://storage.googleapis.com/sixdegreestest2-f5666.appspot.com//AvatarAssets//Users/lmt/Desktop/skin/withmouths/bayc/bayc_2.png?alt=media&token=885ad764-64b6-4ebd-91ac-227b2065a587", "Screen Shot 2022-01-30 at 12.03.23 PM.png": "https://firebasestorage.googleapis.com/v0/b/sixdegreestest2-f5666.appspot.com/o/Screen%20Shot%202022-01-30%20at%2012.03.23%20PM.png?alt=media&token=9b625278-6d7e-4d64-b39c-ddcf529c11fa"}

datajson = {
	"loginemail": "_sys",
	"urlList": retdata,
	"avatarId": 1,
	"fileUniqueName": "bayc"
}
pref = "https://memology-demo.herokuapp.com/"
path = pref + "upload_avatar_bundle"
r = requests.post(path, json=datajson, headers={})

# parse result 
a = json.loads( r.content )

# check for four tables, and update. 
a["data"].keys()
# 'ret_acc'   skins
# 'ret_file'  current files uploaded. 
# 'ret_main'  meta data
# 'ret_pos'   postures



# 3. update previews and names for postures =============================================

datajson = {
	"loginemail": "_sys",
	"avatarId": 1,
	"posture_name": "1",
	"posture_name_disp": "posture desp",
	"posture_preview_url": ""
}
pref = "https://memology-demo.herokuapp.com/"
path = pref + "update_avatar_pospreview"
r = requests.post(path, json=datajson, headers={})

r.content
b'{"message":"update_avatar_pospreview succeeded. ","status_code":200}\n'


# 4. update previews and names for skins =============================================

datajson = {
	"loginemail": "_sys",
	"avatarId": 1,
	"acc_name": "cap/badgelol",
	"acc_type": "posture desp",
	"acc_name_disp": "acc disp",
	"acc_url" : ""
}
pref = "https://memology-demo.herokuapp.com/"
path = pref + "update_avatar_skinpreview"
r = requests.post(path, json=datajson, headers={})

# result
r.content
b'{"message":"update_avatar_skinpreview succeeded. ","status_code":200}\n'



# ======= check existing all avatar data ======== 

datajson = {
	"loginemail": "_sys",
	"avatarId": 1,
	"fileUniqueName": "bayc"
}
pref = "https://memology-demo.herokuapp.com/"
path = pref + "get_existing_aid_meta"
r = requests.post(path, json=datajson, headers={})

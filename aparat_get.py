import pandas as pd
import sklearn
import numpy as np
import json
import requests

base='https://www.aparat.com//etc/api/'
get=lambda x:requests.get(base+x).json()
some_videos=lambda :pd.DataFrame({
    'id':[],
    'title':[],
    'username':[],
    'userid':[],
    'visit_cnt':[],
    "uid":[],
    "process":[],
    "big_poster":[],
    "small_poster":[],
    "duration":[],
    "sdate":[],
    "frame":[],
    "official":[],
    "autoplay":[],
    "360d":[]
})

one_video=lambda :pd.DataFrame({
    'id':[],
    'title':[],
    'username':[],
    'userid':[],
    'visit_cnt':[],
    "uid":[],
    "process":[],
    "sender_name":[],
    "big_poster":[],
    "small_poster":[],
    "profilePhoto":[],
    "duration":[],
    "sdate":[],
    "frame":[],
    "official":[],
    "tags":[],
    "description":[],
    "cat_id":[],
    "cat_name":[],
    "autoplay":[],
    "360d":[],
    "has_comment":[],
    "has_comment_txt":[],
    "size":[],
    "watch_action":[],
    "cost_type":[],
    "can_download":[],
    "like_cnt":[]
})

one_chanel_data=lambda :pd.DataFrame({
    "pic_s":[],
    "pic_m":[],
    "pic_b":[],
    "username":[],
    "name":[],
    "video_cnt":[],
    "url":[],
    "follower_cnt":[],
    "followed_cnt":[],
    "descr":[],
    "official":[],
    "cloob":[],
    "lenzor":[],
    "facebook":[],
    "twitter":[],
    "follow_link":[],
    "follow_status":[],
    "cover_src":[],
    "profile_videos":[]
})

one_chanel_page=lambda :pd.DataFrame({
    "cat_id":[],
    "cat_name":[],
    "cat_cnt":[],
    "link":[],
    "data":[]
})

one_profile_data=lambda :pd.DataFrame({
    "id":[],
    "username":[],
    "name":[],
    "pic":[],
    "ltoken":[],
    "banned":[],
    "email":[],
    "mobile_number":[],
    "mobile_valid":[],
    "pic_s":[],
    "pic_m":[],
    "pic_b":[],
})

form_action=lambda :pd.DataFrame({
    "formAction":[],
    "frm-id":[],
})

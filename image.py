# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys, json

for line in sys.stdin:
  try:
    tweet = json.loads(line)
    #リツイート除外
    if 'retweeted_status' not in tweet:
       #日本語に限定
       if tweet['user']['lang'] == 'ja':
          #画像つきに限定
          if tweet['entities']['media'][0] is None:
              pass
          else:
             screenName = tweet['user']['screen_name']
             bio = tweet['user']['description'].encode('utf-8').replace("\n", "").replace(",", "")
             text = tweet['text'].encode('utf-8').replace("\n", "").replace(",", "")
             imageUrl = tweet['entities']['media'][0]['media_url_https']
              
             print screenName,',',
             print bio,',',
             print text,',',
             print imageUrl
          
  except StandardError:
    pass

# Twitterからランダムで画像を取得
## 準備
twitter APIを使用するためにtweepyをインストールする。
```
sudo apt-get install python-pip
sudo pip install tweepy
```

https://apps.twitter.com/ で新しいアプリを作り，`auth.py`にOAuth認証に必要な4項目を追記する。

## 実行
ランダムサンプリングでツイートを集める（Ctrl+Cで止める）。
```
python stream.py > tweets
```

集めたツイートからスクリーンネーム、プロフィール文、本文、画像URLを抜き出す。
```
python image.py < tweets > result.csv
```

（最初から抜き出したものだけ集める場合）
```
python stream.py | python image.py > result.csv
```

画像URLのリストを作る。
```
cut -d ',' -f 4 result.csv > imageList.txt
```

画像URLリストから画像を保存する。
```
wget -i imageList.txt
```

# twitterAPI

ランダムサンプリングでツイートを集める。
```
python stream.py > tweets
```

集めたツイートからスクリーンネーム、プロフィール文、本文、画像URLを取り出す。
```
python image.py < tweets > image.csv
```

画像URLのリストを作る。
```
cut -d ',' -f 4 image.csv > imageList.txt
```

画像URLリストから画像を保存する。
```
wget -i imageList.txt
```

# Twitterからランダムで画像を取得

ランダムサンプリングでツイートを集める（Ctrl+Cで止める）。
```
python stream.py > tweets
```

集めたツイートからスクリーンネーム、プロフィール文、本文、画像URLを取り出す。
```
python image.py < tweets > result.csv
```

画像URLのリストを作る。
```
cut -d ',' -f 4 result.csv > imageList.txt
```

画像URLリストから画像を保存する。
```
wget -i imageList.txt
```

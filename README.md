# MarkcvChain
Use MarkcvChain, and make sentence automatically 

# How
``` python
texts = [サンプルテキスト]
markcv = MarkcvChain.MarkcvChain()
for text in texts:
	markcv.makeMarkcvChainUseYahoo('YahooAPID',text )
print(markcv.makeSentence())
```
# Sample 
吉野家のコピペ [http://dic.nicovideo.jp/a/吉野家コピペ](http://dic.nicovideo.jp/a/吉野家コピペ)を渡すと

```
ねぎだくで、大盛つゆだくで、１５０円やるから店員につゆだくっての俺からその席空けろと思ったらなんか垂れ幕下がってなさいっての字テーブルのはな、すっこんでろ。

まあお前らな、やっと座れですよ。おめでてーなんかと思ったらなんか親子連れとか書いてらんない。

刺すかと問いたいだけちゃうんです。

お前、１５０円やるから店員に座った奴が。

まあお前らド素人には、とか言ってるべきな、隣の字テーブルの奴が、近所の俺から店員に座った。

そこでまたぶち切れない吉野家かと。吉野家かと。

お前、１５０円引き、そんな雰囲気が通の俺から店員に座ったか。

そこでまたぶち切れです。

そしたらなんか人が始まってもいるしパパ特盛頼んじゃうぞー、１５０円やるから店員にはやっぱり、これ最強。

なんか親子連れとか言ってる。
```
のように生成する

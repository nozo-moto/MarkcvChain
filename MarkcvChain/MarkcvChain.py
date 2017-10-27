import pickle
import random
import re
START = "START"
END = "EOS"


class MarkcvChain:
    def __init__(self):
        self.ngram = {START: []}

    def makeMarkcvChainUseMeCab(self, scentence: str):
        """

        :type scentence: str
        """
        import MeCab
        t = MeCab.Tagger()
        self.textdata = t.parse(scentence)
        self.wordlist = self.parseText()
        self.makengram()

    def makeMarkcvChainUseYahoo(self, appid: str, scentence: str):
        from yahooparse import YahooParse
        yahoo = YahooParse(appid)
        self.wordlist = yahoo.parse(scentence)
        self.wordlist.append(END)
        self.makengram()

    def getNgram(self):
        return self.ngram

    def parseText(self) -> list:
        word = [i.split("\t")[0] for i in self.textdata.split("。",)]
        return word

    def makengram(self) -> dict:
        for index, word in enumerate(self.wordlist):
            if len(word) == 0:
                return self.ngram
            if index == 0 and word != END:
                self.ngram[START].append(word)
            elif END in word:
                return self.ngram
            if word in self.ngram:
                self.ngram[word].append(self.wordlist[index + 1])
            else:
                self.ngram.update({word: [self.wordlist[index + 1]]})

    def makeSentence(self) -> str:
        scentencelist = []
        scentencelist.append(random.choice(self.ngram[START]))
        while scentencelist[len(scentencelist)-1] != END:
            scentencelist.append(random.choice(self.ngram[scentencelist[len(scentencelist)-1]]))
        scentencelist.pop()
        scentence = "".join(scentencelist)
        return scentence

    def saveNgram(self, filename):
        with open(filename, mode='wb') as f:
            pickle.dump(self.ngramdata, f)

    def reloadNgram(self, filename):
        with open(filename, mode='rb') as f:
            pickle.load(f, self.ngramdata)

    def clearText(text: str)-> str:
        text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
        text = re.sub(r'http?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
        text = re.sub(r'@[a-z,A-Z,0-9]+', "", text)
        text = re.sub(r'#[a-z,A-Z,0-9]+', "", text)
        text = re.sub(r'RT', "", text)
        text = re.sub(r':', '', text)
        text = text.strip()
        return text


if __name__ == '__main__':
    mr = MarkcvChain()
    texts = [
        "昨日、近所の吉野家行ったんです。吉野家。",
        "そしたらなんか人がめちゃくちゃいっぱいで座れないんです。"
        "で、よく見たらなんか垂れ幕下がってて、１５０円引き、とか書いてあるんです。",
        "もうね、アホかと。馬鹿かと。",
        "お前らな、１５０円引き如きで普段来てない吉野家に来てんじゃねーよ、ボケが。",
        "１５０円だよ、１５０円。",
        "なんか親子連れとかもいるし。一家４人で吉野家か。おめでてーな。",
        "よーしパパ特盛頼んじゃうぞー、とか言ってるの。もう見てらんない。",
        "お前らな、１５０円やるからその席空けろと。",
        "吉野家ってのはな、もっと殺伐としてるべきなんだよ。",
        "Ｕの字テーブルの向かいに座った奴といつ喧嘩が始まってもおかしくない、",
        "刺すか刺されるか、そんな雰囲気がいいんじゃねーか。 d女子供は、すっこんでろ。",
        "で、やっと座れたかと思ったら、隣の奴が、大盛つゆだくで、とか言ってるんです。",
        "そこでまたぶち切れですよ。"
    ]
    for text in texts:
        # mr.makeMarkcvChainUseYahoo("APIKEY-", text)
        mr.makeMarkcvChainUseMeCab(text)
    print(mr.getNgram())
    print(mr.makeSentence())

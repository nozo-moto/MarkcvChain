import pickle
import random
import yahooparse
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
        t = MeCab.Tagger()
        self.textdata = t.parse(scentence)
        self.wordlist = self.parseText()
        self.makengram()

    def makeMarkcvChainUseYahoo(self, appid: str, scentence: str):
        yahoo = yahooparse.YahooParse(appid)
        self.wordlist = yahoo.parse(scentence)
        self.wordlist.append(END)
        self.makengram()

    def getNgram(self):
        return self.ngram

    def parseText(self) -> list:
        word = [i.split("\t")[0] for i in self.textdata.split("\n")]
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

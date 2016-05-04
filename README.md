# English-Korean Transliteration
영어-한글 표기 변환기(Transliteration)는 영어 단어를 한글 표기로 변환 하는 프로그램입니다. 데모 웹사이트 - [https://transliterator.herokuapp.com](https://transliterator.herokuapp.com)

동작 방법은 기계 학습으로 (영어단어, 한글표기) 쌍의 수많은 데이터를 학습한 결과대로 변환을 수행합니다. 이 프로그램 코드는 TensorFlow Tutorial - [Sequence-to-Sequence Models](https://www.tensorflow.org/versions/r0.8/tutorials/seq2seq/index.html#sequence-to-sequence-models) 의 번역기를 표기 변환기로 변경하여 구현되었습니다.

##### 참고
- 기계 학습으로 구현된 표기 변환기 예 : Google Map의 외국 지역명 표기 ([한글로 보는 세계 지도](http://googlekoreablog.blogspot.kr/2010/12/blog-post_4432.html))
- [내앱찾기](https://play.google.com/store/apps/details?id=net.muik.myappfinder) 앱에서 영어이름으로 되어 있는 앱을 한글 키워드로 검색할 수 있도록 활용 예정

##### 주 학습 데이터
- 국립국어원의 [외래어 표기법의 용례](http://www.korean.go.kr/front/foreignSpell/foreignSpellList.do?mn_id=96)
- 위키낱말사전의 [한국어 외래어](https://ko.wiktionary.org/wiki/%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EC%99%B8%EB%9E%98%EC%96%B4)

학습에 필요한 양질의 대량 데이터가 필요합니다. 수집 아이디어나 데이터가 있다면 추가 부탁드립니다~!

## Requirements
- Python 2.7
- [TensorFlow](https://www.tensorflow.org/) 0.8

## Run interactive console
If not train before, download pre-trained files automatically.
```bash
$ python translate.py --decode
Reading model parameters from train/translate.ckpt-32900
(Input any English word to transliterate Korean)
> super
슈퍼
> morning
(morning is not trained word)
모닝
> kakao
카카오
> gift
(gift is not trained word)
기프트
> 
```

## Run train
```bash
$ python translate.py
Preparing WMT data in data
Creating 2 layers of 128 units.
Created model with fresh parameters.
Reading development and training data (limit: 0).
global step 100 learning rate 0.5000 step-time 0.38 perplexity 240.07
  eval: bucket 0 perplexity 124.96
  eval: bucket 1 perplexity 136.77
  eval: bucket 2 perplexity 146.66
  eval: bucket 3 perplexity 142.27
global step 200 learning rate 0.5000 step-time 0.34 perplexity 80.28
  eval: bucket 0 perplexity 62.63
  eval: bucket 1 perplexity 53.76
  eval: bucket 2 perplexity 95.01
  eval: bucket 3 perplexity 105.53
...
```
## Run demo web
Demo web runs only on Mac OS or Linux.
If not train before, download pre-trained files automatically.
```bash
$ python web.py
Reading model parameters from train/translate.ckpt-32900
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

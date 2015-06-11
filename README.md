# SubTranslate
Simple tool for automatically translating "srt" subtitles for your movies using the google translate service.

This is a command line tool written in <strong>Python 3</strong> to translate your subtitles for your series or movies.

# Download
Download the latest version from <a href="https://github.com/naruse/SubTranslate/archive/master.zip">here</a>.

##### Dependencies
This tool uses goslate (http://pythonhosted.org/goslate/) so you will need to install it in order to run the tool.

<strong>Installing goslate is really easy, just run this:</strong>
```
python -m pip install goslate
```
### Running the tool
Just open your terminal and type:
```
python main.py [sub.srt] [desired sub lang] [original sub lang]
```
or for auto detecting the sub language:
```
python main.py [sub.srt] [desired sub lang]
```
Finally the tool will create for you a file with an upper case Prefix for your desired language. e.g:
```
python main.py Test1.srt es
```
will output: ```ES_Test1.srt```

<strong>Note:</strong> Make sure your srt subtitle files have an UTF8 encoding, else you will have errors.
Checkout <a href="http://redhotwords.com/unicode.html">here</a> to how to set the encoding in case you have a different encoding than UTF8
### Available Languages
|  |  | | |
|:---------------------------|:-------------------------|:---------------------------|:-----------------|
|pt   : Portuguese          |de   : German            |kn   : Kannada             |be   : Belarusian|  
|hi   : Hindi                |iw   : Hebrew           |ny   : Chichewa            |lo   : Lao       |   
|mk   : Macedonian           |ta   : Tamil            |tr   : Turkish             |pl   : Polish    |
|hr   : Croatian             |zu   : Zulu             |ga   : Irish               |pa   : Punjabi   |
|ca   : Catalan              |te   : Telugu           |mr   : Marathi             |es   : Spanish   |
|ur   : Urdu                 |uk   : Ukrainian        |ka   : Georgian            |km   : Khmer     |
|no   : Norwegian            |tg   : Tajik            |my   : Myanmar (Burmese)   |ar   : Arabic    |
|ig   : Igbo                 |ml   : Malayalam        |it   : Italian             |mt   : Maltese   |
|gu   : Gujarati             |sv   : Swedish          |so   : Somali              |bg   : Bulgarian |
|az   : Azerbaijani          |ko   : Korean           |gl   : Galician            |tl   : Filipino  |
|kk   : Kazakh               |sk   : Slovak           |ne   : Nepali              |la   : Latin     |
|fi   : Finnish              |vi   : Vietnamese       |sw   : Swahili             |nl   : Dutch     |
|af   : Afrikaans            |id   : Indonesian       |cs   : Czech               |ha   : Hausa     |
|fr   : French               |si   : Sinhala          |su   : Sundanese           |hy   : Armenian  |
|ja   : Japanese             |lt   : Lithuanian       |ht   : Haitian Creole      |lv   : Latvian   |
|fa   : Persian              |en   : English          |sr   : Serbian             |mg   : Malagasy  |
|zh   : Chinese              |bn   : Bengali          |th   : Thai                |el   : Greek     |
|eo   : Esperanto            |st   : Sesotho          |mn   : Mongolian           |yi   : Yiddish   |
|da   : Danish               |ms   : Malay            |ru   : Russian             |cy   : Welsh     |
|sl   : Slovenian            |mi   : Maori            |yo   : Yoruba              |ro   : Romanian  |
|bs   : Bosnian              |sq   : Albanian         |zh-CN: Chinese (Simplified)|jw   : Javanese  |
|et   : Estonian             |eu   : Basque           |is   : Icelandic           |hmn  : Hmong     |
|zh-TW: Chinese (Traditional)|ceb  : Cebuano          |uz   : Uzbek               |hu   : Hungarian |

### Compatibility
As mentioned above, in order to run SubTranslate you need to run the tool with <strong>Python 3.x</strong>
### Author
This tool was written by and is maintained by Juan Sebastian Muñoz aka "naruse". 
www.pencilsquaregames.com

Please do not hesitate to contact me with comments, bug reports or enhancements you would like to have through GitHub:
https://github.com/naruse/SubTranslate/issues

### License
TLDR; https://tldrlegal.com/license/mit-license

SubTranslate is released under the <a href="http://opensource.org/licenses/MIT">MIT License</a>.
### Donations
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=47A3BCMYDK3TS&lc=CO&item_name=Juan%20Sebastian&item_number=SubTranslateID&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted">Buy me a coffee! via paypal</a>

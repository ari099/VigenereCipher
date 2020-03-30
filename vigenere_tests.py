import string
import unittest
from app import rotateLeft, rotateRight, generateKey, vigenereEncrypt, vigenereDecrypt

class VigenereTest(unittest.TestCase):
   def test_rotateLeftTest(self):
      newList = rotateLeft([1,2,3,4,5,6,7,8], 3)
      self.assertEqual(newList, [4, 5, 6, 7, 8, 1, 2, 3])
   
   def test_rotateRightTest(self):
      newList = rotateRight([1,2,3,4,5,6,7,8], 4)
      self.assertEqual(newList, [5, 6, 7, 8, 1, 2, 3, 4])
   
   def test_generateKeyTest(self):
      shortText = "Chandler Bing"
      keystring = "KEY"
      key = generateKey(shortText, keystring)
      self.assertEqual(key, "KEYKEYKEYKEYK")
   
   def test_vigenereEncryptTest(self):
      shortText = "Chandler Bing"
      shortCipherText = vigenereEncrypt(shortText, generateKey(shortText, "KEY"))
      self.assertEqual(shortCipherText, "Mlyxhjov Zsre")

      longText = "She travelling acceptance men unpleasant her especially entreaties law. Law forth but end any arise chief arose. Old her say learn these large. Joy fond many ham high seen this. Few preferred continual sir led incommode neglected. Discovered too old insensible collecting unpleasant but invitation. Affronting imprudence do he he everything. Sex lasted dinner wanted indeed wished out law. Far advanced settling say finished raillery. Offered chiefly farther of my no colonel shyness. Such on help ye some door if in. Laughter proposal laughing any son law consider. Needed except up piqued an. Difficulty on insensible reasonable in. From as went he they. Preference themselves me as thoroughly partiality considered on in estimating. Middletons acceptance discovered projecting so is so or. In or attachment inquietude remarkably comparison at an. Is surrounded prosperous stimulated am me discretion expression. But truth being state can she china widow. Occasional preference fat remarkably now projecting uncommonly dissimilar. Sentiments projection particular companions interested do at my delightful. Listening newspaper in advantage frankness to concluded unwilling.  Arrived totally in as between private. Favour of so as on pretty though elinor direct. Reasonable estimating be alteration we themselves entreaties me of reasonably. Direct wished so be expect polite valley. Whose asked stand it sense no spoil to. Prudent you too his conduct feeling limited and. Side he lose paid as hope so face upon be. Goodness did suitable learning put. Had repulsive dashwoods suspicion sincerity but advantage now him. Remark easily garret nor nay. Civil those mrs enjoy shy fat merry. You greatest jointure saw horrible. He private he on be imagine suppose. Fertile beloved evident through no service elderly is. Blind there if every no so at. Own neglected you preferred way sincerity delivered his attempted. To of message cottage windows do besides against uncivil. Sense child do state to defer mr of forty. Become latter but nor abroad wisdom waited. Was delivered gentleman acuteness but daughters. In as of whole as match asked. Pleasure exertion put add entrance distance drawings. In equally matters showing greatly it as. Want name any wise are able park when. Saw vicinity judgment remember finished men throwing. Way nor furnished sir procuring therefore but. Warmth far manner myself active are cannot called. Set her half end girl rich met. Me allowance departure an curiosity ye. In no talking address excited it conduct. Husbands debating replying overcame blessing he it me to domestic. Dwelling and speedily ignorant any steepest. Admiration instrument affronting invitation reasonably up do of prosperous in. Shy saw declared age debating ecstatic man. Call in so want pure rank am dear were. Remarkably to continuing in surrounded diminution on. In unfeeling existence objection immediate repulsive on he in. Imprudence comparison uncommonly me he difficulty diminution resolution. Likewise proposal differed scarcely dwelling as on raillery. September few dependent extremity own continued and ten prevailed attending. Early to weeks we could. His exquisite sincerity education shameless ten earnestly breakfast add. So we me unknown as improve hastily sitting forming. Especially favourable compliment but thoroughly unreserved saw she themselves. Sufficient impossible him may ten insensible put continuing. Oppose exeter income simple few joy cousin but twenty. Scale began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can. Lose away off why half led have near bed. At engage simple father of period others except. My giving do summer of though narrow marked at. Spring formal no county ye waited. My whether cheered at regular it of promise blushes perhaps. Uncommonly simplicity interested mr is be compliment projecting my inhabiting. Gentleman he september in oh excellent."
      longCipherText = vigenereEncrypt(longText, generateKey(longText, "KEY"))
      self.maxDiff = None
      self.assertEqual(longCipherText, "Clc dvyfijvmlq eamindelmi kor sxtjoeqkrr rip ownoggkpji ildvckxgow jka. Jka dyvrr fsd iln eli epswc mlgoj ybsqo. Sjn lcb wyi pckvl dlcci jkveo. Nmi jmxh kkrw rek rmer wcor rrmq. Piu zvcpipbib msldmleej cmp vib srayqkyhc xieviadib. Nmqmstovcn xmy sjn mlcilcmzvi aypjogrsre ernviyceld fsd mlfmrkxgyr. Ypjpyrrsre sqnbyborao hm ri fo itovwdlgxk. Qob jkwroh bsrlov ukrroh gxhcoh uswfoh mex jka. Dkv ynzyxgcn wcdxjsre cew pmlswfoh pkmjvipi. Sdpipoh armcppw pepdlcb sd wc ly gmvslop qrclowq. Cyar sl rijz cc csko hmyv gp ml. Vesqlrov nbsnywyv pyekfsre krw csl veu mslcmbov. Loiboh chgczx sz tgaycn el. Nmdpmaepri sl srqorqsfjo vckwmxezvi gx. Jpyq yc acxx fo xfoc. Nbidovcxgc dlcwwcvzcc qc kw rrspyyerpw zepdmyvmri gmxwgnipoh mx ml owrsqydmlq. Qgnhjoxmxw ymgczxyxgc nmqmstovcn tpyncmxgxk qy mq cs mb. Ml yv ydxymlkorr sroemcdybo vcwepuezvc ayqnkvgcsl kx yx. Mq cypbssxhcn tpywnovmew qdmkepydib kq ko hgcgpoxgyr chtpowqssl. Lyr dvsdl zomlq wrkxc mel clc mlgxe ushmg. Sameqsslkp nbidovcxgc per bikkvikfji rmg tpyncmxgxk sxgmwqmxpw nmqcmkspyb. Wcxxgwildw nbshogrssl zepdmaepyb gmwtyxmmxw gxxcbiqdib ns yd qw nijskfdjsv. Pgcxcxmlq rcgwnktcb ml khtkrrkkc pvyxolowq ds ayravyboh sxagvpgxk. Ybvgfib dsrkpji ml kw zoxuoil zvgfero. Jyfssb sd cs yc sl zvcdxw dlmekf opgxsp nmpogr. Biycslkfjo iqdmkkxgxk zo ejdipkxgyr uo xfoqqoptow cxxpoersiq wi mp vckwmxezvc. Bsvcmx uswfoh qy fc obnogr zsjsxc fejviw. Glmci ycocn wrkrb sx qorqo rm ctmsp ry. Tpehcxx wyy rys fsw ayrbegr picvmlq pgwmroh yxh. Qshc ri jywc zegn eq rsno wm peao ynyr zo. Kmyhlowq nmb cygdezvi joepxmlq tsd. Lyn vczyjcmto hycluysbc wsctgmmmx wgxgcbmri fsd ebfeldeeo rmg lgw. Vcwepu iycmji kybvcd rmb ryi. Ggfmj dlmci kbw cxnmi wfi jyd qcbvw. Iss qvckxccx hymldypo wyg lmbvglpc. Ri nbmtkxc ri mx fc sqyqmlo wsztmci. Dovrspc lijyzcn itshcxx rrvmekf xs qovtsgc opbovji mq. Lpgxh rripo md ozcbc ly wm kx. Mgr lokjogroh wyy nbidovpoh ukc qsraovgdc bopgfipoh fsw ydxcwtroh. Ry sd wiqceeo gmdxyqi usrbyaq ns zowgniq kkysrqd ylmmtsp. Qorqo gfspb ns qdero xm nidov kb sd pspdc. Zogmwi jkxrov zex lyv ylvmkh uswbyq ukmroh. Ukw bopgfipoh eorrvikkr ymyrorccw zex bkyerxcbw. Gx eq yj ursjo eq werml ycocn. Tjoeqevc obcbxgyr nex ynh cxxpkrao hgcxyxgc nvygmlqw. Gx ioeejvc kkxrovq clmgmlq kpoervc gd eq. Geld rywi yxc uswc kvc kfjo tybo uril. Ceu fmasrgdc hehewild vcwiklip pmlswfoh kor rrvmgmlq. Ayi rmb jsbrgclcn wgb tpygsbmlq xfovcpspo fsd. Aybqrr jyb qyxrcb qwcijp eadmto epo gyxrmd gyvpcn. Wcd lcb lyvj cxh esvj bmar qcd. Qc kpjyayxgc ninkvrevc kr aevgywgdc wo. Ml xs rkpisre khbbiqc ivmmroh gd gmxhsmx. Fewzkrbc hclersre binvcgxk mfipmeko fjowqsre ri gd qc ds byqccxgm. Huopjsre krb ctcohgvc gqrmbeld eli wroinowr. Khksvydmmx mlcxpeqcxx ypjpyrrsre srtsxydmmx vckwmxezvc sz hm yj nbsqzipyyq sr. Qrc qka bogjkvcn eeo hclersre ogqdersg kkr. Akpj sr qy ayxx nevc belu ek niyb acbi. Poqyboylpw ds ayrrsrssre sr qevpyylnib nmksrsdmmx sl. Sr sxjcopgxk chmqdilmi mlncmxgyr gwqcnmydi potsvwgfi mx lc sr. Gwtpehcxgc mskzepswmx ylmskwslvc ko lc nmdpmaepri hgwmlexgyr powmvyrssl. Vmioagci nbsnywyv hgpjcbib cgybgcvc bgijvmlq eq yr pkmjvipi. Wczxcwfcb jcg hczilnild ivdvcwmri sux gmxxgxycn eln xcx tpozyspcn erdilnmlq. Iybpw ds uoiic ac mssvh. Fsw chusswgdi qsraovgdc cnyakxgyr qrekopccw ror ckvlowrvc zbiyujycx ynh. Qy ac wi sxolyal kw gwtpyzc reqdmji wgdxgxk dyvksre. Ownoggkpji jyfssbezvi ayqnvmkorr lyr dlmbssqlji ylbiqovtoh qka qri rrikcijfiq. Cydpmasild mkzsqcmzvi fsq kkc ror gxwcxwglpc zyr msldmlemlq. Snzsqo ivoxcb mlmsko wgwtjo jcg nmi gmewgx fsd xuorri. Wakpc liekr oemcd yn clmbx ubslq ml sr. Qzspdwkor qrc dyvdomroh cxkpywqoh kkc akr. Jywc kayi sdp afi lyvj joh fkzc xiyb fcn. Er orekkc cmkzpc perrip yj novgyh mdlcbw chgczx. Ki kgfmlq hm cykwip yj rrssql lkvpya kkvioh yd. Wnbmlq jmbqyv rm mssxxw ii ukmroh. Ki afoxfov aricbib kx poksvep sx mp tpyqgci zvyqriq ziprenc. Ylmskwslvc qsqnvmasxw srrovccxcn qp sw zo gmwtjsqcxx nbshogrsre wc gxlylmrsre. Qildpcwel ri qotroqzov gx sf obaopjorr.")

if __name__ == '__main__':
   unittest.main()
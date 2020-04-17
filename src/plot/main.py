# -*- coding: utf-8 -*-
"""Plot: 基本プロット
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
## local files


## define alias
W = Writer
_ = W.getWho()

## scenes
def sc_kukkoro(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("くっころ説明",
            w.comment("くっころ説明"),
            shin.explain("くっころ――それは捕虜にされようとしている気高い女騎士が利用されるくらいなら「くっ！殺せ」と言うけれど、",
                "相手（大抵はオークなどの化物である）は望み通りに殺したりはせず、女として弄ぶ",
                "その後、女騎士は快楽の虜となり自ら求めるようになるという、アダルトコンテンツのテンプレートのことである"),
            camera=w.shin,
            area=w.Tokyo,
            stage=w.on_street,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_outline(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("基本的な世界観説明",
            w.comment("謎のゲーム"),
            w.br(),
            shin.explain("高校生の$full_shinは「学校のマドンナ」と呼ばれる$full_mamiに憧れを抱いていたが、",
                "一言も喋ったことがない",
                "その彼女が学校帰りに古いゲームショップに一人で入るのを目撃し、親近感を覚える"),
            shin.explain("家に帰ると、応募した覚えのない懸賞に当選したとして新作ＶＲゲームが届いていた",
                "『$kukkorogame』は女騎士となり、迫りくる$goblinや$orkなどの怪物を倒しながら様々なクエストに挑戦するアクション系のアドベンチャーゲームだった"),
            w.comment("チュートリアルのはずが"),
            shin.explain("しかし楽勝と思えた小さな$goblinに苦戦し、ゲーム内で犯されてしまう",
                "その際に何か不思議なものを注ぎ込まれた"),
            w.comment("犯された結果"),
            shin.explain("現実世界に戻った$Sは自分が本当に犯されたかのような違和感を体に覚える",
                "眼鏡が必要だった視力は何故か回復していた"),
            )

def sc_mainstory(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("メインストーリー",
            w.comment("ゲームの流行"),
            w.br(),
            shin.explain("知らないうちに世間では『$kukkorogame』がブームとなっていた"),
            shin.explain("一方、$Sたちのクラスには転校生として、小学校の時に行方不明になったはずの幼馴染の$full_kanaが入ってくる",
                "$kanaは何故か$Sにあのゲームをやめるように警告した"),
            w.comment("ゲーム再開"),
            shin.explain("だが友だちの$full_yusakuから$mamiもあのゲームをやっていると聞き、再びゲームの世界に入る",
                "街で$mamiに似た外見の$k_mamiという女騎士に助けられ、色々と教わる",
                "だがチュートリアルだというダンジョンの最深部では、低レベルでは太刀打ちできない$orkが待ち構えていた"),
            )

def sc_futuredevelop(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("今後の展開",
            w.comment("将来の展望"),
            w.br(),
            shin.explain("ゲームで犯される度に何故かゲーム内でも現実世界でも強化される$S",
                "それに伴い、強烈に女を求める衝動が湧き上がるようになる",
                "また猟奇殺人事件や不可思議な妊娠事件等、奇妙な出来事が周囲で起こるようになる"),
            shin.explain("やがて自分には$w_magiと呼ばれるものがゲーム内で怪物によって注ぎ込まれていると知る",
                "その$w_magiを現実世界で取り戻そうと様々な女性が現れて彼を誘惑する",
                "$Sは$mamiへの想いと自分が自分ではなくなる衝動との狭間で苦悩しつつ、",
                "何故ゲームの世界が現実を侵食していくのか、何故自分だけ強化されていくのか、",
                "何故幼馴染の$kanaは戻ってきたのか",
                "その謎を解明していく"),
            shin.explain("その先に破滅と絶望が待っているとは知らずに"),
            )

def sc_fisrt_heroine(w: World):
    shin, mami = W(w.shin), W(w.mami)
    inside, outside = W(w.inside), W(w.outside)
    gob = W(w.goblin)
    return w.scene("ヒロインとの遭遇",
            w.symbol("【１】"),
            shin.be(),
            mami.be(),
            shin.explain("高校からの帰り道、",
                "$full_shinはよく利用している古いゲームショップから出てくる「高校のマドンナ」こと$full_mamiの姿を目撃してしまう"),
            shin.explain("帰宅すると応募した覚えのない懸賞で当たったというＶＲゲームが届いていた"),
            camera=w.shin,
            stage=w.on_hisroom_int,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_newgame(w: World):
    shin, mami = W(w.shin), W(w.mami)
    inside, outside = W(w.inside), W(w.outside)
    gob = W(w.goblin)
    return w.scene("新しいゲーム",
            shin.be(),
            mami.be(),
            shin.explain("ＶＲゲーム『$kukkorogame』は女騎士となり次々と襲い来るモンスターを倒していくアクションアドベンチャーだった",
                "しかしチュートリアルだと思った小さな$goblin一匹相手に苦戦し、仲間を呼ばれ、挙げ句ゲーム内で犯されてしまう"),
            camera=w.shin,
            stage=w.on_hisroom_int,
            )

def sc_transferstu(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("転校生",
            shin.be(),
            shin.explain("高熱を出して三日寝込んだ$Sが学校にやってきたその日、転校生がクラスに入ってくる",
                "彼女は小学生の時に行方不明になった$full_kanaだった", "雰囲気も見た目も変わっていたが、後ろの席に就いた彼女は一言「あのゲームを止めなさい」と言った"),
            )

def sc_schooldays(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("幼馴染と友人と",
            w.symbol("【２】"),
            shin.be(),
            shin.explain("ゲーム内で犯されてから視力が良くなった$Sだったが、友人の$full_yusakuから『$kukkorogame』が若者を中心にブームになってると教わる"),
            shin.explain("更に$mamiもあのゲームをしていると聞き、$Sは再びゲームの世界に入ることを決める"),
            camera=w.shin,
            stage=w.on_highschool,
            )

def sc_party(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("彼女とパーティになる",
            shin.be(),
            shin.explain("ゲームを始めると最初に入った世界と違い、城下町からスタートだった",
                "そこで銀髪の女騎士に絡まれるが、$mamiによく似た$k_mamiという黒髪の騎士に助けられる",
                "話してみるとどうやら彼女は$mamiのアバターのようだった"),
            shin.explain("初心者の$Sとパーティを組んでくれ、初級者用ダンジョンに挑むことになる"),
            )

def sc_herknight(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("彼女を守る",
            shin.be(),
            shin.explain("しかしダンジョン最深部で待っていたのはとても低レベルでは太刀打ちできない$orkだった"),
            )

def sc_pregnancy(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("妊娠事件",
            w.symbol("【３】"),
            w.comment("ある日、別のクラスの女子が学校を休み、妊娠したと噂になる"),
            shin.come(),
            shin.explain("犯されて強くなった聴覚で、隣のクラスの女子同士の会話まで聞こえるようになり、生活に支障が出ていた",
                "噂話にはゴミ屋敷で頭が食いちぎられた遺体が出たとか、学校を休んでる女子生徒が実は妊娠しているとか、",
                "$Sの興味のない、女子同士にありがちな話が沢山混ざっていた"),
            shin.explain("ただ『$kukkorogame』をやるようになってから周囲で奇妙なことが頻発しているのは確かで、",
                "この日も授業の途中で担任の$ln_asakoが体調を崩し出て行った"),
            shin.explain("それでも$mamiと会う為、学校を帰るとゲーム世界に入る",
                "そこで彼女から友人が誰とも付き合っていないのに妊娠していたと聞かされる"),
            camera=w.shin,
            )

def sc_newteacher(w: World):
    shin, mami = W(w.shin), W(w.mami)
    return w.scene("新しい先生",
            shin.be(),
            shin.explain("その数日後、担任の$ln_asakoは産休を取ったと説明され、代わりに若く魅力的な女教師$full_misaeが担任となる",
                "彼女はゲーム内で見かけた$k_misaeという銀髪の騎士によく似ていた"),
            )

def sc_about_shin(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("$full_shinについて",
            w.symbol("【$full_shin】"),
            shin.do("主人公の高校三年生",
                "ＶＲゲーム『$kukkorogame』の中で怪物に犯されることによって現実世界でも謎の力を手に入れることになる",
                "憧れの$full_mamiを守る為、ゲームでの世界でも現実世界でも体を盾にして頑張るが、徐々に変化していく世界と自身の体に戸惑い、",
                "また精神的にも追い詰められていく"),
            shin.explain("口数こそ少ないが、ゲームになるとよく喋る",
                "自分を律する強い精神力を持ち、大切な人を守る為に犠牲になることを厭わない勇敢さもあるが、",
                "こと女関係になるとどうしても一歩が踏み出せなくなってしまう"),
            camera=w.shin,
            )

def sc_about_mami(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    return w.scene("$full_mamiについて",
            w.symbol("【$full_mami】"),
            mami.explain("学校のマドンナと呼ばれるほど、高校でも一番の人気を誇る女子",
                "誰に対しても優しく、多くの同級生、後輩から慕われ、先生たちの信頼も厚い",
                "友だちに誘われて『$kukkorogame』を始めたらしい",
                "後に$shinとパーティを組む",
                "実は暗い過去を持つ"),
            camera=w.mami,
            )

def sc_about_kana(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    return w.scene("$full_kanaについて",
            w.symbol("【$full_kana】"),
            kana.be(),
            kana.explain("転校して$shinの前に戻ってきた、小学生の時に行方不明になって姿を消したはずの幼馴染",
                "小さい頃はいつも泣いていて$shinに助けられていたが、",
                "見た目も雰囲気も変わって別人のようになっている",
                "何故か執拗に$shinにゲームをやめるように忠告する",
                "ゲームはやったことないらしいが"),
            camera=w.kana,
            )

def sc_about_yusaku(w: World):
    shin, mami = W(w.shin), W(w.mami)
    yusaku, kana = W(w.yusaku), W(w.kana)
    mist, misae = W(w.mist), W(w.misae)
    return w.scene("$full_yusakuについて",
            w.symbol("【$full_yusaku】"),
            yusaku.explain("高校で唯一と言っていい$shinの友人",
                "ゲーム好きで将来はプロゲーム実況者を目指している"),
            yusaku.explain("何かと$shinの相談に乗ってくれるが、金勘定や利益優先の考えで動くことが多く、",
                "時々$shinとは相容れないことがある"),
            camera=w.yusaku,
            )

def sc_about_misae(w: World):
    misae = W(w.misae)
    return w.scene("$full_misaeについて",
            w.symbol("【$full_misae】"),
            misae.be(),
            misae.explain("突如産休を取って休んでしまった担任の$full_asakoに変わり、臨時で担任となった女教師",
                "その外見や雰囲気が$shinがゲーム内で遭った銀髪の女騎士によく似ている",
                "豊満な体と妖艶な魅力で$shinに迫ってくる"),
            camera=w.misae,
            )

## episode
def ep_outline(w: World):
    return w.episode("全体プロット",
            sc_kukkoro(w),
            sc_outline(w),
            sc_mainstory(w),
            sc_futuredevelop(w),
            note="世界観などについて")

def ep_story1(w: World):
    return w.episode("第１話",
            sc_fisrt_heroine(w),
            sc_newgame(w),
            sc_transferstu(w),
            ## NOTE
            ##  - 新太は懸賞で当たったらしい新しいVRゲームをやる
            ##  - ゲームのチュートリアルだと思ったゴブリンにゲーム中で犯され、何かを注ぎ入れられた
            ##  - 転校生が入ってくるが、それは小学生の頃に行方不明になった幼馴染だった
            note="主人公と設定説明＋くっころ")

def ep_story2(w: World):
    return w.episode("第２話",
            sc_schooldays(w),
            sc_party(w),
            sc_herknight(w),
            ## NOTE
            ##  - 夏菜に話しかけると彼女は新太に「もうゲームしないでくれ」と頼む
            ##  - しかし真実子がゲームをしていると聞き、新太は彼女を助ける為にゲームに戻る
            ##  - 何とか彼女とパーティになり、初心者向けダンジョンに潜るが、そこで待っていたのは高レベルのオークだった
            note="学校や社会説明とマドンナ紹介")

def ep_story3(w: World):
    return w.episode("第３話",
            sc_pregnancy(w),
            sc_newteacher(w),
            ## NOTE
            ##  - 学校にやってくると別のクラスの女子生徒が妊娠したと話題になっていた
            ##  - 再び彼女とゲームをやる新太。そこで彼女から「学校の友だちが誰ともやってないのに妊娠した」と告げられる
            ##  - 産休を取ったという担任の代わりに現れたのは、ダンジョンの途中で警告していった女騎士に似た女性だった
            note="マドンナもやっているから守ろうとして謎の騎士登場（１話出しておく）")

def ep_chara(w: World):
    return w.episode("メインキャラクター",
            sc_about_shin(w),
            sc_about_mami(w),
            sc_about_kana(w),
            sc_about_yusaku(w),
            sc_about_misae(w),
            note="主人公と、友人と、クラスのマドンナと、彼女の親友、それに謎の女騎士")

## chapter
def ch_plot(w: World):
    return w.chapter("プロット",
            ep_outline(w),
            ep_story1(w),
            ep_story2(w),
            ep_story3(w),
            ep_chara(w),
            )

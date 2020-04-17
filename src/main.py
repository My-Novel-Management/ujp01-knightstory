# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
## public libs
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## assets
from storybuilder.assets import basic, accessory
## local files
from src.plot.main import ch_plot

## define alias
W = Writer
_ = Writer.getWho()

################################################################
#
#   1.謎の姫騎士VRゲーム
#   2.自分だけが知っている？
#   3.彼女を守る為に、くっころされる
#
################################################################


## main
def create_world():
    """Create a world.
    """
    w = World("くっころ姫騎士オンライン")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2020)
    w.setBaseArea("Tokyo")
    # set textures
    # w.entryBlock()
    # w.entryHistory()
    # w.entryLifeNote()
    w.setOutline("くっころとは女騎士等が捕虜にされるなら殺せと言い出すシチュエーションを表す言葉だ。男子高校生の家に知らない人物から新しいVRゲームが届く。それは女騎士となり迫りくる魔物軍団と戦うというものだったが、圧倒的戦力差で負けてしまい、犯される。現実に戻ると何故か尻穴が痛む。出血していた。だが世間では誰もそんな目に遭ったことを覚えていない。クラスのマドンナもそれで遊ぶと知り、彼女を守ろうとするのだが")
    return w


def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_plot(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())


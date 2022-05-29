import os
import io
import requests
import shutil 
import random
import re
import glob
import time

from io import BytesIO
from requests import get
from telethon.tl.types import InputMessagesFilterPhotos

from FallenRobot import OWNER_ID
from FallenRobot.events import register
from FallenRobot import telethn
from PIL import Image, ImageDraw, ImageFont


LOGO_LINKS            = ["https://te.legra.ph/file/9721515204b76ce78406b.jpg",
                         "https://te.legra.ph/file/413f63fb3752840a585d1.jpg",
                         "https://te.legra.ph/file/90cea5034de0fc5284589.jpg",
                         "https://te.legra.ph/file/841a356ba6444e1aaa880.jpg",
                         "https://te.legra.ph/file/f7c93b2721f433b400f9a.jpg",
                         "https://te.legra.ph/file/2fcbf541fbc743d8cdd59.jpg",
                         "https://te.legra.ph/file/e209275161a59407088b3.jpg",
                         "https://te.legra.ph/file/65b6244897cbd7987063d.jpg",
                         "https://te.legra.ph/file/046362a0b7c9e5b99bb13.jpg",
                         "https://te.legra.ph/file/529aa748b07ed87461cd9.jpg",
                         "https://te.legra.ph/file/272506a16a4aa45b4c8e5.jpg",
                         "https://te.legra.ph/file/42190d3ff84819aa35cd1.jpg",
                         "https://te.legra.ph/file/df59e9ac771a79e1848df.jpg",
                         "https://te.legra.ph/file/7f1728a1927ba49591d6c.jpg",
                         "https://te.legra.ph/file/1f9a3959f22588632f49b.jpg",
                         "https://te.legra.ph/file/1872b414064c30b85e35e.jpg",
                         "https://te.legra.ph/file/4733cec4f6d16054b74a0.jpg",
                         "https://te.legra.ph/file/77fe8d7f38aa7b373460e.jpg",
                         "https://te.legra.ph/file/9592ec349d15fb862214e.jpg",
                         "https://te.legra.ph/file/e5fd7f6f2541feea69489.jpg",
                         "https://te.legra.ph/file/8bd136f1cebbb697c6f3c.jpg",
                         "https://te.legra.ph/file/b0177257d181b18a8b5bd.jpg",
                         "https://te.legra.ph/file/80c4dff6b49ccdfec94ba.jpg",
                         "https://te.legra.ph/file/4d0f44d4392206fd5ed05.jpg",
                         "https://te.legra.ph/file/9fc40a89d05d98c3be024.jpg",
                         "https://te.legra.ph/file/3c8adddc9d153804be313.jpg",
                         "https://te.legra.ph/file/65c0d41cc81670c10954c.jpg",
                         "https://te.legra.ph/file/6e26bbd89eca6d3ada2f6.jpg",
                         "https://te.legra.ph/file/7c0f1b8b9ccca4ff5c066.jpg",
                         "https://te.legra.ph/file/8f56d8694dd365dc0a0c8.jpg",
                         "https://te.legra.ph/file/b4068ca76c1842752d17c.jpg",
                         "https://te.legra.ph/file/9f055105168453ce4000e.jpg",
                         "https://te.legra.ph/file/8566828d0a933d8d0ec19.jpg",
                         "https://te.legra.ph/file/995ce509b1794ecd9ce1f.jpg",
                         "https://te.legra.ph/file/b4877126eb15efc1e0788.jpg",
                         "https://te.legra.ph/file/6290bd8f9c1da9dfec6bf.jpg",
                         "https://te.legra.ph/file/b5a567b92c1ad3fa0a2ac.jpg",
                         "https://te.legra.ph/file/a1b01c303d10423ee498f.jpg",
                         "https://te.legra.ph/file/8f8eb53dc41a8a82414c9.jpg",
                         "https://te.legra.ph/file/91179e99c766e695164e0.jpg",
                         "https://te.legra.ph/file/eefb2a9e415f33f60acfd.jpg",
                         "https://te.legra.ph/file/3375cfcc36c5332c1ed2d.jpg",
                         "https://te.legra.ph/file/3008cf400a6c66f35524f.jpg",
                         "https://te.legra.ph/file/d96fab4d6a83820b4f8ba.jpg",
                         "https://te.legra.ph/file/7152664ef4113e99b4a6d.jpg",
                         "https://te.legra.ph/file/493d4c6a3dc92f3cca315.jpg",
                         "https://te.legra.ph/file/621ef520266c253bca7b0.jpg",
                         "https://te.legra.ph/file/f3b002c68e07d769aa58a.jpg",
                         "https://te.legra.ph/file/e71b70c77347520e5088d.jpg",
                         "https://te.legra.ph/file/937381f49edb309eac3f1.jpg",
                         "https://te.legra.ph/file/5c92e3fed3a3641d17414.jpg",
                         "https://te.legra.ph/file/3807112dc25d02e456349.jpg",
                         "https://te.legra.ph/file/4c9208b525dd5b3a7b440.jpg",
                         "https://te.legra.ph/file/94784167fd3fffb1472ef.jpg",
                         "https://te.legra.ph/file/379a4e2dac1ae0964361e.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://te.legra.ph/file/e8685817092883f0aa0c7.jpg",
                         "https://telegra.ph/file/7e1c04947f6afb6cdf25c.jpg",
                         "https://telegra.ph/file/6279bb4be7e48da194353.jpg",
                         "https://telegra.ph/file/616784fcd89f13e789685.jpg",
                         "https://telegra.ph/file/803e7dd9fafdb086bce4a.jpg",
                         "https://telegra.ph/file/d7338861b7f996ec9d40d.jpg",
                         "https://telegra.ph/file/828730cd4d73333eaf129.jpg",
                         "https://telegra.ph/file/36c9321161d49c4b3d671.jpg",
                         "https://telegra.ph/file/ebeae90b99fe482d11784.jpg",
                         "https://telegra.ph/file/70f38f92fe8d3060a31e4.jpg",
                         "https://telegra.ph/file/db12cf905f557487abc60.jpg",
                         "https://telegra.ph/file/0f9be531164c927ded8ec.jpg",
                         "https://telegra.ph/file/57fb7a6df3d666878c6f3.jpg",
                         "https://telegra.ph/file/242930d9f7aaa0b0729fd.jpg",
                         "https://telegra.ph/file/883f255792d2c2ebdd5f5.jpg",
                         "https://telegra.ph/file/36a9c0c26967edf90d42d.jpg",
                         "https://telegra.ph/file/03bdaf253c43fc97adbbe.jpg",
                         "https://telegra.ph/file/5826715ff0895a5321d2d.jpg",
                         "https://telegra.ph/file/74807bfbc85057899ea8d.png",
                         "https://telegra.ph/file/e390f7531557c12379acb.jpg",
                         "https://telegra.ph/file/0b83432e72bb0ce0ed0f1.jpg",
                         "https://telegra.ph/file/23276d7f831611e347a7c.jpg",
                         "https://telegra.ph/file/109789c7dcc615c6731fa.jpg",
                         "https://telegra.ph/file/127ef2c311b42b2dbfb62.jpg",
                         "https://telegra.ph/file/bfd7fcd13b2c353030ef0.jpg",
                         "https://telegra.ph/file/0f7773c27b1379e2f3bea.jpg",
                         "https://telegra.ph/file/4606e5c76a4a6c893a721.png",
                         "https://telegra.ph/file/f46c4569d77d9a6be6aed.jpg",
                         "https://telegra.ph/file/2b4718637a7396e3b23d9.jpg",
                         "https://telegra.ph/file/40bce3c8e8ae3cd0198b9.jpg",
                         "https://telegra.ph/file/ac61cfac3290ed635f8cc.jpg",
                         "https://telegra.ph/file/55313171c70692e838451.jpg",
                         "https://telegra.ph/file/f503ce00794cadbdacdd2.jpg",
                         "https://telegra.ph/file/2153d9fad3613041fcd28.jpg",
                         "https://telegra.ph/file/6a7a790fe964c8c264b61.jpg",
                         "https://telegra.ph/file/103d2f4b7b1088890ae24.jpg",
                         "https://telegra.ph/file/63501bb4f1de53a81dba1.jpg",
                         "https://telegra.ph/file/00fdb4e3a06a6f6e81c35.jpg",
                         "https://telegra.ph/file/e2fbfce637048d2e042da.jpg",
                         "https://telegra.ph/file/29d3c7c297c40a17cde4b.jpg",
                         "https://telegra.ph/file/97c7aa91c51f72f82c2d9.jpg",
                         "https://telegra.ph/file/0096988891ba9b884d2dd.jpg",
                         "https://telegra.ph/file/12cb5cb6512b754deb92d.jpg",
                         "https://telegra.ph/file/38387c8384879e0ddb803.jpg",
                         "https://telegra.ph/file/3353253a27522219cc1ce.jpg",
                         "https://telegra.ph/file/daae7def66cb1d1aefa23.jpg",
                         "https://telegra.ph/file/e5fe618ad651777061c54.jpg",
                         "https://telegra.ph/file/3c56aa160ec242b1670eb.jpg",
                         "https://telegra.ph/file/0794ddfefdc770646c478.jpg",
                         "https://telegra.ph/file/05bc05a4b878e54ed3b20.jpg",
                         "https://telegra.ph/file/ef7ffbd3839645e33a0ec.jpg",
                         "https://telegra.ph/file/1daa50b9d3e26a5509cc2.png",
                         "https://telegra.ph/file/510600a5b93d83ce048f3.jpg",
                         "https://telegra.ph/file/0ede8bd4788327111ecbf.jpg",
                         "https://telegra.ph/file/e9f546797e42e821a91e1.jpg",
                         "https://telegra.ph/file/fc7fbefe92599bd79d038.jpg",
                         "https://telegra.ph/file/b88d6e78e206eb73e2e54.jpg",
                         "https://telegra.ph/file/48f8c62829953e82441e8.jpg",
                         "https://telegra.ph/file/56f7b34cae98a491e2b35.jpg",
                         "https://telegra.ph/file/9c23b4302926d40c46e12.jpg",
                         "https://telegra.ph/file/9bf850ea98a2b252ff233.jpg",
                         "https://telegra.ph/file/e764f0b3e2ecc56167803.jpg",
                         "https://telegra.ph/file/289f9cebe37f31a943f98.jpg",
                         "https://telegra.ph/file/0c647be0f5a48d576d692.jpg",
                         "https://telegra.ph/file/41c5b44c4f5978828b5b5.jpg",
                         "https://telegra.ph/file/9cdce279bdf240a933c14.jpg",
                         "https://telegra.ph/file/f20424687f94e9c285133.jpg",
                         "https://telegra.ph/file/e7858eb025e1ddb2f6267.jpg",
                         "https://telegra.ph/file/3e984aa5ab96df166f2a4.jpg",
                         "https://telegra.ph/file/e43e28aa952eaee6a5315.jpg",
                         "https://telegra.ph/file/6d222dcaf9ba1072c6062.jpg",
                         "https://telegra.ph/file/21e696bbefcfe39c6e74e.jpg",
                         "https://telegra.ph/file/64ec61e41da3d4aded33d.jpg",
                         "https://telegra.ph/file/5b1d8766504ff75c1bd1f.jpg",
                         "https://telegra.ph/file/731879a344b3b49fe51bd.jpg",
                         "https://telegra.ph/file/6221afc84b357ed0d1fc5.jpg",
                         "https://telegra.ph/file/499bb1117771d8c020038.jpg",
                         "https://telegra.ph/file/2690d73bc32cfdb986629.jpg",
                         "https://telegra.ph/file/21255de971701b9df0902.jpg",
                         "https://telegra.ph/file/434a35e7fe5e2c000c598.jpg",
                         "https://telegra.ph/file/22a5d3621aba0b370d0b6.png",
                         "https://telegra.ph/file/ae31845d1df2c4a84915b.png",
                         "https://telegra.ph/file/ae2b809c8d11e7fa4121d.png",
                         "https://telegra.ph/file/ccb7f3113994d5d2b26f6.png",
                         "https://telegra.ph/file/5e53f0257ff12a7b0737a.png",
                         "https://telegra.ph/file/a613600a9f9f8ee29f0f7.jpg",
                         "https://telegra.ph/file/129c14fada1a8c0b151f5.jpg",
                         "https://telegra.ph/file/c7552ed4246ccd8efd301.jpg",
                         "https://telegra.ph/file/e794f772243d46467bcce.jpg",
                         "https://telegra.ph/file/b6c43b9bd63f5f764d60b.jpg",
                         "https://telegra.ph/file/11585459a3950de7f307c.png",
                         "https://telegra.ph/file/37cde08802c3cea25a03f.jpg",
                         "https://telegra.ph/file/d8d2db623223dee65963e.png",
                         "https://telegra.ph/file/b7229017ffee2d814c646.jpg",
                         "https://telegra.ph/file/65630efca60bfbdf84bc9.jpg",
                         "https://telegra.ph/file/b8ce571c2f66a7c7070e5.jpg",
                         "https://telegra.ph/file/a39f63f61f143ec00f19f.jpg",
                         "https://telegra.ph/file/f7d946d8caaa21bf96dbf.jpg",
                         "https://telegra.ph/file/9e4bef8ae0725d6b62108.png",
                         "https://telegra.ph/file/3550089b22f3c8f506226.jpg",
                         "https://telegra.ph/file/4275a4d4d6d433406b5fa.jpg",
                         "https://telegra.ph/file/c476583ff55e1947461ad.jpg",
                         "https://telegra.ph/file/87d2e5c0170ead00a2bc2.jpg",
                         "https://telegra.ph/file/5027dd7379cc432c06e73.jpg",
                         "https://telegra.ph/file/9e447fcaf3c66ddefb603.jpg",
                         "https://telegra.ph/file/e5375f8233bea4f74b0f8.jpg",
                         "https://telegra.ph/file/a1297510a64733cc5845f.jpg",
                         "https://telegra.ph/file/ff04b594b699ce72316d7.jpg",
                         "https://telegra.ph/file/093836a52cb166f161819.jpg",
                         "https://telegra.ph/file/1e64bae43ca10d628ff6d.jpg",
                         "https://telegra.ph/file/678ff9bb3405158a9155e.jpg",
                         "https://telegra.ph/file/ab332ced3f63b96c375c5.jpg",
                         "https://telegra.ph/file/a736d6cac93294c323303.jpg",
                         "https://telegra.ph/file/dce8565bf7742f3d7122b.jpg",
                         "https://telegra.ph/file/3f97672eb7b50426d15ff.jpg",
                         "https://telegra.ph/file/19c6250369f8588a169c7.jpg",
                         "https://telegra.ph/file/13d53b03a48448156564c.jpg",
                         "https://telegra.ph/file/d21ff0d35553890e8cf34.jpg",
                         "https://telegra.ph/file/a5e4cb43178642ba3709d.jpg",
                         "https://telegra.ph/file/ecf108d25a6f5f56f91f4.jpg",
                         "https://telegra.ph/file/8bd2b561b4c1f7164f934.png",
                         "https://telegra.ph/file/7717658e6930c8196a904.jpg",
                         "https://telegra.ph/file/dc85d43c4fc5062de7274.jpg",
                         "https://telegra.ph/file/ff05c19f228ab2ed3d39d.jpg",
                         "https://telegra.ph/file/ff05c19f228ab2ed3d39d.jpg",
                         "https://telegra.ph/file/0d686bfffcb92a2fbdb0f.jpg",
                         "https://telegra.ph/file/0d686bfffcb92a2fbdb0f.jpg",
                         "https://telegra.ph/file/cdc66f16fbfb75971df2f.jpg",
                         "https://telegra.ph/file/5c575892b9f9534fd4f31.jpg",
                         "https://telegra.ph/file/78ffc400d4f3236b00e6b.jpg",
                         "https://telegra.ph/file/89d32e5bbf084a376c803.jpg",
                         "https://telegra.ph/file/b5d7dbcdce241013a061b.jpg",
                         "https://telegra.ph/file/c1d228bc1859213d258d7.jpg",
                         "https://telegra.ph/file/c6b0720b9f765809ea20a.jpg",
                         "https://telegra.ph/file/df7e648f2e68ff8e1a1e6.jpg",
                         "https://telegra.ph/file/5148f764cbc4700519909.jpg",
                         "https://telegra.ph/file/479e7f51c682dcd1f013f.jpg",
                         "https://telegra.ph/file/54a9eb0afe7a0f9c7c2f3.jpg",
                         "https://telegra.ph/file/73c52ee54567a61dac47a.jpg",
                         "https://telegra.ph/file/1427dbba81bd21b1bfc56.jpg",
                         "https://telegra.ph/file/1427dbba81bd21b1bfc56.jpg",
                         "https://telegra.ph/file/b0816374b470a5f9c66a6.jpg",
                         "https://telegra.ph/file/e10840ec9bea9bbfaff0e.jpg",
                         "https://telegra.ph/file/5935275d3ee09bc5a47b8.png",
                         "https://telegra.ph/file/c27e64f1e8ece187c8161.jpg",
                         "https://telegra.ph/file/055e9af8500ab92755358.jpg",
                         "https://telegra.ph/file/f18f71167f9318ea28571.jpg",
                         "https://telegra.ph/file/e2e26f252a5e25a1563c5.jpg",
                         "https://telegra.ph/file/47ccb13820d6fc54d872b.jpg",
                         "https://telegra.ph/file/f2ddccd28ceaeae90b2a3.jpg",
                         "https://telegra.ph/file/951c872f7f8d551995652.jpg",
                         "https://telegra.ph/file/8e8842f9fe207b8abd951.jpg",
                         "https://telegra.ph/file/8a14ecd2347ef88e81201.jpg",
                         "https://telegra.ph/file/b3869374ce0af9f26f92a.jpg",
                         "https://telegra.ph/file/8e17f8d3633a5696a1ccf.jpg",
                         "https://telegra.ph/file/b29d8956ae249773b0ec7.png",
                         "https://telegra.ph/file/d0eebe724b67d2ef7647e.jpg",
                         "https://telegra.ph/file/5780b3273162d2b9ba9ec.jpg",
                         "https://telegra.ph/file/e2d56d5dbb108ba7af20c.jpg",
                         "https://telegra.ph/file/1a4f50dd1e4ec9f04bfa1.jpg",
                         "https://telegra.ph/file/99b56305fa9c50767f574.jpg",
                         "https://telegra.ph/file/0859e0104c671bc9b6b7d.jpg",
                         "https://telegra.ph/file/b3af2980caf7040702171.jpg",
                         "https://telegra.ph/file/14be160df3b84c59e268e.jpg",
                         "https://telegra.ph/file/b958155e1e8e9ab9a0416.jpg",
                         "https://telegra.ph/file/24fff051c39b815e5078a.jpg",
                         "https://telegra.ph/file/258c02c002e89287d5d9b.jpg",
                         "https://telegra.ph/file/d2abc99773a9d4954c2ba.jpg",                       
                         "https://telegra.ph/file/9849b3940f063b065f4e3.jpg"
                         ]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id != OWNER_ID and not quew:
  await event.reply('`ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙʏ​ !`\n`Example /logo <Λ𝖦ՕᏒΛ>`')
  return
 pesan = await event.reply('**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**')
 try:
    text = event.pattern_match.group(1)
    randc = random.choice(LOGO_LINKS)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "black"
    shadowcolor = "blue"
    fnt = glob.glob("./FallenRobot/resources/fonts/*")
    randf = random.choice(fnt)
    font = ImageFont.truetype(randf, 120)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y = ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black")
    fname = "fallen.png"
    img.save(fname, "png")
    await telethn.send_file(event.chat_id, file=fname, caption = f"━━━━━━━━━━━━━━━━\nʟᴏɢᴏ sᴜᴄᴄᴇssꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ​ [ꨄ︎ 𝘼𝙧𝙮𝙖 ꨄ︎](https://t.me/MissAyra_Robot)\n━━━━━━━━━━━━━━━━")         
    await pesan.delete()
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await event.reply(f'Error, Report @karunada_kings_and_queens')


__mod_name__ = "Lᴏɢᴏ​"

__help__ = """
❍ /logo (Text) - Create a logo of your given text with random view.`
"""

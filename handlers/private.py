from sys import version_info
from handlers import __version__
from pyrogram import Client, filters, __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from time import time
from datetime import datetime

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    OWNER_NAME, 
    SUPPORT_GROUP,
    UPDATES_CHANNEL,
    ASSISTANT_NAME,
)
from helpers.filters import command, other_filters2
#  


__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)




@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAI8bmKIvgnlJyCrq9HIxSvCZCbm5CEjAAIaEAACpvFxHg-Z648-SCRWJAQ")
    await message.reply_text(
        f"""**Merhaba {message.from_user.mention} 🎵\nBen {BOT_NAME}!\n
● **Sesli sohbetlerde müzik çalabilen botum.**

● **Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕  Grubuna Ekle  ➕", 
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 Asistan", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ), 
    ) 
    
  
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""**🧸 {BOT_NAME} Online**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📣 Support", url=f"https://t.me/{SUPPORT_GROUP}")]])
    )

@Client.on_message(filters.private & filters.incoming & filters.command(["help", f"help@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔓 Üye komutları", callback_data="herkes"), 

                     InlineKeyboardButton(
                         "🔐 Admin komutları", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🪐 Sahip", url=f"https://t.me/{OWNER_NAME}")
                 ]
             ]
         )
    )




@Client.on_callback_query(filters.regex("cbhelp"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🔓 Üye Komutları", callback_data ="herkes"), 
          
          InlineKeyboardButton(
            "🔐 Admin Komutları",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🪐 Sahip", url=f"https://t.me/{OWNER_NAME}")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n 🏓/ping bot ping durumunu kontrol eder\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 Sahip", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri", callback_data="cbhelp")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🪐 Sahip", url=f"https://t.me/{OWNER_NAME}")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri", callback_data="cbhelp")
                 ] 
             ]
         )
         )






@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**Merhaba şuan aktif olarak çalışmaktayım yardım için aşağıda buttonu kullanınız!**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Yardım", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **Merhaba {query.from_user.mention} 🎵\nBen {BOT_NAME}!\n\n● Sesli sohbetlerde müzik çalabilen botum.\n\n● Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Grubuna Ekle ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🎙 Asistan", url=f"https://t.me/{ASSISTANT_NAME}"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Komutlar" , callback_data= "cbhelp"
                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
                
           ]
        ),
    )

@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📣 ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton(
                    "🗯️ ʙɪʟɢɪ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**• ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()} {BOT_NAME}**\n\n🧑🏼‍💻 sᴀʜɪʙɪᴍ: [{ALIVE_NAME}](https://t.me/mutsuz_pandabio)\n👾 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n🔥 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n🐍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n✨ PʏTɢCᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n🆙 ᴄᴀʟɪsᴍᴀ ᴅᴜʀᴜᴍᴜ: `{uptime}`\n\n❤ **Bᴇɴɪ ɢʀᴜʙᴀ ᴀʟᴅɪɢɪɴɪᴢ ɪᴄɪɴ ᴛᴇsᴇᴋᴋᴜʀʟᴇʀ . . !**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )




@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")



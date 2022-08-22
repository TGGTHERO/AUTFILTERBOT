class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {}</b>
    
<b>Sᴏʀʀʏ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ᴏɴ</b> <b><a href=https://t.me/TrockersDiscussions>𝗧𝗿𝗼𝗰𝗸𝗲𝗿𝘀𝗗𝗶𝘀𝗰𝘂𝘀𝘀𝗶𝗼𝗻𝘀</a></b><b> Gʀᴏᴜᴘ. Nᴏ ᴏᴛʜᴇʀ ᴄᴏᴍᴍᴀɴᴅ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴛʜɪs ʙᴏᴛ ᴇxᴄᴇᴘᴛ sᴛᴀʀᴛ. ᴅᴏɴ’ᴛ ᴡᴀsᴛᴇ ʏᴏᴜʀ ᴛɪᴍᴇ</b>"""
    OWNER_TXT = """<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : 
• ᴜꜱᴇʀɴᴀᴍᴇ : @HAASHIM_999
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href=https://t.me/HAASHIM_999>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ENGLISHSPELL_TXT = "<b>Hello {} I could not find the movie you asked for 🥴</b>\n\n<b>Google, Yandex Click on any button and find the <u>CORRECT MOVIE NAME </u>and enter it here the movie will be available 🙃\n\nIf you do not receive the movie even after entering the correct name ...</b> <code>@admin type movie name</code> <b>Inform the admin in this format .. We will upload within 24 hours 😇</b>"
    MALAYALMSPELL_TXT = "<b>வணக்கம் {} நீங்கள் கோரிய திரைப்படத்தை என்னால் கண்டுபிடிக்க முடியவில்லை 🥴 ...\n\nGoogle, Yandex ஏதேனும் பட்டனைக் கிளிக் செய்து, சரியான திரைப்படத்தின் பெயரைக் கண்டுபிடித்து, அதை இங்கே உள்ளிடவும், திரைப்படம் கிடைக்கும் / சரியான பெயரை உள்ளிட்ட பிறகும் படம் வரவில்லை என்றால் 🙂...</b> <code>@admin movie name</code>  <b>இந்த பார்மேட்டிள் அட்மிநுகு தெரிவிக்கலாம் .. 24 மணி நேரத்திற்குள் திரைப்படதம் இணைக்கப்படும் 😇</b>"
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🗂️ ᴛᴏᴛᴀʟ ғɪʟᴇs: <code>{}</code>
👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
👥 ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
📈 ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code>
📊 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SPELL_CHECK_ENG = """
Google the correct movie name by clicking the Google Button or click on the button labeled yendex and find the correct movie name and enter it here Movie / Tv. Web Series will get ..

If you still do not get it. Movie Name & year after @admin. Example: Add @admin kala 2020 to the group in this way. The admin will upload within 24 hours

If you ask for a movie released in theaters, you will not get it, only if it is released on ott Dvd
"""
    SPELL_CHECK_MAL = """
Google, yendex ஏதேனும் பட்டனைக் கிளிக் செய்து, சரியான திரைப்படத்தின் பெயரைக் கண்டுபிடித்து, அதை இங்கே உள்ளிடவும், திரைப்படம் கிடைக்கும்...

சரியான பெயரை உள்ளிட்ட பிறகும் படம் வரவில்லை என்றால் 🙂... [@admin movie name & year] இந்த பார்மேட்டிள் அட்மிநுகு தெரிவிக்கலாம் .. 24 மணி நேரத்திற்குள் திரைப்படதம் இணைக்கப்படும் 😇

தியேட்டர்ல ரிலீஸ் ஆகும் படத்தை கேட்டால் கிடைக்காது, Ott Dvd ரிலீஸ் ஆகும் போது தான் படம் கிடைக்கும்.
"""

import os

class Config(object):
    CONVERT_API = os.environ.get("GN4pzf2BHGr7nzHE")
    MAX_FILE_SIZE = os.environ.get("8")
    OWNER_ID = os.environ.get("OWNER_ID")
    PDF_THUMBNAIL = "./thumbnail.jpeg"
    USERNAME = os.environ.get("@my_channel")
    CAPTION = os.environ.get("TRUE")
    CUSTOM_TAG = os.environ.get("@HTGToolBot")
    if CUSTOM_TAG:
        custom_tag = " {" + CUSTOM_TAG + "}"
    else:
        custom_tag = " "



class Msgs(object):

    feedbackMsg = """
[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    fullPdfSplit = """If you want to split a pdf,

you need to send limits too..🙃
"""
    
    
    bigFileUnSupport = """Due to Overload, bot supports only {}mb files

`please Send me a file less than {}mb Size`🙃
"""
    
    
    encryptedFileCaption = """Page Number: {}
key 🔐: `{}`"""
    
    
    imageAdded = """`Added {} page/'s to your pdf..`🤓

/generate to generate PDF 🤞
"""
    
    
    errorEditMsg = """Something went wrong..😐

ERROR: `{}`

For bot updates join @Psgf 💎
"""
    
    
    pdfReplyMsg = """`Total pages: {}pgs`

__Unlike all other bots, this bot start sending images without converting the entire PDF to pages__ 😉

reply:
/extract - __to get entire pages__
/extract `pgNo` - __to get a specific page__
/extract `start:end` - __to get all the images b/w__


/encrypt `password` - to set password
/text - to extract text from pdf

Join Update Channel @ilovepdf_bot, More features soon 🔥
"""
    
    
    aboutDev = """About Dev:

OwNeD By: @nabilanavab 😜
Update Channel: @ilovepdf_bot 😇                                                                

Lang Used: Python🐍
[Source Code](https://github.com/nabilanavab/ilovepdf)

Join @ilovepdf_bot, if you ❤ this

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    
    I2PMsg = """Images to pdf :

        Just Send/forward me some images. When you are finished; use /generate to get your pdf..😉

 ◍ Image Sequence will be considered 🤓
 ◍ For better quality pdfs(send images without Compression) 🤧
 
 ◍ `/delete` - Delete's the current Queue 😒
 ◍ `/id` - to get your telegram ID 🤫                                                            
 
 ◍ RENAME YOUR PDF:
 
    - By default, your telegram ID will be treated as your pdf name..🙂
    - `/generate fileName` - to change pdf name to fileName🤞
    - `/generate name` - to get pdf with your telegram name

For bot updates join @ilovepdf_bot 💎

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    
    P2IMsg = """PDF to images:

        Just Send/forward me a pdf file.

 ◍ I will Convert it to images ✌️
 ◍ if Multiple pages in pdf(send as albums) 😌
 ◍ Page numbers are sequentially ordered 😬
 ◍ Send images faster than anyother bots 😋
 ◍ /cancel : to cancel a pdf to image work                                                       

1st bot on telegram wich send images without converting entire pdf to images

For bot updates join @ilovepdf_bot 💎

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    
    F2PMsg = """Files to PDF:

        Just Send/forward me a Supported file.. I will convert it to pdf and send it to you..😎

◍ Supported files(.epub, .xps, .oxps, .cbz, .fb2) 😁
◍ No need to specify your telegram file extension 🙄
◍ Only Images & ASCII characters Supported 😪
◍ added 30+ new file formats that can be converted to pdf..
API LIMITS..😕

For bot updates join @ilovepdf_bot 💎                                                           

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    
    warningMessage = """WARNING MESSAGE ⚠️:

◍ This bot is completely free to use so please dont spam here 🙏

◍ Please don't try to spread 18+ contents 😒

IF THERE IS ANY KIND OF REPORTING, BUGS, REQUESTS, AND SUGGESTIONS PLEASE CONTACT @nabilanavab

For bot updates join @ilovepdf_bot 💎                                                           

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""
    
    
    back2Start = """Hey..!! This bot will helps you to do many things with pdf's 🥳

Some of the main features are:
◍ `Convert images to PDF`
◍ `Convert PDF to images`
◍ `Convert files to pdf`

For bot updates join @ilovepdf_bot 💎                                                           

[Write a feedback 📋](https://t.me/nabilanavabchannel/17?comment=10)
"""

# please don't try to steel this code,
# god will asks you :(


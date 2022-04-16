class Translation(object):
# Unziper module
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    DOWNLOAD_START = " 📥 Downloading \n\nWait⏳ untill it completed."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists."
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""

# Renamer module
    CUSTOM_CAPTION_UL_FILE = "Uploaded by: @HTGToolBot"
    DOWNLOAD_FILE = " 📥 Downloading File "
    FILE_NOT_FOUND = "Error, File not Found!!"
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    UPLOAD_START = " 📤 Uploading File "
    AFTER_SUCCESSFUL_UPLOAD_MSG = " JOIN MY GROUP❤️: https://t.me/Music_Galaxy_Dl"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"

# Go fileupload module
    GO_FILE_UPLOAD = " 📤 Uploading \n\n To  gofile.io "
    AFTER_GET_GOFILE_LINK = " gofile.io\n\n<b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>🔗Link :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nUploaded by: @HTgToolbot\nJoin my group: @Music_Galaxy_Dl"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    
# Anon upload module
    ANNO_UPLOAD = " 📤 Uploading \n\n To  anonfiles.com "
    AFTER_GET_LINK = " anonfiles.com\n\n<b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b> 🔗 Link :</b> <code>{}</code>\n\nUploaded by: @HTgToolbot\nJoin my group: @Music_Galaxy_Dl"
    
# Converter to audio module
    AFTER_SUCCESSFUL_UPLOAD_MSG = " JOIN My Group ❤️: https://t.me/music_galaxy_dl"
    
# Converter to file
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
 
#--------
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @TGBotsCollectionbot \n For the list of Telegram bots. "
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."


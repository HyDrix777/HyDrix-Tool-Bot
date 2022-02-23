import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '784589736').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://hydra92074:hydra92074@cluster0.ktfkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
TG_MAX_SELECT_LEN = 100
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a>\n<b>📺 Type:</b> {kind}\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n<b>🎭 Genres:</b> {genres}\n\n<b>☀️ Languages:</b> {languages}\n<b>🎛 Countries:</b> {countries}\n<b>🎥 Director:</b> {director}\n<b>📝 Writers:</b> {writer}\n\n<b><a href='https://t.me/+q9NMdy0rY10zZWZl'>© IMDb (Series & Movies) Studio</a></b>\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 10 minutes to avoid copyright issues.</s>")


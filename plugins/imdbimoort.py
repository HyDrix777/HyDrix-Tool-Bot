

IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🎬 Title:</b> <a href={url}>{title}</a> [{year}]\n<b>📺 Type:</b> {kind}\n<b>📆 Release:</b> <a href={url}/releaseinfo>{release_date}</a>\n<b>🌟 Rating:</b> <a href={url}/ratings>{rating} / 10</a>\n(based on <code>{votes}</code> user ratings.)\n\n<b>📀 Runtime:</b> <code>{runtime} minutes</code>\n<b>🎭 Genres:</b> {genres}\n\n<b>☀️ Languages:</b> {languages}\n<b>🎛 Countries:</b> {countries}\n<b>🎥 Director:</b> {director}\n<b>📝 Writers:</b> {writer}\n\n<b><a href='https://t.me/+q9NMdy0rY10zZWZl'>© IMDb (Series & Movie) Studio</a></b>\n\n<b>✍️ Note:</b> <s>This message will be Auto-deleted after 10 minutes to avoid copyright issues.</s>")
IMDB = is_enabled((environ.get('IMDB', "True")), True)

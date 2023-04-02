# Markdown Quote Generator

Imagine you have a CSV file with the following format.

| Quote | Source | SourceURL |
|-------|--------|-----|
| God is our refuge and strength, a very present help in times of trouble. | Psalm 46:1 | https://www.biblegateway.com/passage/?search=Psalm46:1&version=NKJV |
| The lone wolf dies, but the pack survives. | Ned Stark | |

I'm not quite sure why *you* in particular reader would have a CSV file with that format, but I often times do. On my [website](https://segunakinyemi.com) I sometimes publish excerpts from various books that I've read. These excerpts contain quotes and passages that stood out to me, so much so that I recorded them for later reference. When recording those quotes, I do so in a running CSV file (or Excel/Google Docs spreadsheet that I convert to CSV) with the aforementioned format. While I could just publish that file in its entirety to the website, I prefer to convert it to a format that works better with the [Jekyll](https://jekyllrb.com/) flavor of markdown that the site uses.

This repo is a script I wrote to do that conversion. Examples of what its output eventually looks like can be seen [here](https://segunakinyemi.com/blog/excerpts-from-the-imitation-of-christ/), [here](https://segunakinyemi.com/blog/commands-of-christ/), and [here](https://segunakinyemi.com/blog/antman-quantamania-kang-the-conqueror/#arent-you-the-guy-that-got-bodied-by-ant-man).

You pass the script a CSV file with the aforementioned format, and it'll spit you back out a markdown quote version of all the rows within, taking into account whether you provided a `SourceURL` or not. The CSV file can be quoted or unquoted, but it does have to have all 3 columns.

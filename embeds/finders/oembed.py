from wagtail.embeds.finders.oembed import OEmbedFinder

class YouTubeOEmbedFinder(OEmbedFinder): 
    """
    Ensures that all YouTube embeds use the youtube-nocookie.com domain
    instead of youtube.com.
    """

    def find_embed(self, url, max_width=None):
        embed = super().find_embed(url, max_width=max_width)

        embed['html'] = embed['html'].replace(
            'youtube.com/embed', 'youtube-nocookie.com/embed')
        return embed        


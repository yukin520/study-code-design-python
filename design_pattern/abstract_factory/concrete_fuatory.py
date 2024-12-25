

from abstract_fuatory import LinkItem, ListItem, PageItem, Factory


class HtmlPageItem(PageItem):
    def __init__(self, title, author) -> None:
        super().__init__(title, author)

    def make_html(self):
        ouput = f"<html>\n<head>\n<title>{self.title}</title></head></html>"
        ouput += f"<body>\n"
        ouput += f"<h1>{self.title}</h1>\n"
        ouput += f"<ul>"
        for  l in self.content:
            ouput += l.make_html()

        ouput += f"</ul>\n"

        ouput += f"<hr>\n<address>{self.author}</address>\n"
        ouput += f"</body></html>"

        return ouput


class HtmlLinkItem(LinkItem):
    def __init__(self, caption, url) -> None:
        super().__init__(caption, url)

    def make_html(self):
        return f'<li><a href = "{self.url}"> {self.caption}</a></li>'


class HtmlListItem(ListItem):
    def __init__(self, caption) -> None:
        super().__init__(caption)

    def make_html(self):
        output = "<li>\n"
        output += f"{self.caption}"
        output += "<ul>\n"
        for l in self.items:
            output +=  l.make_html()
        output += "</ul>\n"
        
        output += "</li>\n"

        return output
    

class HtmlFacttory(Factory):
    def creata_page_item(self, title , author):
        return HtmlPageItem(title=title, author=author)
    
    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption=caption, url=url)
    
    def create_list_item(self, caption):
        return HtmlListItem(caption=caption)
    

html_factory = HtmlFacttory()
asahi = html_factory.create_link_item('asahi news', 'https://asahi.exaample.com')
yomiuri = html_factory.create_link_item('yomiuri news', 'https://yomiuri.exaample.com')
yahoo = html_factory.create_link_item('yahoo', 'https://yahoo.exaample.com')
wiki = html_factory.create_link_item('wiki', 'https://wiki.exaample.com')


news_pages = html_factory.create_list_item("news")
news_pages.add(asahi)
news_pages.add(yomiuri)

other_pages = html_factory.create_list_item('other page')
other_pages.add(yahoo)
other_pages.add(wiki)

all_page = html_factory.creata_page_item("My page", "taro")
all_page.add(news_pages)
all_page.add(other_pages)

all_page.write_html('hoge.html')







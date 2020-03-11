# 'Page' class is used to create page.

from base import Base
import setting

page_link = setting.DOMAIN + '/wp-admin/post-new.php?post_type=page'

class Page(Base):

    # xpath
    title_path = '//input[@id="title"]'
    submit_path = '//input[@id="publish"]'
    # 修改name的url
    rename_url = 'http://wppy.com/wp-admin/edit.php?post_type=page'
    slug_path = '//input[@name="post_name"]'
    r_submit_path = '//div[@class="submit inline-edit-save"]/button[@type="button"]'

    def __init__(self, url=page_link, item={'name' :'','slug':'','content':''}):
        super().__init__(url=url, item=item)


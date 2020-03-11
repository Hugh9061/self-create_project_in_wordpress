from base import Base
import setting
# http://wppy.com/wp-admin/edit-tags.php?taxonomy=lb21005-news-centers-cat&post_type=lb21005-news-centers


class Taxonomy(Base):

    # xpath
    title_path = '//input[@id="tag-name"]'  # xpath title
    slug_path = '//input[@id="tag-slug"]'  # xpath slug
    submit_path = '//input[@id="submit"]'  # xpath submit
    select_path = '//select[@id="parent"]'  # xpath select

    def __init__(self,tax_name = '',item={'name' :'','slug':'','tax':'','content':''}):
        url = setting.DOMAIN + '/wp-admin/edit-tags.php?taxonomy=' + tax_name + '-cat&post_type=' + tax_name
        super().__init__(url=url, item=item)

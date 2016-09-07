from cms.models import Page, Title
from djangocms_text_ckeditor.models import Text
from djangocms_picture.models import Picture
import json
from uuslug import slugify
import os

def copy_page(page, target, site):
    # from page @ site to target( or None ) @ site with position(0)
    # page = self.model.objects.get(pk=page_id)
    # page = self.model.objects.get(pk=page_id)
    # site = Site.objects.get(id=int(site_id))
    new_page = page.copy_page(target, site)
    new_page.save()
    return new_page


def set_title(object, title, slug):
    object.title = title
    object.slug = slug
    object.update_path()
    object.save()


def set_name(language, page, name):
    object = Text.objects.get(language = language, placeholder__page = page, placeholder__slot = "people_name")
    object.body = '<p>{}</p>\n'.format(name)
    object.save()


def set_profile(language, page, title, phd, tel, email, office, homepage):
    object = Text.objects.get(language = language, placeholder__page = page, placeholder__slot = "people_profile")
    if language == 'zh':
        object.body = '<p><strong>头衔:\xa0</strong>{}</p>\n\n<p><strong>博士:\xa0</strong>{}</p>\n\n<p><strong>电话:\xa0</strong>{}</p>\n\n<p><strong>Email: </strong>{}</p>\n\n<p><strong>办公室:\xa0</strong>{}</p>\n\n<p><strong>个人主页:\xa0</strong>{}</p>\n'.format(title, phd, tel, email, office, homepage)
    else:
        object.body = '<p><strong>Title:\xa0</strong>{}</p>\n\n<p><strong>PHD:\xa0</strong>{}</p>\n\n<p><strong>Tel:\xa0</strong>{}</p>\n\n<p><strong>Email: </strong>{}</p>\n\n<p><strong>Office:\xa0</strong>{}</p>\n\n<p><strong>Homepage:\xa0</strong>{}</p>\n'.format(title, phd, tel, email, office, homepage)
    object.save()


def set_brefintro(language, page, title, tel, email, office, research):
    object = Text.objects.get(language = language, placeholder__page = page, placeholder__slot = "people_brefintro")
    if language == 'zh':
        object.body = '<p><strong>头衔:\xa0</strong>{}<br>\n<strong>电话:\xa0</strong>{}<br>\n<strong>Email:\xa0</strong>{}<br>\n<strong>办公室:\xa0</strong>{}<br>\n<strong>研究领域:</strong></p>\n\n{}\n'.format(title, tel, email, office, research)
    else:
        object.body = '<p><strong>Title:\xa0</strong>{}<br>\n<strong>Tel:\xa0</strong>{}<br>\n<strong>Email:\xa0</strong>{}<br>\n<strong>Office:\xa0</strong>{}<br>\n<strong>Research Interests:</strong></p>\n\n{}\n'.format(title, tel, email, office, research)
    object.save()


def set_content(language, page, research, biography, publication):
    object = Text.objects.get(language = language, placeholder__page = page, placeholder__slot = "people_content")
    if language == 'zh':
        object.body = '<p><strong>研究领域:</strong></p>\n\n{}\n\n<p>\xa0</p>\n\n<p><strong>个人简历</strong></p>\n\n<p>{}</p>\n\n<p>\xa0</p>\n\n<p><strong>代表性论文</strong></p>\n\n<p>{}</p>\n'.format(research, biography, publication)
    else:
        object.body = '<p><strong>RESEARCH\xa0INTERESTS</strong></p>\n\n{}\n\n<p>\xa0</p>\n\n<p><strong>BIOGRAPHY</strong></p>\n\n<p>{}</p>\n\n<p>\xa0</p>\n\n<p><strong>SELECTED\xa0PUBLICATIONS</strong></p>\n\n<p>{}</p>\n'.format(research, biography, publication)
    object.save()


def set_picture(language, page, url):
    object = Picture.objects.get(language = language, placeholder__page = page, placeholder__slot = "people_photo")
    object.image = 'cms_page_media/{}/{}'.format(page.id, url)
    object.save()
    os.system('mkdir media/cms_page_media/{}'.format(page.id))
    os.system('wget http://sist.shanghaitech.edu.cn/cn/upload/image/{} -P media/cms_page_media/{}/'.format(url, page.id))


def set_people(list):
    page = Page.objects.get(pk=173) #mayi page
    target = page.parent
    site = page.site
    for i in list:
        new_page = copy_page(page, target, site)
        new_page_title_en = Title.objects.get_title(page = new_page, language = 'en')
        new_page_title_zh = Title.objects.get_title(page = new_page, language = 'zh')
        # zh
        set_title(new_page_title_zh, i['Name'], slugify(i['Name']))
        set_name('zh', new_page, '{} {}/{} {}'.format(
            i['EnglishTitle'],
            i['EnglishName'],
            i['Name'],
            i['Title_cn']))
        set_profile('zh', new_page, i['Title'], i['PHD'], i['Tel'], i['Email'], i['Office'], i['Website'])
        set_brefintro('zh', new_page, i['Title'], i['Tel'], i['Email'], i['Office'], i['Research'])
        set_content('zh', new_page, i['Research'], i['Biography'], i['Publication'])
        set_picture('zh', new_page, i['Photo'])
        if not (i['en']):
            new_page_title_en.delete()
        else:
            set_title(new_page_title_en, i['EnglishName'], slugify(i['EnglishName']))
            set_name('en', new_page, '{} {}/{} {}'.format(
                i['EnglishTitle'],
                i['EnglishName'],
                i['Name'],
                i['Title_cn']))
            set_profile('en', new_page, i['Title'], i['PHD_en'], i['Tel'], i['Email'], i['Office_en'], i['Website'])
            set_brefintro('en', new_page, i['Title'], i['Tel'], i['Email'], i['Office_en'], i['Research_en'])
            set_content('en', new_page, i['Research_en'], i['Biography_en'], i['Publication_en'])
            set_picture('en', new_page, i['Photo'])

file1 = open("/Users/eastpiger/Downloads/convertcsv.json")
set_people(json.load(file1))

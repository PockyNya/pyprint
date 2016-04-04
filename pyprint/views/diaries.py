#coding: utf-8
import tornado.web
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from pyprint.handler import BaseHandler
from pyprint.models import Post
from pyprint.constants import DIARY


class ListDiariesHandler(BaseHandler):
    def get(self):
        diaries = self.orm.query(Post.title, Post.created_time).filter(Post.type == DIARY)\
            .order_by(Post.created_time.desc()).all()
        return self.render('diaries.html', title='Diaries', diaries=diaries)


class RetrieveDiaryHandler(BaseHandler):
    def get(self, title):
        password = self.get_argument('pass', None)

        try:
            post = self.orm.query(Post).filter(and_(Post.title == title, Post.type == 'diary')).one()
        except NoResultFound:
            return self.redirect('/akarin')

	if not self.get_secure_cookie('username'):
	    if post.password and not password == post.password:
                raise tornado.web.HTTPError(403, '๑`･ᴗ･´๑')

        return self.render('post.html', title=post.title, post=post)

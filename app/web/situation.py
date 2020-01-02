from . import web
from app.models.issue import Issue
from flask import current_app
from app.models.content import Content
# from app.logger.logger_util import get_logger
#
# logger = get_logger()


@web.route('/situation')
def situation():
    # res = Issue.query.all()
    # user = Issue.query.filter_by(id=2).first()
    content = Content.query.filter_by(id=2).first()
    #
    # Content.query.join(followers, (followers.c.followed_id == Post.user_id))
    print(content.as_date)
    current_app.logger.info("this is log ...11111")

    # logger.info("get user data success ...".format(content.as_date))
    return 'this is a situation test ^_^'
    # res = db.session.query(Setting.title, db.func.count(Content.id)).join(Setting, (Content.status_id == Setting.id),
    #                                                                       isouter=True).group_by(
    #     Content.status_id).all()

    pass

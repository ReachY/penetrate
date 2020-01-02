from . import web
from app.models.issue import Issue
from app.models.content import Content
from app.logger.logger_util import get_logger

# logger = get_logger()


@web.route('/situation')
def situation():
    # res = Issue.query.all()
    user = Issue.query.filter_by(id=2).first()
    content = Content.query.filter_by(id=2).first()
    # logger.info("get user data success ...".format(user.title))
    return 'this is a situation test ^_^'

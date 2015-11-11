from .plugins.formskit.models import PostForm as BasePostForm
from .requestable import Requestable


class PostForm(BasePostForm, Requestable):
    pass

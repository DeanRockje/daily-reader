from django.db.models import signals
from django.utils.functional import curry


class AutoUser(object):
    def process_request(self, request):
        if not request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            if hasattr(request, 'user') and request.user.is_authenticated():
                user = request.user
            else:
                user = None

            user = curry(self.mark_whodid, user)
            signals.pre_save.connect(user,  dispatch_uid = (self.__class__, request,), weak = False)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid =  (self.__class__, request,))
        return response

    def mark_whodid(self, user, sender, instance, **kwargs):
        if not getattr(instance, 'user', None):
            instance.user = user
        if hasattr(instance,'user'):
            instance.user = user
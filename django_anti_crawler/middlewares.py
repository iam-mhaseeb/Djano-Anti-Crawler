import logging
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings

log = logging.getLogger(__name__)


class DjangoAntiCrawlerMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):

        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        ip_cache_key = "django_anti_crawler:ip_rate" + ip

        ip_hits_timeout = settings.IP_HITS_TIMEOUT if hasattr(settings, 'IP_HITS_TIMEOUT') else 60
        max_allowed_hits = settings.MAX_ALLOWED_HITS_PER_IP if hasattr(settings, 'MAX_ALLOWED_HITS_PER_IP') else 2000

        # get the hits by this IP in last IP_TIMEOUT time
        this_ip_hits = cache.get(ip_cache_key)

        if not this_ip_hits:
            this_ip_hits = 1
            cache.set(ip_cache_key, this_ip_hits, ip_hits_timeout)
        else:
            this_ip_hits += 1
            cache.set(ip_cache_key, this_ip_hits)

        log.info('Ip: {} already did: {} where max allowed hits are: {} and timeout for hits is: {}.'.format(
          ip,
          this_ip_hits,
          max_allowed_hits,
          ip_hits_timeout
        ))

        if this_ip_hits > max_allowed_hits:
            return HttpResponseForbidden()

        else:
            response = self.get_response(request)
            return response

import pprint
import logging
from scrapy import signals


class SettingsLogging(object):
    @classmethod
    def from_crawler(cls, crawler):
        logging.debug('Crawler settings:\n{}'.format(
            pprint.pformat(crawler.settings.attributes)))
        ext = SettingsLogging()
        crawler.signals.connect(
            ext.spider_opened,
            signal=signals.spider_opened)
        return ext

    def spider_opened(self, spider):
        logging.debug('Spider settings:\n{}'.format(
            pprint.pformat(spider.settings.attributes)))


EXTENSIONS = {
    'levelup.settings.SettingsLogging': 100
}

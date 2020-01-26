import json
from typing import Dict, List

from django.conf import settings
from django.db import models

from .article import Article
from .category import Category
from .user import User
from ..generics.models import RealmBaseModel
from ..integration.summary import SUMMARY_FETCHERS
from ..utils import get_datetime_from_till

if False:  # pragma: nocover
    from ..integration.summary.base import ItemsFetcherBase, SummaryItem


class Summary(RealmBaseModel):
    """Cводки. Ссылки на материалы, собранные с внешних ресурсов."""

    data_items = models.TextField('Текущие элементы сводки')

    data_result = models.TextField(
        'Результат для фильтрации сводки',
        help_text='Данные для фильтрации элементов сводки при последующих обращениях к ресурсу.')

    class Meta:

        verbose_name = 'Сводка'
        verbose_name_plural = 'Сводки'
        ordering = ('-time_created',)

    def __str__(self):
        return str(self.time_created)

    @classmethod
    def make_text(cls, fetched: Dict[str, List['SummaryItem']]) -> str:
        """Компонует текст из полученных извне данных.

        :param fetched:

        """
        summary_text = []

        for fetcher_alias, items in fetched.items():

            if not items:
                continue

            summary_text.append(f'.. title:: {SUMMARY_FETCHERS[fetcher_alias].title}')
            summary_text.append('.. table::')

            for item in items:
                line = f'`{item.title}<{item.url}>`_'

                if item.description:
                    line += f' — {item.description}'

                summary_text.append(line)

            summary_text.append('\n')

        if not summary_text:
            return ''

        summary_text.append('')
        summary_text = '\n'.join(summary_text)

        return summary_text

    @classmethod
    def create_article(cls) -> 'Article':
        """Создаёт сводку, используя данные, полученные извне."""
        summary_text = cls.make_text(cls.fetch())

        format_date = lambda d: d.date().strftime('%d.%m.%Y')
        date_from, date_till = get_datetime_from_till(7)

        robot_id = settings.ROBOT_USER_ID

        article = Article(
            title=f'Сводка {format_date(date_from)} — {format_date(date_till)}',
            description='А теперь о том, что происходило в последнее время на других ресурсах.',
            submitter_id=robot_id,
            text_src=summary_text,
            source=Article.SOURCE_SCRAPING,
            published_by_author=False,
        )
        article.mark_published()
        article.save()

        article.add_to_category(Category(pk=settings.SUMMARY_CATEGORY_ID), User(pk=robot_id))

        return article

    @classmethod
    def fetch(cls) -> Dict[str, List['SummaryItem']]:
        """Добывает данные из источников, складирует их и возвращает в виде словаря."""
        latest = cls.objects.order_by('-pk').first()

        prev_results = json.loads(getattr(latest, 'data_result', '{}'))
        prev_dt = getattr(latest, 'time_created', None)

        all_items = {}
        all_results = {}

        for fetcher_alias, fetcher_cls in SUMMARY_FETCHERS.items():

            prev_result = prev_results.get(fetcher_alias) or []

            fetcher: ItemsFetcherBase = fetcher_cls(
                previous_result=prev_result,
                previous_dt=prev_dt
            )
            result = fetcher.run()

            if result is None:
                # По всей видимости, произошла необработанная ошибка.
                items, result = [], prev_result

            else:
                items, result = result

            all_items[fetcher_alias] = items
            all_results[fetcher_alias] = result

        new_summary = cls(
            data_items=json.dumps(all_items),
            data_result=json.dumps(all_results)
        )
        new_summary.save()

        return all_items

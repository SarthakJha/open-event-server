import factory

import tests.factories.common as common
from tests.factories.event import EventFactoryBasic
from app.models.event_copyright import EventCopyright, db


class EventCopyrightFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = EventCopyright
        sqlalchemy_session = db.session

    event = factory.RelatedFactory(EventFactoryBasic)
    holder = common.string_
    holder_url = common.url_
    licence = common.string_
    licence_url = common.url_
    year = 2007
    logo = common.url_
    event_id = 1

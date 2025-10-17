from modeltranslation.translator import translator, TranslationOptions

from info.models import MainInfo, Service, AboutUs, Event


class TitleWithDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location')


translator.register(MainInfo, TitleWithDescriptionTranslationOptions)
translator.register(Service, TitleWithDescriptionTranslationOptions)
translator.register(AboutUs, TitleWithDescriptionTranslationOptions)
translator.register(Event, EventTranslationOptions)

import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')

    class Meta:
        model = settings.AUTH_USER_MODEL


class TagFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = 'askbot.Tag'


class PostFactory(factory.django.DjangoModelFactory):
    text = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = 'askbot.Post'


class QuestionFactory(PostFactory):
    post_type = 'question'


class AnswerFactory(PostFactory):
    post_type = 'answer'


class ThreadFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    text = factory.Faker('paragraph', nb_sentences=10)
    author = factory.SubFactory(UserFactory)

    tagnames = factory.Faker('word')
    language = factory.Faker('language_code')

    added_at = factory.Faker('date_time')
    wiki = factory.Faker('boolean')

    class Meta:
        model = 'askbot.Thread'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        instance = manager.create_new(*args, **kwargs)
        return instance
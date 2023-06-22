from celery import shared_task
from django.contrib.auth.models import User
from .models import Post, Response
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def respond_send_email(respond_id):
    respond = Response.objects.get(id=respond_id)
    send_mail(
        subject=f'MMosup Billboard: новый отклик на объявление!',
        message=f'Доброго дня, {respond.post.author}, ! На ваше объявление есть новый отклик!\n'
                f'Прочитать отклик:\nhttp://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='newsportal272@gmail.com',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def respond_accept_send_email(response_id):
    respond = Response.objects.get(id=response_id)
    print(respond.post.author.email)
    send_mail(
        subject=f'MMosup: Ваш отклик принят!',
        message=f'Добрый день, {respond.author}, Автор объявления {respond.post.title} принял Ваш отклик!\n'
                f'Посмотреть принятые отклики:\nhttp://127.0.0.1:8000/responses',
        from_email='090090999@mail.ru',
        recipient_list=[respond.post.author.email, ],
    )


@shared_task
def send_mail_monday_8am():

    now = timezone.now()
    list_week_posts = list(Post.objects.filter(dateCreation__gte=now - timedelta(days=7)))
    if list_week_posts:
        for user in User.objects.filter():
            print(user)
            list_posts = ''
            for post in list_week_posts:
                list_posts += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'посты за прошедшую неделю.',
                message=f'Добрый день, {user.username}!\nредлагаю ознакомится с новостями, '
                        f'за последние 7 дней :\n{list_posts}',
                from_email='090090999@mail.ru',
                recipient_list=[user.email, ],
            )
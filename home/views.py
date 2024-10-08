from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post, Like
import pika
import json
def publish_message(message):
    params = pika.URLParameters('amqps://jgnrzslb:RzcNiznVg3p688251fhexCrTu8DyHG4r@rat.rmq2.cloudamqp.com/jgnrzslb')

    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    message = {
        "data" : 1,
        "Tech" : ["Django", "RabbitMQ"]
    }
    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=json.dumps(message),
                        )
    print(f"Published message: {message}")
    connection.close()



def post_list(request):
    publish_message('Hello, RabbitMQ!')
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.create(user=request.user, post=post)  # Assuming a Like model exists
    return redirect('post_list')
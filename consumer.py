import pika

def process_message(message):
    # Add your message processing logic here
    print(f'Processing message: {message}')

def callback(ch, method, properties, body):
    message = body.decode()
    process_message(message)

params = pika.URLParameters('amqps://jgnrzslb:RzcNiznVg3p688251fhexCrTu8DyHG4r@rat.rmq2.cloudamqp.com/jgnrzslb')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='my_queue')

channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
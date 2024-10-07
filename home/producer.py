import pika, json

params = pika.URLParameters('amqps://jgnrzslb:RzcNiznVg3p688251fhexCrTu8DyHG4r@rat.rmq2.cloudamqp.com/jgnrzslb')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    print(method, body)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
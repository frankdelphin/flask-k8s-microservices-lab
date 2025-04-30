import pika, json

def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)

    except Exception as err:
        return "Internal server error", 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchage="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE #the queue will be retained even if the pod crashes or restart. unless, queue will be lost
            ),
        )
    except: 
        fs.delete(fid)
        return "Internal server error", 500
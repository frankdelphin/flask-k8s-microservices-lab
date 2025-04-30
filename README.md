# flask-k8s-microservices-lab
Un laboratoire pour explorer les architectures MSA avec Flask, Kubernetes, RabbitMQ et K9s.


## Configuration du /etc/hosts pour l'Ingress
Le routage Kubernetes utilise le domaine personnalisé mp3converter.com.

Pour que cela fonctionne en local via Minikube, vous devez activer ingress et modifier votre fichier /etc/hosts :
```
minikube addons enable ingress
sudo nano /etc/hosts
```
Ajoutez la ligne suivante (dans la section de Minikube si elle existe déjà) :

#### To allow the same kube context to work on the host and the container
127.0.0.1       mp3converter.com

127.0.0.1 correspond à l'adresse locale de votre machine (localhost).
Cela permet de rediriger les appels vers mp3converter.com directement sur votre environnement local via Minikube. Vous pourrez alors accéder aux services exposés par l'Ingress en visitant : http://mp3converter.com/


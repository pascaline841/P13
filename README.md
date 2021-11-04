*Création de l'application dans Heroku*
commande du terminal:
- Se connecter à Heroku : `heroku login`
- Création de l'application : `heroku create <nom_app>`
- `git push heroku master `<br>
- Lancer l'application:  `heroku open `
Vous pouvez accéder à votre application en ligne : `https://<nom_app>.herokuapp.com/`  

### Mise en place du pipeline Circle CI
*Liaison du projet à Circle CI*
- Se connecter à CircleCI
- Reliez votre compte CircleCI à votre compte GitHub 
- Allez dans `Projects` > `Set Up Project` choisir `"if you already have.circleci/config.yml"` et branche master 
- Choisissez votre projet GitHub 
- Retournez ensuite sur `Dash Board`

**Ajout de variables d'environnement**<br>
Cliquez sur `Project Settings` > `Environment Variables` > `Add Environment Variables`

| Nom | Description | 
|-----------------|:-------------:|-
| IMAGE_NAME  |  Le nom de l’image Dockerhub |   
| HEROKU_APP_NAME | Nom de votre appli dans Heroku |   
| HEROKU_TOKEN   | Token d'identification Heroku `heroku auth:token` | 
| DOCKERHUB_USERNAME | Votre identifiant Dockerhub |  
| DOCKERHUB_PASS | Votre mot de passe ou token Dockerhub https://hub.docker.com/settings/security > New access token | 

*Déploiement Effectué à chaque mise à jour du projet GitHub.*<br>
`git add <file>
git commit -m "<comment>"
git push -u origin`
<br>
Retournez sur votre compte CircleCI pour voir les "*jobs*" du pipeline s'activer :
- `build_and_test` monte et effectue les tests du bon fonctionnement de l'appli, via Pytest
- `docker-build-and-push` envoie l'image du projet sur docker hub (uniquement branche master)
- `deploy_heroku` envoie le projet sur heroku et le déploie (uniquement  branche master)  

### Récupération du projet en local
- Ouvrir Docker Desktop<br>
- Récupérez l'image en localement: `docker pull <docker_username>/oc-lettings:tag`
- Listez les images: `docker images`
- Lancez le conteneur Docker avec le fichier des variables d'environnement locales: `docker run -d -p 8000:8000 oc-lettings`
- Testez le site dans votre navigateur: `http://127.0.0.1:8000/`
- Listez les conteneurs Docker lancés: `docker container ps`
- Arrêtez le conteneur: `docker stop <CONTAINER ID>`
- Nettoyez/Supprimez conteneur: `docker system prune`

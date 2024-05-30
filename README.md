# Coffee Project # 

Welcome to my coffee recipes website, a website that contains private and public coffee recipes and other functions ! 

---


## Features ##


**index** ⚡
![Image alt text](screenShots/index.png)

The first page, from here you can go to registration or login



---


**Login** ⚡

![Image alt text](screenShots/login.png)

Guarantees secure access and entry to the user's personal area


---




**Register**⚡

![Image alt text](screenShots/registger.png)

Enables new user registration to the system





---




**dashboard** ⚡
![Image alt text](screenShots/dashboard.png)

The dashboard is the page with the quick access to all the other pages, contains links to all the functions of the site, only a logged in user can enter the dashboard!





---





**Add Public Recipe** ⚡
![Image alt text](screenShots/addPublic.png)

Allows the user to enter information about a public recipe, the information will be accessible to everyone



---





**Add Private Recipe** ⚡
![Image alt text](screenShots/addPrivate.png)

Allows only a logged in user to enter a private recipe for him, which is associated with him in the database, using a foreign key



---





**My Recipes** ⚡
![Image alt text](screenShots/myRecipes.png)

Displays all the private recipes of that user, according to user_id association in the database, therefore the user must be logged in




---






**All Recipes** ⚡
![Image alt text](screenShots/allRecipes.png)

Allows access to the public recipes only, to all users even if they are not logged in



---






**Random Recipe** ⚡
![Image alt text](screenShots/random.png)

Displays a random recipe from the public recipes in the database



---





**Gallery** ⚡
![Image alt text](screenShots/gallery.png)

Shows pictures of different types of coffee



---
**Logout** ⚡

Disconnects the user and redirects him to the index page


---







# tools 💼


In our project we use modern technologies and tools to improve and optimize the development, testing and deployment process.
In this project we use these tools especially and especially in the various devops processes.



## Continuous Integration and Delivery
  - **jenkins** : An open-source automation server that enables developers around the world to reliably build, test, and deploy their software. Jenkins orchestrates our CI/CD pipeline, integrating seamlessly with GitHab for a smooth development     
     process. in this project used with multibranch pipeline t orun diffrent workflows.
    ![Image alt text](images/jenkins.png)





## Containerization and Artifact Storage
  - **Docker** : Dockerize our application and storing the image, in Dockerhub.
     allows us to run and deploy the application without conditions and limitations, and to share with group members.
    ![Image alt text](images/docker.png)




## Deployment
  - **argocd** : Argo CD is an open-source tool used for managing and automating the operation of applications in Kubernetes. It focuses on easily and safely managing and deploying applications in a Kubernetes environment..
    When using Argo CD, you define applications through relatively simple and readable YAML.
    The application definition includes all the necessary information to specify the import and deployment of the application in your Kubernetes environment.


    ![Image alt text](images/argocd.png)



## Kubernetes
  - **azure AKS** : Azure Kubernetes Service (AKS) is a managed Kubernetes service provided by Microsoft Azure. It allows you to deploy, manage, and scale containerized applications using Kubernetes without needing to manage the underlying 
infrastructure.
With AKS, you can easily create, configure, and scale Kubernetes clusters in the Azure cloud. It provides integration with other Azure services, such as Azure Active Directory for authentication, Azure Monitor for monitoring, and Azure Container Registry for storing container images.


    ![Image alt text](images/kubernetes.png)


## monitoring
  - **grafana** :Grafana is an open-source analytics and monitoring platform that allows you to query, visualize, alert on, and understand metrics no matter where they are stored. It provides a powerful and flexible platform for creating, exploring, and sharing dashboards and data visualizations.

    ![Image alt text](images/grafana.png)






- **prometheus** : Prometheus is designed for monitoring the performance and availability of applications and infrastructure. It collects metrics from configured targets at regular intervals, evaluates rule expressions, displays the results, and can trigger alerts if certain conditions are met.

    ![Image alt text](images/prometheus.png)

  
---


# Run Locally : 🐳


## Clone  :

```bash
git clone https://github.com/ofekbarel/Final-Project.git
```

## Docker-compose file :


```bash
  version: '3.3'
services:
  web:
    image: ofekbarel11/coffeproject:latest
    ports:
      - "5000:5000"
    environment:
     - POSTGRES_USER=postgres
     - POSTGRES_PASSWORD=postgres
     - HOST=postgres


    depends_on:
      - postgres

  postgres:
    image: postgres:14
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=test
    #volumes:
      #- mongodb_data:/data/db
```


## Start the Applicaion :

Go to the project directory

```bash
  docker-compose up -d
```



    

  

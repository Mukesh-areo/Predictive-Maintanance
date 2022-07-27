# Predictive-Maintanance
Machine Learning Project to Predict Remaining useful life of an Engine

creating conda enviroinment
......
conda create -p venv1 python==3.7 -y

......
Activating Conda env 
......
conda activate venv1/

......

to add file to github
......
git add .
......


```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```


CICD PIPELINE 



To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = mukeshbabu447@gmail.com
2. HEROKU_API_KEY = 064c1296-73f1-43f9-a719-341c98a8c5f3
3. HEROKU_APP_NAME = predictive-maintenance-ml

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir
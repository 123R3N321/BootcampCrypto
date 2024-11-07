# This is the bootcamp project
## git and github tutorial
all the steps here require you to sue the terminal in pycharm
- everytime before you want to work on the project:
    - type command:
```bash
  git pull
  ```
  the above command makes sure your code is up-to-date with the shared version
<br />
<br />
- Then, when you are done coding, you need to:
    - type three commands:
```bash
  git add <the name of the file you modified>  
  ```
  above command makes sure the specific file is tracked
<br />
<br />
```bash
  git commit -m <a message to your teammates>  
  ```
  above code is a "confirmation" of the changes you made
<br />
<br />  
```bash
  git push  
  ```
  and the above code is the last step. The shared code is updated.


## serve on the cloud
for now since we are using Firebase, we have to resort to GCP, which is notorious for its billing plans
- note that you might need to manually install gcloud cli
to serve, go to ``server/`` directory:
```bash
cd server
```
then, build the project on the cloud:
```bash
gcloud builds submit --tag gcr.io/add8474c155291931e21688b027bf9/flask-fire
```
note that the project id is a sha-1 hash of the project name. details in ``util/idGenerator.py`` 
and that the service name is ``flask-fire`` (dumb choice. I know.)
<br />
<br />
Last step, deployment:
```bash
gcloud beta run deploy --image gcr.io/add8474c155291931e21688b027bf9/flask-fire
```
same command break-down as the previous line.
## Serve on Firebase (local host)
Honestly I don't even know why I did this. But it sure looks cool!
You need to be in the root directory of this project, ``BootcampCrypto/``
```bash
./node_modules/.bin/firebase serve
```
And a cooler version of the website will be rendered!

## Important notes:
remember to shut down GCP else we get a financial shipwreck very very soon!
go to google cloud console, make sure that ``Cloud Run --> Services `` are all **deleted**
and that always double-check ``App Engine --> settings`` to verify it is <span style="color: red"> **disabled**</span>
<br/>
<br/>
When you start the app again, remember to go to ``Cloud Run --> Services `` and allow unauthorized access by adding rule:
<br/><br/>``allUsers``<br/><br/> and allow unauthorized invocation by adding role: <br/><br/>``roles/run.invoker``<br/><br/>

## code maintenance/housekeeping
After adding new feature, remember to:
```bash
pip freeze > requirements.txt
```
if you want the cloud version to be updated too, also run
<br/> ``util/requirementUpdate.py``file's main function<br/> 
which will update the requirments needed for Docker image.

## to be continued...
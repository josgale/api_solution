# Python Flask API

#### 1. API

The API was created using Python and the Flask library.

#### 2. Local Setup

For local setup run `./buildAndTest.sh` from the root of the project directory. The local setup is comprised of a `docker-compose` file that will deploy a `flask-app` and `mysql` containers. The bash script will build the containers with docker-compose then run 3 unit tests in the flask app. The provided CSV was used in the testing, to verify we can `/post` the provided users, then verified that we can perform a `/get` on all users, and a `/get` per user ID.

#### 3. Containerization and Orchestration

`kube-deployment.yaml` has two deployments one for `flask-app` and one for `mysql` as well as two services for the deployments, additionally a persistent volume is created for the database. A `.env`, and the database password is set in the deployment file was included, these would be omitted in an actual production environment in favor of Vault, or a secrets manager in AWS, Azure, GCP etc. I left them in for ease of use while testing this sample project

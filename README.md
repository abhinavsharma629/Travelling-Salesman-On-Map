# Travelling Salesman Problem On Map View

## Brief:
  - A web app which accepts multiple sets of location points in the form of :-
     - coordinates
     - area names
     - marker
  - Plots them on a Google Map/Bing Map
  - Find the shortest path which connects all the points and display that on the same map.
  - Also a screen that displays the logs of all the previously computed routes.


## Installation Steps

 ### Server Setup
 This instruction only enable the home module. If you want to enable others, you need to install some other packages listed in
 requirements.txt.

 - First, clone this repo or download the zip of this project.
 - Then, install the dependencies : pip -r requirements.txt
 - SetUp local postgreSQL database server
    - Steps for postgres database server installation : are given below 
 - Apply migrations and run server.
    - py manage.py makemigrations
    - py manage.py migrate
    - py manage.py runserver

## Resources:
  - BING Maps API
  - Django
  - PostgreSQL

---

## PostgreSQL Installation and Setup

### Installation
Before you get started with using PostgreSQL, you'll have to install it.
Follow these steps to get started:

#### MacOS

1. There are a couple of ways to install PostgreSQL. One of the easier ways to
get started is with Postgres.app. Navigate to http://postgresapp.com/ and then
click "Download":
![download](https://cloud.githubusercontent.com/assets/12450298/19641848/6d3cfa4a-99da-11e6-858f-3ff2ada026be.png)

2. Once it's finished downloading, double click on the file to unzip then move
the PostgreSQL elephant icon into your `applications` folder. Double click the
icon to launch the application.

3. You should see a new window launched that says "Welcome to Postgres". If it
says that it cannot connect to the postgres server this means that the DEFAULT
port is probably already in use. Make sure you don't have any other instances of
Postgres on your computer. Uninstall them if you do and then resume with these
steps. Click on the button that says "Open psql":
![open psql](https://cloud.githubusercontent.com/assets/12450298/19642044/463eceae-99db-11e6-8907-bb3a6cc532a7.png)

4. Postgres.app will by default create a role and database that matches your current macOS username. You can connect straight away by running `psql`.

5. You should then see something in your terminal that looks like this (with your macOS username in front of the prompt rather than 'postgres'):
![terminal](https://cloud.githubusercontent.com/assets/12450298/19642816/f8ac0c66-99de-11e6-87e2-db55e6abc27b.png)

6. You should now be all set up to start using PostgreSQL. For documentation on
command line tools etc see http://postgresapp.com/documentation/

#### Ubuntu

Digital Ocean have got a great article on [getting started with postgres]( https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04). A quick summary is below.

##### Installation

```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

By default the only role created is the default 'postgres', so PostgreSQL will only respond to connections from an Ubuntu user called 'postgres'. We need to pretend to be that user and create a role matching our actual Ubuntu username:

```
sudo -u postgres createuser --interactive
```

This command means 'run the command `createuser --interactive` as the user called "postgres"'.

When asked for the name of the role enter your Ubuntu username. If you're not sure, open a new Terminal tab and run `whoami`.

When asked if you want to make the role a superuser, type 'y'.

We now need to create the database matching the role name, as PostgreSQL expects this. Run:

```
sudo -u postgres createdb [your user name]
```

You can now connect to PostgreSQL by running `psql`.

### Create your first PostgreSQL database

1. To start PostgreSQL, type this command into the terminal:  
`psql`  

2. Next type this command into the PostgreSQL interface:  
`CREATE DATABASE test;`  
**NOTE:** Don't forget the semi-colon. If you do, useful error messages won't
show up.

3. To check that our database has been created, type `\l` into the psql prompt.
You should see something like this in your terminal:
![test db](https://cloud.githubusercontent.com/assets/12450298/19650613/ce278678-9a01-11e6-89ad-b124c0adcfe5.png)

### Create new users for your database

1. If you closed the PostgreSQL server, start it again with:  
` psql`  

2. To create a new user, type the following into the psql prompt:  
    ```sql
    CREATE USER testuser;
    ```

3. Check that your user has been created. Type `\du` into the prompt. You should
see something like this:
![user](https://cloud.githubusercontent.com/assets/12450298/19650852/9c340708-9a02-11e6-8f06-75f1e30a86b3.png)
Users can be given certain permissions to access any given database you have
created.

4. Next we need to give our user permissions to access the test database we
created above. Enter the following command into the `psql` prompt:  
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE test TO testuser;
    ```

### Learning Resources

- [Node-hero](https://blog.risingstack.com/node-js-database-tutorial/)
- [Pluralsight](https://www.pluralsight.com/courses/postgresql-getting-started)
- [Tech Republic](http://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/)
- [PostGIS install](http://postgis.net/install/)
- [PostGIS docs](http://postgis.net/docs/manual-2.3/)
- [PostGIS ST_Distance](http://postgis.net/docs/ST_Distance.html)

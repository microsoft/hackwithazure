# az hack

`az hack` is a command-line utility for quickly bootstrapping Azure resources commonly used for a student hack project. With `az hack create` you will be able to spin up and configure databases, web hosting, and even artificial intelligence.

## Provisioned resources

- [Azure App Service plan](https://docs.microsoft.com/azure/app-service/overview-hosting-plans), which creates a VM in Azure for your site
- [Azure App Service](https://docs.microsoft.com/azure/app-service/overview), which will host and run your site
- Database, including [Azure SQL Database](https://docs.microsoft.com/azure/sql-database/), [Azure Database for MySQL](https://docs.microsoft.com/azure/mysql/), or [CosmosDB using Mongo API](https://docs.microsoft.com/azure/cosmos-db/mongodb-introduction)
- Key for [Azure Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/), which can be used to add artificial intelligence into your application

All resources are placed in the same [resource group](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-overview#resource-groups)

> **Pricing Note:** The database and Cognitive Services keys may incur charging. Please consult the documentation for up-to-date pricing information.

### Configuration notes

All generated passwords, keys, and names will be displayed on the screen upon completion of the command. In addition, all values are stored as environmental variables in the website, and can be accessed in your application as such.

> **Note:** To enable an easier-to-read output, use `--output yaml`

> **Note:** You may want to consider using a package such as [Node dotenv](https://www.npmjs.com/package/dotenv), [python-dotenv](https://pypi.org/project/python-dotenv/), [dotenv.net](https://www.nuget.org/packages/dotenv.net/) or [PHP dotenv](https://github.com/vlucas/phpdotenv) to simplify managing environmental variables for your application.

> **Note:** Databases may require additional configuration for access. Please see [database notes](#database) below.

## Installation

`az hack` is an [Azure Command Line Interface (CLI)](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest) [extension](https://docs.microsoft.com/cli/azure/azure-cli-extensions-overview?view=azure-cli-latest).

### Cloud shell

1. Navigate to [https://shell.azure.com](https://shell.azure.com) and authenticate
2. Install the **hack** extension

``` shell
az extension add --name hack
```

### Local installation

If you wish to use the Azure CLI locally, you can perform the installation by following these steps. Because the Azure CLI is based on Python, it can be installed on any operating system. Note you may need to open a new command or terminal window after installing Python.

1. Install [Python](https://python.org)
2. Install [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest)
3. Login

``` shell
az login
```

4. Install the **hack** extension

``` shell
az extension add --name hack
```

## Usage

### Command

``` shell
az hack create --name
           --database {mysql, sql, cosmosdb}
           --runtime {python, tomcat, jetty, php, aspnet, node}
           --location
           [--ai]
```

### Samples

Create a website with Azure Cognitive Services, PHP and MySQL

``` shell
az hack create --name demo --runtime php --database mysql --ai --location westus2 --output yaml
```

Create a website with Azure Cognitive Services and Python

``` shell
az hack create --name demo --runtime python --ai --location westus2 --output yaml
```

Create a website with CosmosDB with Mongo API and Node.js

``` shell
az hack create --name demo --runtime node --database cosmosdb --location westus2 --output yaml
```

### Parameters

#### name

Base name of the application. Must be 10 characters or less. A random set of characters will be placed at the end to ensure uniqueness.

#### runtime

Runtime or framework for website - **tomcat** or **jetty** for Java, **php**, **python**, **aspnet**, **node**

#### database

(Optional) Type of database to create - **cosmosdb** (for Mongo API), **mysql**, or **sql**

> **Note about firewalls** By default, the firewall for **SQL** or **MySQL** will be configured to only allow resources on Azure to connect to your database. To enable your local system to connect, you will need to add your IP address to the [MySQL firewall rules](https://docs.microsoft.com/azure/mysql/howto-manage-firewall-using-cli) or [SQL firewall rules](https://docs.microsoft.com/cli/azure/sql/server/firewall-rule?view=azure-cli-latest). You can determine your systems public IP address by using a search engine and searching "What is my IP".

> **Note for MySQL** If you are using [Azure Databases for MySQL](https://docs.microsoft.com/azure/mysql/), you will need to [enable SSL](https://docs.microsoft.com/azure/mysql/howto-configure-ssl) for your application to connect

#### ai

(Optional) Creates a key for use with Cognitive Services

#### location

[Region](https://azure.microsoft.com/global-infrastructure/regions/) for the application. See full list by using `az location list`

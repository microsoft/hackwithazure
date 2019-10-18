# az hack

`az hack` is a command-line utility for quickly bootstrapping Azure resources commonly used for a student hack project. By using `az hack create`, you can quickly provision

## Provisioned resources

- [Azure App Service plan](https://docs.microsoft.com/azure/app-service/overview-hosting-plans), which creates a VM in Azure for your site
- [Azure App Service](https://docs.microsoft.com/azure/app-service/overview), which will host and run your site
- Database, including [Azure SQL Database](https://docs.microsoft.com/azure/sql-database/), [Azure Database for MySQL](https://docs.microsoft.com/azure/mysql/), or [CosmosDB using Mongo API](https://docs.microsoft.com/azure/cosmos-db/mongodb-introduction)
- Key for [Azure Cognitive Services](https://docs.microsoft.com/azure/cognitive-services/), which can be used to add artificial intelligence into your application

All resources are placed in the same [resource group](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-overview#resource-groups)

> **Pricing Note:** The database and Cognitive Services keys may incur charging. Please consult the documentation for up-to-date pricing information.

### Configuration notes

All generated passwords, keys, and names will be displayed on the screen upon completion of the command. In addition, all values are stored as environmental variables in the website, and can be accessed in your application as such.

> **Note:** You may want to consider using a package such as [Node dotenv](https://www.npmjs.com/package/dotenv), [python-dotenv](https://pypi.org/project/python-dotenv/), [dotenv.net](https://www.nuget.org/packages/dotenv.net/) or [PHP dotenv](https://github.com/vlucas/phpdotenv) to simplify managing environmental variables for your application.

## Installation

`az hack` is an [Azure Command Line Interface (CLI)](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest) [extension](https://docs.microsoft.com/cli/azure/azure-cli-extensions-overview?view=azure-cli-latest), and is designed to be run locally.

### Installation Steps

1. Install [Python](https://python.org)
2. Install [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest)
3. Login

```azurecli-interactive
az login
```

4. Install the **hack** extension

```azurecli-interactive
az extension add --name hack
```

## Usage

### Command

```azurecli-interactive
az hack create --name
           --database {mysql, sql, cosmosdb}
           --runtime {python, tomcat, jetty, php, aspnet, node}
           --location
           [--ai]
```

### Parameters

#### name

Base name of the application. Must be 10 characters or less. A random set of characters will be placed at the end to ensure uniqueness.

#### database

Type of database to create - **cosmosdb** (for Mongo API), **mysql**, or **sql**

> **Note for MySQL** If you are using [Azure Databases for MySQL](https://docs.microsoft.com/azure/mysql/), you will need to [enable SSL](https://docs.microsoft.com/azure/mysql/howto-configure-ssl) for your application to connect

> **Note about firewalls** By default, the firewall for SQL or MySQL will be configured to only allow resources on Azure to connect to your database. To enable your local system to connect, you will need to add your IP address to the [MySQL firewall rules](https://docs.microsoft.com/azure/mysql/howto-manage-firewall-using-cli) or [SQL firewall rules](https://docs.microsoft.com/cli/azure/sql/server/firewall-rule?view=azure-cli-latest). You can determine your systems public IP address by using a search engine and searching "What is my IP".

#### runtime

Runtime or framework for website - **tomcat** or **jetty** for Java, **php**, **python**, **aspnet**, **node**

#### location

[Region](https://azure.microsoft.com/global-infrastructure/regions/) for the application. See full list by using `az location list`

#### ai

(Optional) Creates a key for use with Cognitive Services

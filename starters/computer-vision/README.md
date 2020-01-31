# Computer Vision

This project is designed to be a sample Azure project using [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/). You can use this to see how Computer Vision works, or as a starter for a project you're creating. The sample will allow you to upload an image to Computer Vision and [read printed text](https://docs.microsoft.com/azure/cognitive-services/computer-vision/concept-recognizing-text).

## Requirements

### Git

We will be using [Git](https://git-scm.com/) for both downloading (cloning) the starter code and deploying our project to Azure for hosting. You can install Git by visiting the [Git downloads](https://git-scm.com/downloads) page.

### Python

In order to run the site you will need [Python](https://python.org) installed locally. You can install Python by visiting the [Python downloads](https://www.python.org/downloads/) page.

### Azure Cognitive Services and Azure App Services

To use Computer Vision you will need a key for Azure Cognitive Services. [App Service](https://azure.microsoft.com/services/app-service/) will be used to host our web application. We will create this by using [az hack create](../../az-hack.md) in Azure Cloud Shell.

1. Navigate to the [Cloud Shell](https://shell.azure.com) and authenticate with your Azure account.

> **Note**: Upon first use of Cloud Shell you will be prompted to create a storage account for its use. Cloud Shell needs a little space to store content, such as the extensions you install. This should remain a nominal amount of data.

2. After the shell opens in the browser, issue the following command to install the `az hack` extension.

``` shell
az extension add -n hack
```

3. Issue the following command to create a web app to host your website, and a key for [Cognitive Services](https://azure.microsoft.com/services/cognitive-services/).

> **NOTE**: The command will add a random set of characters to the name you provide (**textdemo** in our example). This ensures the name will always be unique.

> **NOTE**: Our example us using **westus2** as the region in which our resources will be created. When configuring Azure resources, the most important factor for performance is ensuring everything is created in the same region. If you would like to create your project in a region closer to you geographically, you can replace **westus2** with the name of the region you wish to use. However, you will need to [ensure the services are available in the region you choose](https://azure.microsoft.com/global-infrastructure/services/?products=all). All services are available in **westus2**, which is why we're using it as part of this starter.

``` shell
az hack create -n textdemo -r python -l westus2 --ai --output yaml
```

4. **Copy the output.** We will be using several values to complete the creation of our project, specifically:

   - Application settings
     - COGSVCS_CLIENTURL
     - COGSVCS_KEY
   - Deployment info
     - Git url
     - User name
     - Password
   - Website url

## Local setup

1. Open a command or terminal window on your local system. Clone the sample repository.

``` shell
git clone https://github.com/microsoft/hackwithazure
```

1. Navigate to the folder containing the source code for the sample.

``` shell
cd hackwithazure/tutorials/computer-vision
```

3. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html) using Python and install the libraries listed in [requirements.txt](./requirements.txt)

``` shell
# Windows
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

# macOS or Linux
python3 -m venv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```

4. Open the folder in the code editor of your choice. If you are using [Visual Studio Code](https://code.visualstudio.com/) you can use the command below.

``` shell
code .
```

5. Using your code editor, create a new file named **.env**, which is used by [dotenv](https://github.com/theskumar/python-dotenv), to simulate environment variables.

> **NOTE**: The leading **.** is required on the file name.

6. Add the text below, and then update the placeholder `<your url>` with **COGSVCS_CLIENTURL** and `<your key>` with **COGSVCS_KEY** from the values [you created earlier](#azure-cognitive-services-and-azure-app-services) with `az hack create`.

``` shell
COGSVCS_CLIENTURL=<your url>
COGSVCS_KEY=<your key>
```

6. Run your application! Return to the terminal or command window you opened previously, and run the application in flask.

``` shell
# Windows
set FLASK_APP=app.py
flask run

# macOS or Linux
export FLASK_APP=app.py
flask run
```

7. Navigate to **http://localhost:5000**. Click **Upload**, and choose an image (such as **sample.jpg** in this repository) which has text. The image and text will be displayed!

## Deploy your project

Ready to take show your project to the world? If so, you can use [local Git deployment](https://docs.microsoft.com/azure/app-service/deploy-local-git) to deploy your application. `az hack create` has already configured your project; all we need to do is execute the steps.

1. Stop the running site by returning to the command or terminal window and hitting **Ctl-C** (or **Cmd-C** on a Mac).

2. Use the same command or terminal window to [initialize the directory as a Git repository](https://git-scm.com/docs/git-init)

``` shell
git init
```

3. [Add all files to the index](https://git-scm.com/docs/git-add) of the repository and [commit](https://git-scm.com/docs/git-commit) them.

``` shell
git add .
git commit -m "Initial commit"
```

4. Add the [web app you created earlier](#azure-cognitive-services-and-azure-app-services) as a [remote for your repository](https://git-scm.com/docs/git-remote). Replace `<Git url>` with the **Git url** displayed when you executed `az hack create`.

``` shell
git remote add azure <Git url>
```

5. Deploy your code!

``` shell
git push -u azure master
```

Use the **user name** and **password** you copied earlier when you [created your App Service and Cognitive Services key](#azure-cognitive-services-and-azure-app-services). 

> Note: Keep in mind when pasting in your password to the command or terminal window, it will not display. Copy/paste carefully!

When deployed, App Services will use Kudu (the magic behind App Services) to install all Python packages listed in **requirements.txt** just as we did previously, and then run **app.py** to start our website. In addition, the values we used in **.env** were already configured on our website by `az hack create`, so we don't need to update our site with the information for Cognitive Services.

6. Test your site on Azure

Navigate to the URL displayed earlier under **Website url**. Upload a picture with text on it (such as **sample.jpg** in this repository), and you will see it displayed as before!

## Next steps

We've explored one aspect of [Computer Vision](https://azure.microsoft.com/services/cognitive-services/computer-vision/), the ability to extract text from an image. Computer Vision also supports [reading hand-written text](https://docs.microsoft.com/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk#read-printed-and-handwritten-text). More generally, Computer Vision offers you the ability to [recognize objects, detect brands, and locate faces](https://docs.microsoft.com/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk#analyze-an-image). You can update the starter code to add the necessary functionality for your project, and continue to deploy to Azure.

# mrds

## Steps

To create a GitHub repo to connect Sagemaker to

* Create a repo for where the notebook instances will be stored from Sagemaker
* If secrets manager is needed, then create a Personal Access Token in the GitHub repo by going to `settings → Developer settings → Personal access tokens → Generate new token`. Choose an expiration date for the token and select the scope to be just `repo`, which gives full control of private repositories. Click on `Generate new token` and copy the result.

To connect the repo to Sagemaker

* Go to the Sagemaker console and under the notebooks section, select `Git repositories`. Click on `Add repository`.
* Choose the name for the Sagemaker repository name (it might be easier to choose the same name as the GitHub repo)
* Add the repository URL. This can be obtained by going to the `code` section of the repo, clicking on the green `code` button on the top right, and copying the url found in the HTTPS section
* In the Git credentials, select the `Create secret` tick, add the desired secret name, your username and the generated Personal Access Token from GitHub. Click on `Create secret` button once finished
* Click on the `Add repository` button at the bottom

Once the connection is made between the Github repo and Sagemaker a Notebook instance can be made

* Choose the desired selections needed for the Jupyter Notebook
* In the `Git repositories` section, click on the dropdown menu and select the repository that was connected to Sagemaker using the steps listed above
* Finish creating the notebook by clicking the `Create notebook instance` button found at the bottom


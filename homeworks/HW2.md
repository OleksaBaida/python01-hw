# Python Homework #2: Deployment Automation Script

### Description

Your should _develop a deployment automation script_ that automates a deployment process of a web application to a server.

The script should do the _following tasks_:

* Pull the latest code from the the sample application Git repo for https://github.com/rat9615/simple-nodejs-app
* Build and package the web application
* Deploy the application
* Configure any necessary environment variables or settings
* Restart the necessary services to apply the changes
* Implement error handling and rollback mechanisms in case of deployment failures
* Generate a deployment report summarizing the deployment status

### Requirements

1. Create a Python script that automates a deployment process
2. Integrate the script with git to pull latest code from a repository
3. Implement necessary build steps to build and package the web application on a server
4. Deploy the packaged application to a server
5. Configure any necessary environment variables or settings on the target servers to support the application
6. Implement appropriate error handling to detect deployment failures and provide rollback functionality if needed
7. Generate a deployment report that summarizes a deployment to server status, indicating success or failure

### Additional Challenge (Optional)

Extend the deployment automation script to include the following additional features:

* Implement version tracking or tagging mechanisms to ensure traceability and rollback options
* Deployment to multiple servers over SSH
* Multiple reports that summarize information per server

### Submission

Submit your Python script to your GitHub repo, along with any necessary instructions or configuration files

<sub>Note: _Ensure that your script connects securely to remote servers via SSH and automates the deployment process accurately. Handle any potential errors or exceptions gracefully and provide informative output or logs. Test your script against multiple servers and a sample web application to validate its functionality and performance._</sub>

### Example Interaction

Here's an example of how you can interact with the Python script:

Execute script with

```bash
$ python3 deployment_script.py <ip address of server>
```

or

```bash
$ ./deployment_script.py <ip address of server>
```

The script establishes SSH connections to remote servers defined in the configuration file.

It retrieves latest code from the Git repository for server (on each server).

The necessary build steps are executed to build and package the web application.

The packaged application is deployed to the target servers using secure file transfer mechanisms over SSH.

Any required environment variables or settings are configured on the target servers.

The necessary services are restarted to apply the changes.

The script generates a deployment report summarizing the deployment status for each server, indicating success or failure.

Remember to customize the script according to your specific deployment requirements and server configurations.

Useful links

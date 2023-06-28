Python Homework #2: Deployment Automation Script

**Task Description:**
Your task is to _develop a deployment automation script_ that automates the deployment process of a web application on server. 

The script should perform the _following tasks_:
 
* Pull the latest code from a version control system (e.g., Git) for https://github.com/rat9615/simple-nodejs-app application 
* Build and package the web application. 
* Deploy the application. 
* Configure any necessary environment variables or settings. 
* Restart the necessary services to apply the changes. 
* Implement error handling and rollback mechanisms in case of deployment failures. 
* Generate a deployment report summarizing the deployment status.

**Requirements**:

1. Create a Python script that automate the deployment process.
2. Integrate the script with a version control system (e.g., Git) to pull the latest code from the repository.
3. Implement the necessary build steps to build and package the web application on server.
4. Deploy the packaged application on the server.
5. Configure any required environment variables or settings on the target servers to support the application.
6. Implement appropriate error handling to detect deployment failures and provide rollback functionality if needed.
7. Generate a deployment report that summarizes the deployment status for server, indicating success or failure.

**Additional Challenge (Optional):**

Extend the deployment automation script to include the following additional functionalities:
- Implement version tracking or tagging mechanisms to ensure traceability and rollback options.
- multiple servers deployment using SSH
- multiple report that summarize info per server

**Submission:**

Submit your Python script along with any necessary instructions or configuration files to your GitHub repo

Note:
Ensure that your script securely connects to remote servers using SSH and automates the deployment process accurately. Handle any potential errors or exceptions gracefully and provide informative output or logs. Test your script with multiple servers and a sample web application to validate its functionality and performance.

**Example Interaction:**
Here's an example of how you can interact with the Python script:

_Run the script:_

```bash
$ python deployment_script.py or python deployment_script <ip_address of server>
The script establishes SSH connections to the remote servers defined in the configuration file.

It pulls the latest code from the version control system (e.g., Git) repository for server(on each server).

The necessary build steps are executed to build and package the web application.

The packaged application is deployed to the target servers using secure file transfer mechanisms over SSH.

Any required environment variables or settings are configured on the target servers.

The necessary services are restarted to apply the changes.

The script generates a deployment report summarizing the deployment status for each server, indicating success or failure.
```
Remember to customize the script according to your specific deployment requirements and server configurations.

Useful links
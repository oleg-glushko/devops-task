This repo contains the solution for the DevOps task (see its description [below](#test-assignment-for-a-devops-position)). It uses the GitOps methodology, the repo is a source of truth for the deployment configuration.

Backend is written on Flask, by default it's listening on port 5000. To change this port redefine the `FLASK_PORT` environment variable. And don't forget to reflect this adjustment on the frontend counterpart. App accepts incoming GET or POST requests waiting for the body property in an appropriate form.

The frontend is a single-page HTML form using the JavaScript function to make calls to a backend. It's hosted on an NGINX web-server that proxies requests on "`<hostname>/req`" to a `http://backend:5000`. You can change the backend's URL and/or port through environmental variables `BCKND_NAME` & `BCKND_PORT`, accordingly.

All changes (commits) in the ./frontend and ./backend dirs trigger GitHub Actions to create artifacts - container images. A CI pipeline sets the commit SHA as the image's tag to make it unique among other versions.

The continuous delivery pipeline is based on [Flux](https://github.com/fluxcd/flux). You've to install it in your Kubernetes cluster using the next commands.

    export GHUSER=<github-account>
    kubectl create namespace flux
    fluxctl install --git-user=${GHUSER} --git-email=${GHUSER}@users.noreply.github.com --git-url=git@github.com:${GHUSER}/devops-task.git --git-path=./infra --namespace=flux | k apply -f -

This example uses an auto-deployment feature - Flux monitors for image updates and injects new versions directly into manifests from the GitHub's "./infra" directory. You should grant Flux write permissions to your repo. It could be done in your account, use the next URL, just change <username> to your actual GitHub account name:
`https://github.com/<username>/devops-task/settings/keys/new`

Flux automatically generates an SSH key during its installation, you can get it by this command:

    fluxctl identity --k8s-fwd-ns flux

If you don't want to use this feature, you should remove "`fluxcd.io/automated`" annotations from both manifests in the "./infra" directory.

# Test assignment for a DevOps position

The assignment will consist front-end and back-end hosted in a k8s cluster (e.g minikube)

The backend part might be writted in any language out of this list:
* Golang
* Python
* Rust
* Node.js

It should have only one endpoint which will accept requests and in a response returns what method was used and content of the request body.
* Method: Post
* Body: Hello World
* Response: Method Post, Body “Hello World”

Front-end part is a single page application with a simple form consisting of
* Dropdown list with available methods (GET, POST…)
* Text field for body
* Button to be able to send requests
* Text field showing response from the backend

This project should be deployable to a minukube instance via CI/CD pipelines of your choice.

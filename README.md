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

# k8slabelmaker

k8slabelmaker is a Kubernetes Mutating Webhook designed to label all the created pods in the cluster with a predefined set of labels.

## Features

- **Dynamic Labeling**: Automatically applies labels to Kubernetes Pods.
- **Customizable Rules**: Define rules for labeling based on resource specifications or annotations.
- **Easy Integration**: Works seamlessly with existing Kubernetes environments.

### Helm chart ready to be used

Under /chart you will find all the templates you need to deploy the webhook via Helm

DO NOT forget to generate your own certs and populate the "caBundle" inside the mutating-webhook-configuration.yaml
Your certificates should go to a k8s secret named "webhook-certs". The deployment is injecting them into the pod
to be used by the web server.

## Configmap

In the configmap.yaml, you can define the labels you want to add to all of your cluster pods.

## Image

For your convinience, you can build a docker image right from this repo and use it for deploying the webhook

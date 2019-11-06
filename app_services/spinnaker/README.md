
1. Install Halyard
https://www.spinnaker.io/setup/install/halyard/


https://www.spinnaker.io/setup/install/providers/kubernetes-v2/

2. Activate Kubernetes
Within container:
```
hal config provider kubernetes enable
```

3. Configure hal for context Kubernetes connected cluster
For local docker-for-desktop
```
CONTEXT=docker-desktop
hal config provider kubernetes account add my-k8s-v2-account --provider-version v2 --context $CONTEXT
```

4. Now Setup Spinnaker for environment
https://www.spinnaker.io/setup/install/environment/
- Doing prod setup
```
hal config deploy edit --type distributed --account-name my-k8s-v2-account
```

5. Select Spinnaker version
```
hal config version edit --version 1.16.4
hal deploy apply
```

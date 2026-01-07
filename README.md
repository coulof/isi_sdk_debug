# isi_sdk_debug
This quick & dirty project helps to debug isilon PAPI access in [isilon python SDK](https://pypi.org/project/isilon_sdk/).

## Usage
```
kubectl apply -f pod.yaml
```

Then, you can access it with:
```
kubectl exec -it $(kubectl get pod -l app=isi-sdk-pod -o jsonpath='{.items[0].metadata.name}') -- /bin/bash
```

Edit the values in [app.py](app.py) and run it with `python app.py`.
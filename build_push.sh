#! /bin/bash

echo $1
result_string="${2/\:/-}"
echo $result_string
docker build --tag ildoonet/pysc2:$result_string $1/$2
docker push ildoonet/pysc2:$result_string

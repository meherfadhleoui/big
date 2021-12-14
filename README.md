
## Instructions

- Clone project 
```bash
  git clone https://github.com/meherfadhleoui/tpBigData
```

- Copy access.log file to tpBigData folder

- Lancer le cluster
```bash
  docker-compose up 
```
-Se connecter au container exécutant spark-master
```bash
  sudo docker exec -it spark-master bash 
```

- Get top 10 visited websites 
```bash
  ./script.sh 
```

- Get top N visited websites
```bash
    ./script.sh N 
```
- Example 
```bash
  ./script.sh 5 
```
  

## Instructions

- Clone project 
```bash
  git clone https://github.com/meherfadhleoui/bigdata
```

- Copy access.log file to bigdata folder

- Build Image
```bash
  docker build -t bigdata . 
```

- Get top 10 visited websites 
```bash
  docker run -it bigdata 
```

- Get top N visited websites
```bash
  docker run -it bigdata N 
```
- Example 
```bash
  docker run -it bigdata 20 
```
  
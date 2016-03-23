default: build

clean:
	docker rmi bborbe/taiga-backend

build:
	docker build --rm=true -t bborbe/taiga-backend .

run:
	docker run -h example.com -p 8000:8000 bborbe/taiga-backend:latest

bash:
	docker run -i -t bborbe/taiga-backend:latest /bin/bash

upload:
	docker push bborbe/taiga-backend

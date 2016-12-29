VERSION ?= 1.0.0

default: build

clean:
	docker rmi bborbe/taiga-backend:$(VERSION)

build:
	docker build --build-arg VERSION=$(VERSION) --no-cache --rm=true -t bborbe/taiga-backend:$(VERSION) .

run:
	docker run -h example.com -p 8000:8000 bborbe/taiga-backend:$(VERSION)

shell:
	docker run -i -t bborbe/taiga-backend:$(VERSION) /bin/bash

upload:
	docker push bborbe/taiga-backend:$(VERSION)

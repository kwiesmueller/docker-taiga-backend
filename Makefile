VERSION ?= latest

default: build

clean:
	docker rmi kwiesmueller/taiga-backend:$(VERSION)

build:
	docker build --build-arg VERSION=$(VERSION) --no-cache --rm=true -t kwiesmueller/taiga-backend:$(VERSION) .

run:
	docker run -h example.com -p 8000:8000 kwiesmueller/taiga-backend:$(VERSION)

shell:
	docker run -i -t kwiesmueller/taiga-backend:$(VERSION) /bin/bash

upload:
	docker push kwiesmueller/taiga-backend:$(VERSION)

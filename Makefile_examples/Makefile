FILE = ./message.txt
MESSAGE = "Hello, World!"
HASH = $(shell git rev-parse --short HEAD)

.PHONY: clean write read print

write: clean
	echo "$(MESSAGE) - $(HASH)" > $(FILE)
clean:
	-rm *.txt
read: write
	cat $(FILE)
print:
	$(info $(MESSAGE))


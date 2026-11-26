all: producer consumer

producer: producer.cpp
	g++ -Wall -O2 producer.cpp -o producer -lrt -pthread

consumer: consumer.cpp
	g++ -Wall -O2 consumer.cpp -o consumer -lrt -pthread

clean: 
	rm -f producer consumer


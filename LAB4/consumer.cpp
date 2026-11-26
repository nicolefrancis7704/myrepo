# include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>     
#include <sys/mman.h>   
#include <sys/wait.h>
#include <semaphore.h>
#include <signal.h>

#define SHM_NAME "/shm_demo"
#define SEM_MUTEX "/sem_mutex"
#define SEM_FULL "/sem_full"
#define SEM_EMPTY "/sem_empty"

#define NUM_COMM 11
#define HISTORY 5

sem_t *mutex;//1  
sem_t *full;//0
sem_t *empty;//N

typedef struct {char name[11];  float generated_price;}Buffer;
typedef struct {int next_write;  int next_read;   Buffer buf[];}SharedData;
typedef struct {double price_history[HISTORY];  int count; int next_slot; double price; double average; int price_direction; int avg_direction;}Consumer;

const char *names[NUM_COMM]={"ALUMINIUM","COPPER","COTTON","CRUDEOIL","GOLD","LEAD","MENTHAOIL","NATURALGAS","NICKEL","SILVER","ZINC"};

//struct timespec{
//  time_t tv_sec;  seconds
//  long tv_nsec;   nanoseconds
// };
Consumer consumer[NUM_COMM];

void cleanup(int signum){
	sem_close(mutex);
	sem_close(full);
	sem_close(empty);
	sem_unlink(SEM_MUTEX);
	sem_unlink(SEM_FULL);
	sem_unlink(SEM_EMPTY);
	shm_unlink(SHM_NAME);
	printf("\n");
	exit(0);
}

const char *color(int d){ return d>0 ? "\033[32m" : d<0 ? "\033[31m" : "\033[36m"; }
const char *arrow(int d){ return d>0 ? "↑" : d<0 ? "↓" : " "; }

void draw(){
	printf("\033[1;1H\033[2J");
	printf("+---------------------------------------+\n");
	printf("  Currency   |    PRICE    |   AVERAGE  |\n");
	for(int i=0;i<NUM_COMM;i++){
		printf("| %-12s | %s%7.2lf%s\033[0m | %s%7.2lf%s\033[0m |\n", names[i],
       color(consumer[i].price_direction), consumer[i].price, arrow(consumer[i].price_direction),
       color(consumer[i].avg_direction),   consumer[i].average, arrow(consumer[i].avg_direction));
	}
	printf("+---------------------------------------+\n");
	fflush(stdout);
}

void update_consumer(const char *name, double price){
	for (int i=0;i<NUM_COMM;i++){
		if(strcmp(name,names[i])==0){
			Consumer *c=&consumer[i];
			double old_price, old_average;
			old_price=c->price;
			old_average=c->average;
			int first_time=(c->count==0);
			c->price_history[c->next_slot]=price;
			c->next_slot=(c->next_slot+1)%HISTORY;
			if(c->count<HISTORY) c->count++;
			double sum=0;
			for(int j=0;j<c->count;j++){
				sum+=c->price_history[j];
			}
			c->price=price;
			c->average=sum/c->count;
			if (!first_time){
				c->price_direction=(c->price>old_price)?1:(c->price<old_price)?-1:0;
				c->avg_direction=(c->average>old_average)?1:(c->average<old_average)?-1:0;
			}
		}
	}
	return;
}

int main(int argc , char *argv[]){
	if (argc != 2){
		fprintf(stderr,"Usage:%s <buffer_size>\n" , argv[0]);	exit(1);
	}
	int N=atoi(argv[1]);
	if(N<=0 ){
		fprintf(stderr,"Invalid buffer size\n");	exit(1);
	}
	size_t size = sizeof(SharedData)+N*sizeof(Buffer);
	int shm_fd=shm_open(SHM_NAME,O_CREAT | O_RDWR , 0666);
	if (shm_fd == -1) {
       	        perror("shm_open failed"); exit(1);
    	}
	if(ftruncate(shm_fd,size)==-1){
		perror("ftruncate failed");	exit(1);
	}
	SharedData *data=(SharedData *)mmap(NULL,size,PROT_READ | PROT_WRITE , MAP_SHARED , shm_fd , 0);
	if(data == MAP_FAILED){
		perror("mmap failed");	exit(1);
	}
	close (shm_fd);
	mutex=sem_open(SEM_MUTEX,O_CREAT,0666,1);
	full=sem_open(SEM_FULL,O_CREAT,0666,0);
	empty=sem_open(SEM_EMPTY,O_CREAT,0666,N);
	if(mutex == SEM_FAILED || full ==SEM_FAILED || empty == SEM_FAILED){
		perror("sem_open failed"); exit(1);
	}
	signal(SIGINT,cleanup);// cltr c
	signal(SIGTERM,cleanup);// kill or shutdown
    draw();
	
	while(1){
		sem_wait(full);
		sem_wait(mutex);
		Buffer item=data->buf[data->next_read];
		data->next_read = (data->next_read + 1)%N;
		sem_post(mutex);
		sem_post(empty);
		update_consumer(item.name, item.generated_price);
		draw();
	}
return 0;
}

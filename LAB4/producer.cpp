# include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>     
#include <sys/mman.h>   
#include <sys/wait.h>
#include <semaphore.h>
#include <random>
#include <time.h>

#define SHM_NAME "/shm_demo"
#define SEM_MUTEX "/sem_mutex"
#define SEM_FULL "/sem_full"
#define SEM_EMPTY "/sem_empty"

sem_t *mutex;//1  
sem_t *full;//0
sem_t *empty;//N

typedef struct {char name[11];	float mean_price;   float standard_deviation_price;	int length_sleep;   int buffer_size;}Producer;
typedef struct {char name[11];  float generated_price;}Buffer;
typedef struct {int next_write;  int next_read;   Buffer buf[];}SharedData;

//struct timespec{
//  time_t tv_sec;  seconds
//  long tv_nsec;   nanoseconds
//};


void logmsg (const char *name , const char *msg , double val , int flag){
	struct timespec ts ;
	clock_gettime(CLOCK_REALTIME,&ts);
	struct tm t;
	localtime_r(&ts.tv_sec,&t);
	char tb[32];
	strftime(tb,sizeof tb,"%m/%d/%Y %H:%M:%S",&t);
	if(flag)
		fprintf(stderr,"[%s.%03ld] %s: %s %.2f\n",tb,ts.tv_nsec/1000000,name,msg,val);
	else
		fprintf(stderr,"[%s.%03ld] %s: %s\n",tb,ts.tv_nsec/1000000,name,msg);
}

int main(int argc , char *argv[]){
	if (argc != 6){
		fprintf(stderr,"Usage:%s <name> <mean> <standard_deviation> <sleep_ms> <buffer_size>\n" , argv[0]);
		exit(1);
	}
	Producer p;
	strncpy(p.name,argv[1],10);
	p.name[10]='\0';
	p.mean_price=atof(argv[2]);
	p.standard_deviation_price=atof(argv[3]);
	p.length_sleep=atoi(argv[4]);
	p.buffer_size=atoi(argv[5]);
	size_t size = sizeof(SharedData)+p.buffer_size*sizeof(Buffer);
	int shm_fd=shm_open(SHM_NAME,O_CREAT | O_RDWR , 0666);
	if (shm_fd == -1) {
       	        perror("shm_open failed"); exit(1);
    	}
	if(ftruncate(shm_fd,size)==-1){
		perror("ftruncate failed");	exit(1);
	}
	SharedData *data= (SharedData *)mmap(NULL,size,PROT_READ | PROT_WRITE , MAP_SHARED , shm_fd , 0);
	if(data == MAP_FAILED){
		perror("mmap failed");	exit(1);
	}
	close (shm_fd);
	mutex=sem_open(SEM_MUTEX,O_CREAT,0666,1);
	full=sem_open(SEM_FULL,O_CREAT,0666,0);
	empty=sem_open(SEM_EMPTY,O_CREAT,0666,p.buffer_size);
	if(mutex == SEM_FAILED || full ==SEM_FAILED || empty == SEM_FAILED){
		perror("sem_open failed"); exit(1);
	}
	std::random_device rd;
	std::mt19937 gen(rd());
	std::normal_distribution<double> dist(p.mean_price,p.standard_deviation_price);

	while(1){
		double price = dist(gen);
		logmsg(p.name,"generating a new value",price,1);
		sem_wait(empty);
		logmsg(p.name,"trying to get mutex on shared buffer",0,0);
		sem_wait(mutex);
		logmsg(p.name,"placing value on shared buffer",price,1);
		strcpy(data->buf[data->next_write].name,p.name);
		data->buf[data->next_write].generated_price=price;
		data->next_write = (data->next_write + 1)%p.buffer_size;
		sem_post(mutex);
		sem_post(full);
		char msg[100];
		snprintf(msg,sizeof msg ,"sleeping for %d ms",p.length_sleep);
		logmsg(p.name,msg,0,0);
		usleep(p.length_sleep*1000);
	}
return 0;
}

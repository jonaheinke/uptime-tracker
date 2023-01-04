//Should this be solved with POSIX timers?
//https://man7.org/linux/man-pages/man2/timer_create.2.html

#define INTERVAL 60 //every minute (in seconds)

/* ----------------------------------------------------- INCLUDE ---------------------------------------------------- */

#include<stdio.h>
#include<stdlib.h>
//#include<signal.h>
#include<time.h>

#ifdef _WIN32
#include<Windows.h>
unsigned int sleep(unsigned int seconds) {
	Sleep(seconds * 1000);
	return 0;
}
#else
#include<unistd.h>
#endif



/* ------------------------------------------------------ MAIN ------------------------------------------------------ */
FILE *file = NULL;

void close_file() {
	//skip if file is already closed
	if(!file) return;
	//clear buffers
	fflush(file);
	//close file
	if(fclose(file)) {
		printf("Error closing file\n");
		//TODO: What to do now?
		return;
	}
	file = NULL;
}

void exit_handler() {
	printf("Exit handler called\n");
	//if program is terminated while file is being written, wait one second for it to finish
	if(file) sleep(1);
}

void save_time() {
	file = fopen("time.txt", "w");
	if(!file) {
		printf("Error opening file\n");
		return;
	}
	//fprintf();
	time_t now = time(NULL);
	if(now == -1) {
		printf("Error retrieving the current time\n");
		return;
	}
	struct tm *timeinfo = localtime(&now);
	printf("%d.%d.%d - %d:%d:%d\n", timeinfo->tm_mday, timeinfo->tm_mon + 1, timeinfo->tm_year + 1900, timeinfo->tm_hour, timeinfo->tm_min, timeinfo->tm_sec);
	close_file();
}

int main() {
	//register exit handler
	//https://man7.org/linux/man-pages/man3/atexit.3.html
	int failure = atexit(exit_handler);
	if(failure) {
		printf("Error registering exit handler");
	}
	//main loop
	while(1) {
		save_time();
		sleep(INTERVAL); //sleep for 1 second
	}
	//should never be reached
	return(0);
}
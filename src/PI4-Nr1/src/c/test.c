//-------------------------------------------------------------------------------------------------------------------------//
//General

//#include<pthread.h>
//ld: -pthread

//-------------------------------------------------------------------------------------------------------------------------//
//Joinable

pthread_t           PollThread;
pthread_attr_t      PollThreadAttribute;
void               *PollThreadStatus;
long                PollThreadId;

	pthread_attr_init(&PollThreadAttribute);
	pthread_attr_setdetachstate(&PollThreadAttribute, PTHREAD_CREATE_JOINABLE);
	pthread_create(&PollThread, &PollThreadAttribute, PollThreadWrapper, (void *) PollThreadId);

	pthread_join(PollThread, NULL);
	pthread_attr_destroy(&PollThreadAttribute);

//-------------------------------------------------------------------------------------------------------------------------//
//Detached

pthread_t           ListenerThread;
pthread_attr_t      ListenerThreadAttribute;
void               *ListenerThreadStatus;
long                ListenerThreadId;

	pthread_attr_init(&ListenerThreadAttribute);
	pthread_attr_setdetachstate(&ListenerThreadAttribute, PTHREAD_CREATE_DETACHED);
	pthread_create(&ListenerThread, &ListenerThreadAttribute, ListenerThreadWrapper, (void *) ListenerThreadId);

//-------------------------------------------------------------------------------------------------------------------------//
//Simple Routine

void Test()
{
	//
}

void *TestThread(void *TID)
{
	//ID
	long ID = (long) TID;

	Test();

	//Result
	pthread_exit(NULL);
}

//-------------------------------------------------------------------------------------------------------------------------//
//Complex Routine

void RequestOut(ConnectionData *Connection)
{
	//
}

void *RequestThreadWrapper(void *ConnectionBox)
{
	//ID
	ConnectionData *Connection = (ConnectionData *) ConnectionBox;

	RequestOut(Connection);

	//Result
	pthread_exit(NULL);
}

//-------------------------------------------------------------------------------------------------------------------------//
//Complex Object Pass Routine

void *PackageMultiplexerOutThreadWrapper(void *Box)
{
	QueueOut *Object = (QueueOut *) Box;
	Object->PackageMultiplexerOut();

	pthread_exit(NULL);
}

pthread_create(&PackageMultiplexerOutThread, &PackageMultiplexerOutThreadAttributes, PackageMultiplexerOutThreadWrapper, (void *) this);

//-------------------------------------------------------------------------------------------------------------------------//
//Cancel State

//Internal (Beginning)
int Old;
pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, &Old);
pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, &Old);

//External (Create joinable recommended)
pthread_cancel(PollThread);
pthread_join(PollThread, NULL);
pthread_attr_destroy(&PollThreadAttribute);

//-------------------------------------------------------------------------------------------------------------------------//
//Mutex

pthread_mutex_t ListenerLock;

	pthread_mutex_init(&ListenerLock, NULL);

	pthread_mutex_lock(&ListenerLock);
	//Action
	pthread_mutex_unlock(&ListenerLock);

	pthread_mutex_destroy(&ListenerLock);

//-------------------------------------------------------------------------------------------------------------------------//
//Barrier

pthread_barrier_t ListenStartBarrier;

	pthread_barrier_init(&ListenStartBarrier, NULL, 2); //2x
	pthread_barrier_wait(&ListenStartBarrier); // 1/2
	pthread_barrier_wait(&ListenStartBarrier); // 2/2
	pthread_barrier_destroy(&ListenStartBarrier);

//-------------------------------------------------------------------------------------------------------------------------//
//Semaphore

#include<semaphore.h>

sem_t OutQueueSemaphore;

	//Init
	sem_init(&OutQueueSemaphore, 0, 0);

	//Signal
	sem_post(&OutQueueSemaphore);

	//Sleep
	sleep(1);

	//Wait
	sem_wait(&OutQueueSemaphore);

	//Free
	sem_destroy(&OutQueueSemaphore);

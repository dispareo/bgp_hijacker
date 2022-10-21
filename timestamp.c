#include <stdio.h>
#include <inttypes.h>
#include <time.h>

int64_t millis()
{
    struct timespec now;
    timespec_get(&now, TIME_UTC);
    return ((int64_t) now.tv_sec) * 1000 + ((int64_t) now.tv_nsec) / 1000000;
}


int main (void)
{
        FILE *fp;
        fp = fopen("Output.txt", "a");// "w" means that we are going to write on this file
        fprintf(fp, "BGP packet first received: %ld\n", millis());
        fclose(fp);
}

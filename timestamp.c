#include <stdio.h>
#include <inttypes.h>
#include <time.h>

int64_t millis()
{
    struct timespec now;
    timespec_get(&now, TIME_UTC);
    return ((int64_t) now.tv_sec) * 1000 + ((int64_t) now.tv_nsec) / 1000000;
}

int print_to_file (void)
{
        FILE *fp;
        fp = fopen("/tmp/timestamps.txt", "a");// TIL "a" means append. 
        fprintf(fp, "BGP packet first received: %lld\n", millis());
        fclose(fp);
}

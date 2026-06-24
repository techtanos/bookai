#include <stdio.h>
int main() {
    //  Open file for writing
    FILE *file = fopen("drone_log.txt", "w");
    // Write drone data
    fprintf(file, "Flight 1: mass=2.5kg, speed=10m/s, force=24.5N\n");
    fprintf(file, "Flight 2: mass=3.7kg, speed=15m/s, force=36.3N\n");
    fprintf(file, "Flight 3: mass=9.9kg, speed=20m/s, force=97.0N\n");
    //Close file;
    fclose(file);
    printf("Flight data saved to drone_log.txt\n");
    return 0;
}

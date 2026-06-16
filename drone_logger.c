#include <stdio.h>
#include <string.h>

struct Drone {
    char name[20];
    float mass;
    float speed;
};

int main() {
    // Create 3 drones
    struct Drone d1, d2, d3;
    strcpy(d1.name, "Eagle-1");
    strcpy(d2.name, "Eagle-2");
    strcpy(d3.name, "Eagle-3");
    d1.mass = 3.7;
    d1.speed = 15;
    d2.mass = 7;
    d2.speed = 17;
    d3.mass = 2.7;
    d3.speed = 12000;
    
    // Calculate forces
    float f1 = d1.mass * 9.8;
    float f2 = d2.mass * 9.8;
    float f3 = d3.mass * 9.8;
    // Open file and write
    FILE *file = fopen("drone_data.txt", "w");
    fprintf(file, "%s: mass=%.1fkg, force=%.1fN\n", d1.name, d1.mass, f1);
    fprintf(file, "%s: mass=%.1fkg, force=%.1fN\n", d2.name, d2.mass, f2);
    fprintf(file, "%s: mass=%.1fkg, force=%.1fN\n", d3.name, d3.mass, f3);
    fclose(file);
    
    // Print confirmation
    printf("Saved to drone_data.txt\n");
    
    // Read file back
    FILE *read = fopen("drone_data.txt", "r");
    char line[100];
    while(fgets(line, 100, read)) {
        printf("%s", line);
    }
    fclose(read);
    
    return 0;
}
